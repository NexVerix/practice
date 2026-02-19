
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


""" #  PROTECTED PAGES
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'name': 'Aziz'})
 """
""" #  PROTECTED PAGES
def home(request):
    return render(request, 'home.html')
 """
# @login_required(login_url='login')
def home(request):
    username = request.user.username  # get logged-in user's username
    return render(request, 'home.html', {'name': username})
 
 
@login_required(login_url='login')
def service(request):
    return render(request, 'service.html', {'name': 'Aziz'})

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html', {'name': 'Aziz'})

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html', {'name': 'Aziz'})

@login_required(login_url='login')
def account(request):
    return render(request, 'account.html', {'name': 'Aziz'})


#  SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')


#  LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


#  LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')



from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required(login_url='login')
def settings_view(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get('email')
        user.save()
        messages.success(request, "Settings updated successfully")
        return redirect('settings')

    return render(request, 'settings.html')


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully")
            return redirect('account')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})


