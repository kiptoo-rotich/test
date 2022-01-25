from ast import For
from django.shortcuts import redirect, render
from .forms import Form
from .models import User

# Create your views here.
def home(request):
    data=User.objects.all()
    if request.method=="POST":
        form=Form(request.POST,request.FILES)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=request.user
            data.save()
            return redirect('home')
    else:
        form=Form()
    return render(request,'index.html',{'form':form,'data':data})