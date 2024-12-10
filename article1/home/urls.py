from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('1',views.abouts,name="about"),
    path('one/<int:pk>',views.details,name='details'),
]