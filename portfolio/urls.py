from django.urls import path
from . import views
from codingMansion import views as v


urlpatterns = [
    path('',views.index,name='index'),
    path('contacts',views.contact,name='contact'),
    path('about',v.about,name='about'),
]
