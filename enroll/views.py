from django.shortcuts import render, HttpResponse, redirect
from .forms import UserRegistration
from .models import User
from django.contrib import messages

# Create your views here.


def add_show(request):
    if request.method == "POST":
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = UserRegistration()

    fm = UserRegistration()
    stud = User.objects.all()
    return render(request, "enroll/addandshow.html", {"form": fm, "stu": stud})


def delete_data(request, id):
    if request.method == "POST":
        us_data = User.objects.get(pk=id)
        us_data.delete()
        return redirect("addandshow")


def update_record(request, id):
    if request.method == "POST":
        update_user = User.objects.get(pk=id)
        fm = UserRegistration(request.POST, instance=update_user)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Data updated successfully.')

    else:
        update_user = User.objects.get(pk=id)
        fm = UserRegistration(instance=update_user)
    return render(request, "enroll/update.html", {"form": fm})
