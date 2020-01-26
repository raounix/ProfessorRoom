from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255,help_text="Required")

    class Meta:
        model = User
        fields = ('email','username','password1','password2')


class add_room_form(forms.Form):
    room_choice = [('1', 'یک تخته'), ('2', "دو تخته"), ("3", "۳ تخته"), ("4", "۴ تخته")]
    no = forms.CharField(max_length=5)
    name = forms.CharField(max_length=255)
    images = forms.ImageField()
    default_price = forms.IntegerField()
    room_type = forms.CharField(max_length=1)
    def clean(self):
        cleaned_data = super(add_room_form,self).clean()
        no = cleaned_data.get("no")
        name = cleaned_data.get("name")
        images = cleaned_data.get("images")
        default_price = cleaned_data.get("default_price")
        room_type = cleaned_data.get("room_type")

