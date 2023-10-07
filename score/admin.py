from django.contrib import admin

from .models import ScoreModel

# Registering User models into admin site.
admin.site.register(ScoreModel)