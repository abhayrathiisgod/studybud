from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms = [
#     {'id':1 , 'name': 'Lets learn python!'},
#     {'id':2 , 'name': 'Design with me'},
#     {'id':3 , 'name': 'Front end developers'},
# ]

def home(request):
    rooms = Room.objects.all() # gives all room in databse
    context = {'rooms':rooms}
    return render(request, 'base/home.html',{'rooms':rooms})

def room(request,pk): # pk is primary key
    room = Room.objects.get(id=pk) # one single item
    context ={'room': room}
    return render(request, 'base/room.html',context)
