from django.shortcuts import render
from django.contrib import messages
from portfolio_app.models import mails

# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST.get("cf-name")
        email=request.POST.get("cf-email")
        msg=request.POST.get("cf-message")
        mail_obj=mails(name=name, email=email, message= msg)
        mail_obj.save()
        messages.success(request, name.upper())
    return render(request,'index.html')