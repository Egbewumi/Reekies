from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, "home.html", {})

def contact(request):
    if request.method == 'POST':
        Name = request.POST["Name"]
        Email= request.POST["Email"]
        Message = request.POST["Message"]

        send_mail(
            Name,
            Message,
            Email,
            ['jay.touch@yahoo.com'],
        )
        return render(request, "contact.html", {'Name': Name})

    else:
        return render(request, "contact.html", {})


def care(request):
    return render(request, "care.html", {})

def hold(request):
    return render(request, "hold.html", {})

def kitchen(request):
    return render(request, "kitchen.html", {})

# Create your views here.
