from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MyUserCreationForm
from django.contrib import messages
from .models import User
# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def loginPageCustom(request):
    page = 'login'

    # after registrqation login
    if request.user.is_authenticated:
        return redirect('home')

    # user loging form
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist!!')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            dj_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exits')

    context = {'page': page}
    return render(request, 'login_register.html', context)


def registerUser(request):
    page = 'register'
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        messages.error(request, form.errors)
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occured during registration")
            # return redirect('registerUser')
    context = {'page': page, 'form': form}
    return render(request, 'login_register.html', context)


def updateUser(request):
    return HttpResponse('updateUser')


def logoutUser(request):
    logout(request)
    return redirect('home')
