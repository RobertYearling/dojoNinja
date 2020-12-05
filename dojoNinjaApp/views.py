from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja #This is the data being pulled in from the models.py file

# Create your views here.

def index(request):
    context = {
        "all_dojo" : Dojo.objects.all(), #all_dojos is the info that the HTML File will be looking at : the second half is what is need to pull data from the database.
        "all_ninja" : Ninja.objects.all()
    }
    return render(request, "index.html", context)

def dojo(request):
    Dojo.objects.create(name = request.POST['dojo_name'], city = request.POST['dojo_city'], state = request.POST['dojo_state'])
    return redirect('/')

def ninja(request):
    Ninja.objects.create(first_name = request.POST['ninja_fname'], last_name= request.POST['ninja_lname'], student = Dojo.objects.get(id=request.POST['ninja_dojo']))
    return redirect('/')

def delete(request):
    Dojo.objects.get(id=request.POST['dojo_id']).delete()
    return redirect('/')