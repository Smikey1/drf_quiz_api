from django.contrib import admin

from .models import User
# Registering User models into admin site.
admin.site.register(User)