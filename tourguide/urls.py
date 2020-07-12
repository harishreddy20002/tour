
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("login",views.login,name="login"),
    path("registration",views.registration,name="registration"),
    path("portal",views.portal,name="portal"),
    path("getl",views.getl,name="getl"),
    path("getm",views.getm,name="getm"),
    path("locdet",views.locdet,name="locdet")


]
