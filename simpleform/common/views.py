from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from common.models import SimpleForm
from random import randrange

from django.forms import ModelForm

class MyForm(ModelForm):
    class Meta:
        model = SimpleForm

def login(request):
    params = {}
    params['username'] = 'user' + str(randrange(1000, 9999))
    params['password'] = str(hex(hash(params['username'])))[2:]
    return render(request, 'login.html', params)

def challenge(request):
    if request.method == "POST":
        passwd = str(hex(hash(request.POST['user'])))[2:]
        if passwd == request.POST['pass']:
            return render(request, 'challenge.html', {"form": MyForm().as_table()})
        else:
            raise Http404
    raise Http404

def submit(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/farewell')
        else:
            return render(request, 'challenge.html', {"form": form})
    return redirect('/login')

def farewell(request):
    return render(request, 'farewell.html', {})
