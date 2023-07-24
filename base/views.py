import re
from django.shortcuts import render,redirect
from .models import User,Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def login_page(request):
    page='login'
    if request.method=='POST':
        user=authenticate(email=request.POST['email'],password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('home')

    context={'page':page}
    return render(request,'login_register.html',context)

def logout_user(request):
    logout(request)
    return redirect('login')


def register_page(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            return redirect('home')
    page='register'
    context={'page':page,'form':form}
    return render(request,'login_register.html',context)

# Create your views here.

def home_page(request):
    users=User.objects.filter(event_paricipant=True)
    events=Event.objects.all()
    context={'users':users,'events':events}
    return render(request,'home.html',context)

def user_page(request,pk):
    user=User.objects.get(id=pk)
    context={'user':user}
    return render(request,'profile.html',context)

@login_required(login_url='login')
def account_page(request):
    user=request.user
    context={'user':user}
    return render(request,'account.html',context)

def event_page(request,pk):
    event=Event.objects.get(id=pk)
    registered=request.user.events.filter(id=event.id).exists()
    context={'event':event,'registered':registered}
    return render(request,'event.html',context)

@login_required()
def registration_confirmation(request,pk):
    event=Event.objects.get(id=pk)
    if request.method=="POST":
        event.participants.add(request.user)
        return redirect('event', pk=event.id)
    
    return render(request, 'event_confirmation.html', {'event':event})