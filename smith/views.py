from django.shortcuts import render, redirect,get_object_or_404
from smith.forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'smith/index.html')

class login(LoginView):
    template_name= 'smith/login.html'

class logout_user(LogoutView):
    template_name= 'smith/logout.html'



# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
                
#                 return redirect("index")
#             else:
#                 messages.error(request, "user does not exist or wrong password")

#     form = AuthenticationForm()
#     context = {'form' :form}

#     return render(request, 'smith/login.html', context)


def signup(request):
    form = SignupForm()
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'acounted created successfully')
            return redirect('login')
    context = {'form' :form}


    return render(request, 'smith/signup.html', context)