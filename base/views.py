from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id':1 , 'name': 'Lets learn python!'},
#     {'id':2 , 'name': 'Design with me'},
#     {'id':3 , 'name': 'Front end developers'},
# ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') !=None else ''

    #                         the below atleast contains above query
    rooms = Room.objects.filter(Q(topic__name__icontains=q)) # gives all room in databse
    topics = Topic.objects.all() 
    
    context = {'rooms':rooms, 'topics':topics}
    return render(request, 'base/home.html', context)

def room(request,pk): # pk is primary key
    room = Room.objects.get(id=pk) # one single item
    context ={'room': room}
    return render(request, 'base/room.html',context)
def  createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # can do manually
        # request.POST.get('name')
        #print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html',context)


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form  = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request, 'base/room_form.html',context)

# pk is primary key to know which room we are deleting
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})