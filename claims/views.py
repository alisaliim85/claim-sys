from django.shortcuts import render
from django.http import HttpResponse
from .models import Claim

# Create your views here.

def index(request):
    allclaim = Claim.objects.all()
    context = {'allclaim' : allclaim}
    return render(request,'claims\index.html', context)


def details(request , id):
    claim_detail = Claim.objects.get(id=id)
    context = {'claim_detail': claim_detail}

    return render(request,'claims\detail.html', context)


