from django.contrib import admin
from .models import *

# Registering all models into django admin site.
admin.site.register(Category)
class AnswerAdmin(admin.StackedInline):
    model=Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerAdmin]

admin.site.register(Question,QuestionAdmin)

admin.site.register(Answer)
