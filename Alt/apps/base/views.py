from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def main(request):
    context = {'data': 'some text'}
    return render(request, 'base/main.htm', context=context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        # noinspection PyBroadException
        try:
            login(request, user)
            return redirect('main')
        except BaseException:
            messages.error(request, "Email or Adress is incorrect")

    return render(request, 'base/login.htm')


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    
    form = forms.UserCreationForm

    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Your password is weak or Fields are filled incorrectly")

    context = {'form': form}
    return render(request, 'base/registration.htm', context)


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('main')
