from django.contrib import admin
from .models import UserData, Album, Posts

# Register your models here.
admin.site.register(UserData)
admin.site.register(Posts)
admin.site.register(Album)