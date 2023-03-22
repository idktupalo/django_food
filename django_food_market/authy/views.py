from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm

# Create your views here.
def redirect_to_home(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']

    user = authenticate(request, first_name=first_name, last_name=last_name, password=password)
    if user is not None:
        login(request, user)
        return redirect('home_page')


def login(request):
    page = 'login'
    if request.method == "POST":
        redirect_to_home(request)
        
    context = {'page': page}    
    return render(request, 'authy/login_registry.html', context)


def registry(request):
    page = 'registry'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            redirect_to_home(request)
            
    context = {'form':form, 'page':page}
    return render(request, 'authy/login_registry.html', context)


def logout(request):
    logout(request)
    return redirect('login')