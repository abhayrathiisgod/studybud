from django.contrib import admin

# Register your models here.
# basically saying we want to work and view this
from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)



