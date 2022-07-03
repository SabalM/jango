from django.shortcuts import render,redirect
from userapp.forms import RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form=RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('user_login')
    else:
        form = RegisterForm()
    context = {"form":form}
    return render(request, 'userapp/register.html', context)

def user_login(request):
    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('laptop-list')
            else:
                messages.error(request,"You are not registered")

        else:
            messages.error(request,"Invalid credentials")
    form = AuthenticationForm()
    return render(request, 'userapp/login.html',{'form':form})
