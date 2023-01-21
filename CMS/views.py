from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import NewUserForm
from django.contrib import messages



def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = True
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/blog/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


