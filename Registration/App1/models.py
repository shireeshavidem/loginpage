from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Registration(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    
    class meta:
        model = User
        fields = ('username','password1','passwrod2','email')
    
    def save(self, commit: True):
        user = super(Registration,self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user