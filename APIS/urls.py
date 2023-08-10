from .views import *
from django.urls import path

urlpatterns=[
    path('USERS',PANTERAAPI.as_view(),name="USERS"),
    path('FEEDBACKS',FEEDBACKAPI.as_view(),name="FEEDBACKS"),
]