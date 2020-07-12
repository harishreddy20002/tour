
from django.contrib import admin

from . import views

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),

    path('tourguide/',include('tourguide.urls')),
    


]
