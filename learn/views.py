#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import AddForm

def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:
        form = AddForm()

    return render(request,'index.html',{'form':form})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def add2(request,a,b):
    c =int(a) + int(b)
    return HttpResponse(str(c))

def old_add_redirect(request,a,b):
    return HttpResponseRedirect(
        reverse('add2',args=(a,b)))
'''
def home(request):
    TutorialList = ['HTML','CSS','JQUEY','PYTHON']
    return render(request,'home.html',{'TutorialList':TutorialList})
'''

def home(request):
    List = map(str,range(100))
    return render(request,'home.html',{'List':List})



# Create your views here.
