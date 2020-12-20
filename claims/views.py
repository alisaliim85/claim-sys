from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Claim
from .form import NewClaim

# Create your views here.

def index(request):
    allclaim = Claim.objects.all()
    context = {'allclaim' : allclaim}
    return render(request,'claims\index.html', context)


def details(request , id):
    claim_detail = Claim.objects.get(id=id)
    username = request.user.username

    context = {'claim_detail': claim_detail,
                'username': username
                }

    return render(request,'claims\detail.html', context)


def newclaim(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewClaim(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewClaim()

    return render(request, 'claims/add.html', {'form': form})