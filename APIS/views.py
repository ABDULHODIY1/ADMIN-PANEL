# from django.shortcuts import render
# from django.views.generic import *
from .serializers import PANTERASERIALIZERS,FeedbackSerializers
from rest_framework.generics import ListCreateAPIView
from .models import *
# # Create your views here.
#
class PANTERAAPI(ListCreateAPIView):
    queryset = PANTERAUSERS.objects.all()
    serializer_class = PANTERASERIALIZERS

class FEEDBACKAPI(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers