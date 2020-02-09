from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^dashboard/$',views.dashboard,name="Admin Dashboard"),
    url(r'^dashboard/rooms/$',views.rooms,name="Rooms"),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^add_room/$',views.add_room,name="add_room"),
    url(r'^add_new_room/$',views.add_new_room,name="add_new_room"),
    url(r'^profile/$',views.profile,name="profile"),
    url(r'^logout/$',views.logout_view,name="logout"),
    url(r'^reserve/$',views.reserve,name="reserve"),

]
