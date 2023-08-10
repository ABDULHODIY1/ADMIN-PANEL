from django.db import models


class PANTERAUSERS(models.Model):
    user_id=models.CharField(max_length=200, null=True, blank=True)
    name= models.CharField(max_length=200, null=True, blank=True)
    user_name=models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Feedback(models.Model):
    user_id = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(null=True,blank=True)
    Text = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)