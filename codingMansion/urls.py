"""codingMansion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path,include
from . import views
from tutorials import views as tv

from user import views as user_view
from django.contrib.auth import views as auth


def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/',include('portfolio.urls')),
    path('tutorials/', include('tutorials.urls')),
    path('blogs/', include('blog.urls')),
    path('',views.home,name='home'),
    path('contactus', views.contactus,name='contactus'),
    path('about',views.about,name='about'),
    path('search',tv.search,name='search'),
    path('index',views.home,name='home'),

    ##### user related path##########################
	path('login/', user_view.Login, name ='login'),
	path('logout/', auth.LogoutView.as_view()),
	path('register/', user_view.register, name ='register'),

    ######################### blog ######################

    # path('blog/',include('blog.urls')),

    ############     error handler #######################33
    path("404/", custom_page_not_found),



]
