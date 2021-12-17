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

from django.urls import path
from . import views
from codingMansion import views as v
from django.shortcuts import redirect


urlpatterns = [
    path('index',views.playlist,name='playlist'),
    path('video',views.video,name='video'),
    path('about',v.about,name='about'),
    path('portfolio/',v.portfolio,name='portfolio'),
    path('search',views.search,name='search'),
    path('contactus',v.contactus,name='contactus'),
]
