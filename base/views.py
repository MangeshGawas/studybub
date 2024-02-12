from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
rooms = [
    {'id':1, 'name':"lets learn the python"},
    {'id':2, 'name':"lets learn the angular"},
    {'id':3, 'name':"lets learn the react"},
]

def home(request):
    return render(request, 'home.html',{'rooms':rooms})
def room(request):
    return render(request, 'room.html')