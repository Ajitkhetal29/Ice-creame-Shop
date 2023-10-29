from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from Users.forms import RegistrationForm	
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Register View
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data.get('username')
            messages.success(request , 'Welcome {}, Your account is created'.format(username))
            form.save()
            return redirect('Icecreame:index')
    else:
        form=RegistrationForm()
    return render (request,'users/register.html',{'form':form})


#  Login View
def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is None:
            messages.success(request,'Invalid login , Please try again')
            return redirect('login_view')
        elif user.is_superuser:
            messages.success(request,'{}, is a superuser and has been succesfully logged in'.format(username))
            login(request,user)
            return redirect('Icecreame:index')
        elif user.is_authenticated:
            messages.success(request , 'Welcome {}... Logged in succesfully'.format(username))
            login(request,user)
            return redirect('Icecreame:index')
    return render (request,'users/login.html')

    


# Logout vIew 
def logout_view(request):
    logout(request)
    return redirect('login_view')


#  Profile page view
@login_required
def profilepage(request):
    return render (request,'users/profile.html')



   