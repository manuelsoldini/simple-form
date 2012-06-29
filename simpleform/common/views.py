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

def auth(request):
    request.session['is_auth'] = request.POST['pass']
    request.session['check'] = request.POST['pass']
    request.session.set_expiry(30*60)

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
            return redirect('/success')
    else:
        if is_auth(request.session):
            return redirect('/success')
        params = {}
        params['username'] = 'user' + str(randrange(1000, 9999))
        params['password'] = str(hex(hash(params['username'])))[2:]
        return render(request, 'login.html', params)
    return Http404

def success(request):
    if request.method == "POST":
        if is_auth(request.session):
            return redirect('/fake')
    else:
        if is_auth(request.session):
            return render(request, 'success.html', {})
        return redirect('/login')
    return Http404

def fake(request):
    if is_auth(request.session):
        return render(request, "fakeException.html", {})
    return redirect('/login')

def becomeAJedi(request):
    if request.method == "GET":
        if is_auth(request.session):
            return render(request, 'becomeAJedi.html', {"form": MyForm()})
    elif request.method == "POST":
        if is_auth(request.session):
            form = MyForm(request.POST, request.FILES)
            if form.is_valid():
                f = request.FILES.get('resume', None)
                if f:
                    if f.size/1024.0/1024 > 2.5:
                        return render(request, "becomeAJedi.html", 
                                {"file_info": "File Size > 2.5Mb, please \
                                               upload a smaller file",
                                 "form": form})    
                form.save()
                #send_mail(form)
                return redirect('/farewell')
            else:
                return render(request, 'becomeAJedi.html', {"form": form})
    raise Http404

def farewell(request):
    return render(request, 'farewell.html', {})


