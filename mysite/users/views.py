from django.shortcuts import render, redirect
from users.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
# ---------------------------------------------------
# users index
# ---------------------------------------------------
def index(request):

    context = {

    }

    return render(request,'users/home.html',context)
#register
# ---------------------------------------------------

def register(request):

    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(
               request,
               'Welcome, {} your account has been successfully created'. format(username) 
            )
        return redirect('food:index')
    
    else:
        form = RegisterForm(None)

        context = {
        'form':form
    }


    return render(request,'users/register.html',context)

#login view
#--------------------------------------------------------------------
def login_view(request):

    if request.method == 'POST':
        # using username
        #-------------------------------------------------------------------
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username , password=password)

        # using firstname
        #-------------------------------------------------------------------
        # firstname = request.POST['firstname']
        # password = request.POST['password']
        # userobj = User.objects.get(first_name=firstname)
        # username=userobj.username

        if user is not None:
            login(request,user)
            return redirect('food:index')

    context = {

    }

    return render(request,'users/login.html',context)

#Logout view
#---------------------------------------------------------------
def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect('food:index')

    return render(request, 'users/logout.html')

#profile page
#------------------------------------------------------------------

def ProfilePage(request):

    context = {

    }
    return render(request,'users/profile.html',context)

#profile view
#----------------------------------------------------------------
@login_required
def ProfilePage(request):
    context = {

    }
    return render(request, 'users/profile.html',context)


    
