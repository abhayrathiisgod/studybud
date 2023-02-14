from django.db import models
# the below one is built in in java
from django.contrib.auth.models import User 
# Create your models here.
# we create dtabse here

#table for room
#a topic can have multiple rooms
class Topic(models.Model):
    name= models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Room(models.Model):
    host =  models.ForeignKey(User , on_delete=models.SET_NULL,null=True)
    topic= models.ForeignKey(Topic , on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # can be blank
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True) # diffrence is takes only 1 time stamp when we save up one takes of everytime
    
    class Meta:
        # - is added to get the new one on top
        ordering = ['-updated','-created']


    def __str__(self):
        return self.name 
    

class Message(models.Model):
    #user one to many relation
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # one to many relation
    room = models.ForeignKey(Room , on_delete=models.CASCADE) # parent key -- cascade means delete so if the room us deleted so will other 
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True) # diffrence is takes only 1 time stamp when we save up one takes of everytime

    def __str__(self): #object into string
        return self.body[0:50] # only first 50 char


