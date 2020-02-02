from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm,add_room_form
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import *

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
          print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'home.html', {'form': form})


def activate(request, uidb64, token):
  try:
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
  except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    user = None
  if user is not None and account_activation_token.check_token(user, token):
    user.is_active = True
    user.save()
    login(request, user)
    # return redirect('home')
    return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
  else:
    return HttpResponse('Activation link is invalid!')

def index(request):
  form = SignupForm()
  return render(request,"home.html",{'form':form})

def add_room(request):
    form = add_room_form()
    return render(request,"add_new_room.html",{"form":form})
def add_new_room(request):
    if request.method=="POST":
            vacant = 0
            if request.POST.get("Vacanttype1") == ["on"]:
                vacant = 0
            elif request.POST.get("Vacanttype2") == ["on"]:
                vacant = 1
            print(request.FILES)
            my_form_data = add_room_form(request.POST, request.FILES)
            if my_form_data.is_valid():
                myform_clean = my_form_data.cleaned_data
                myform = Room(no=myform_clean['no'], name=myform_clean['name'],
                             room_type=myform_clean['room_type'], vacant=vacant
                              ,images=myform_clean['images'],default_price=myform_clean['default_price'])
                myform.save()
    return redirect("/dashboard/")

def dashboard(request):
    return render(request,"admin_dashboard.html")
def rooms(request):
    queryrooms=Room.objects.all()

    return render(request,"rooms.html",{"allrooms": queryrooms})

def login_view(request):
  if request.method=="POST":
    email = request.POST["email"]
    password = request.POST["password"]
    authuser = None
    user = None
    try:
      authuser = User.objects.get(email=email)
    except ObjectDoesNotExist:
            render(request,"home.html", {"notification":"کاربر موجود نمی‌باشد ایمیل خود را تصحیح کنید","notification_type":"error"})
    if authuser:
      user = authenticate(request,username=authuser.username,password=password)
    if user is not None:
      login(request,user)
      return render(request,"home.html", {"notification":"وارد شدید","notification_type":"success"})
    else:
      return render(request,"home.html", {"notification":"ایمیل یا پسورد شما نادرست است","notification_type":"error"})
  else:
    return render(request, "home.html")


def profile(request):
    current_user = request.user
    profile_exists = 1
    theuser = None
    try:
        theuser = Users.objects.get(User.objects.get(pk=current_user))
    except Exception as e:
        theuser = User.objects.get(pk=current_user.pk)
        profile_exists = 0
    if profile_exists==0:
        return render(request,"finish_profile.html",{"myuser":theuser})
    elif profile_exists==1:
        return render(request, "profile.html", {"myuser":theuser})


def logout_view(request):
  logout(request)
  return render(request,"home.html",{"notification":"خارج شدید","notification_type":"success"})



	
	
