from django.db import models
import uuid as unique_id
from accounts.models import UserProfile

class BaseModel(models.Model):
    _id= models.UUIDField(primary_key=True,editable=False,default=unique_id.uuid4)
    created_at= models.DateField(auto_now=True)
    updated_at= models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class ScoreModel(BaseModel):
    user = models.ForeignKey(UserProfile, related_name='scores', on_delete=models.CASCADE)
    score_date = models.DateTimeField(auto_now=True)
    score_value = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'User Scores'

    def __str__(self):
        full_name = f"{self.user.first_name} {self.user.last_name}"
        return f"{full_name}"
