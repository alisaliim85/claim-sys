from django.shortcuts import render
from django.http import HttpResponse
from .models import Claim

# Create your views here.

def index(request):
    allclaim = Claim.objects.all()
    context = {'allclaim' : allclaim}

    
    return render(request,'claims\index.html', context)
