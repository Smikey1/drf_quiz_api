from django.db import models
import uuid as unique_id

# Creating Base Model.
class BaseModel(models.Model):
    _id= models.UUIDField(primary_key=True,editable=False,default=unique_id.uuid4)
    created_at= models.DateField(auto_now=True)
    updated_at= models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

# Creating Category Model
class Category(BaseModel):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = 'Categories'

# Creating Question Model
class Question(BaseModel):
    category = models.ForeignKey(Category,related_name="category",on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    mark = models.IntegerField(default=5)

    
    def __str__(self):
        return self.question_text
    
    class Meta:
        verbose_name_plural = 'Questions'

# Creating Answer Model
class Answer(BaseModel):
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey('Question', related_name='options', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.answer_text
    
    class Meta:
        verbose_name_plural = 'Answers'
