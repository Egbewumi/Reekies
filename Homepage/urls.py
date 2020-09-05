from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('care', views.care, name="care"),
    path('hold', views.hold, name="hold"),
    path('kitchen', views.kitchen, name="kitchen"),


]
