from django.shortcuts import render, HttpResponse, redirect
from .models import dojos, ninjas
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "all_the_dojos": dojos.objects.all(),
        "all_the_ninjas": ninjas.objects.all()
    }
    return render(request, "index.html", context)

def process_dojo(request):
    if request.method == "POST":
        dojos.objects.create(
            name = request.POST['name'],
            city = request.POST['city'],
            state = request.POST['state']
            )
        return redirect("/")
    else:
        return redirect("/")

def process_ninja(request):
    if request.method == "POST":
        errors = ninjas.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for error in errors.values():
                messages.error(request, error)
            return redirect("/")

        selected_dojo = dojos.objects.get(id= request.POST['dojo_id'])
        ninjas.objects.create(
            dojo = selected_dojo, 
            first_name = request.POST['first_name'], 
            last_name = request.POST['last_name']
        )
        return redirect("/")
    else:
        return redirect("/")

def delete_dojo(request):
    if request.method == "POST":
        dojo_to_delete = dojos.objects.get(id = request.POST['delete_dojo'])
        dojo_to_delete.delete()
        return redirect("/")
    else:
        return redirect("/")