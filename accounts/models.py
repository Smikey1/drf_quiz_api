from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
import uuid as unique_id

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class BaseModel(models.Model):
    _id= models.UUIDField(primary_key=True,editable=False,default=unique_id.uuid4)
    created_at= models.DateField(auto_now=True)
    updated_at= models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class UserProfile(models.Model):
    _id= models.UUIDField(primary_key=True,editable=False,default=unique_id.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    bio = models.TextField(max_length=255,blank=True)
    score = models.IntegerField(default=0)
    num_of_quiz_played = models.IntegerField(default=0)
    profile_url = models.CharField(max_length=255,blank=True)
    created_at= models.DateField(auto_now=True)
    updated_at= models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
