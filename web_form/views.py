from ast import For
from django.shortcuts import render
from .forms import Form

# Create your views here.
def home(request):
    form=Form()
    return render(request,'index.html',{'form':form})