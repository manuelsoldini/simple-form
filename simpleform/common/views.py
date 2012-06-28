from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from common.models import SimpleForm
from random import randrange

from django.forms import ModelForm
from bootstrap.forms import BootstrapMixin

class MyForm(BootstrapMixin, ModelForm):
    class Meta:
        model = SimpleForm

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def auth(request):
    request.session['is_auth'] = request.POST['pass']
    request.session['check'] = request.POST['pass']

def is_auth(session):
    try:
        return session['is_auth'] == session['check']
    except:
        return False

def login(request):
    if request.method == "POST":
        passwd = str(hex(hash(request.POST['user'])))[2:]
        if passwd == request.POST['pass']:
            auth(request)
            return redirect('/challenge')
    else:
        if is_auth(request.session):
            redirect('/challenge')
        params = {}
        params['username'] = 'user' + str(randrange(1000, 9999))
        params['password'] = str(hex(hash(params['username'])))[2:]
        return render(request, 'login.html', params)
    return Http404

def challenge(request):
    if request.method == "GET":
        if is_auth(request.session):
            return render(request, 'challenge.html', {"form": MyForm()})
    elif request.method == "POST":
        if is_auth(request.session):
            form = MyForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                handle_uploaded_file(request.FILES['resume'])
                return redirect('/farewell')
            else:
                return render(request, 'challenge.html', {"form": form})
    raise Http404

def farewell(request):
    return render(request, 'farewell.html', {})


