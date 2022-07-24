from django.contrib import admin

# Register your models here.
from .models import Job, Application

admin.site.register(Job)
admin.site.register(Application)