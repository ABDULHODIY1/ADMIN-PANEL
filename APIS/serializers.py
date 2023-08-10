from .models import *
from rest_framework.serializers import *

class PANTERASERIALIZERS(ModelSerializer):
    class Meta:
        model=PANTERAUSERS
        fields=[
            'name','user_id','user_name','date'
        ]

class FeedbackSerializers(ModelSerializer):
    class Meta:
        model=Feedback
        fields=[
            'user_id','Text','image','date'
        ]