from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as logouts
from . models import SignUp, Gallery
from . forms import SignUpForm, LoginForm, UpdateForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            age = form.cleaned_data['Age']
            photo = form.cleaned_data['Photo']
            password = form.cleaned_data['Password']
            confirmPass = form.cleaned_data['ConfirmPassword']
            user = SignUp.objects.filter(Email=email).exists()
            if user:
                messages.warning(request, "Email already exist!")
                return redirect('/register/')
            elif password != confirmPass:
                messages.warning(request, "Password mismatch!")
                return redirect('/register/')
            else:
                tab = SignUp(Name=name, Email=email, Age=age, Photo=photo, Password=password)
                tab.save()
                return redirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password =  form.cleaned_data['Password']
            user = SignUp.objects.get(Email=email)
            if not user:
                messages.warning(request, 'Email does not exist!')
                return redirect('/login/')
            elif user.Password != password:
                messages.warning(request, 'Incorrect password!')
                return redirect('/login/')
            else:
                messages.success(request, 'Login Successful')
                return redirect('/home/%s' % user.id)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def home(request, id):
    user = SignUp.objects.get(id=id)
    return render(request, 'home.html', {'user':user})

def update(request, id):
    user = SignUp.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST or None, request.FILES or None, instance=user)
        if form.is_valid():
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            age = form.cleaned_data['Age']
            photo = form.cleaned_data['Photo']
            form.save()
            messages.success(request, 'Profile updated')
            return redirect('/home/%s' % user.id)
    else:
        form = UpdateForm(instance=user)
    return render(request, 'update.html', {'user':user, 'form':form})

def logout(request):
    logouts(request)
    messages.success(request, 'Logout Successful')
    return redirect('/')

def galleryPage(request):
    data = Gallery.objects.all()
    return render(request, 'gallery.html', {'data':data})

def details(request, id):
    data = Gallery.objects.get(id=id)
    return render(request, 'details.html', {'data':data})
    
