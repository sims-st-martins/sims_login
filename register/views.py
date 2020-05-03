from django.shortcuts import render,redirect
from .forms import Registerform
from .models import Register
from django.contrib import messages
def home(request):
    context= {'user_details':Register.objects.all()}
    return render(request,'base.html',context)


def register(request):
    if request.method == 'POST':
        form= Registerform(request.POST)
        if form.is_valid():
            form.save()
            #user_name = form.cleaned_date.get('user_name')
            #messages.success(request,f'Account created for {user_name}')
            return redirect('home/')


    else:
        form = Registerform()
    return render(request, 'register_form.html',{'form':form})

