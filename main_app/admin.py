from django.contrib import admin

# Register your models here.


from .models import Application

admin.site.register(Application)

from .models import Status

admin.site.register(Status)