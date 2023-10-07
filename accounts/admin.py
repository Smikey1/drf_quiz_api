from django.contrib import admin

from .models import *
# Registering User models into admin site.
admin.site.register(UserProfile)