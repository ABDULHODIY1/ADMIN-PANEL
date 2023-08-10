from .views import *
from django.urls import path

urlpatterns=[
    path('user',Collectuser.as_view(),name="HOME")
]