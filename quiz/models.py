from django.db import models
import uuid as unique_id

# Creating Base Model.
class BaseModel(models.Model):
    _id= models.UUIDField(primary_key=True,editable=False,default=unique_id.uuid4)
    created_at= models.DateField(auto_now=True)
    updated_at= models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
