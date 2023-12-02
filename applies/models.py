from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AvaliableCourses(models.Model):
    country = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    timeline = models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.country} -- {self.last_updated}'
    

class ApplyCourse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(AvaliableCourses,on_delete=models.SET_NULL,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_decline = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} -- {self.course}'