from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="/login/")
def account(request):
    return render(request, "login.html")
    

def login(request):
    form = LoginForm()
    return render(request, "login.html", {'form': form})