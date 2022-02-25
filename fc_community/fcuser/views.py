from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm


def home(request):
    user_id = request.session.get('user')

    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and firstname and lastname and useremail and password and re_password):
            res_data['error'] = 'You are missing some required fields!'
        elif password != re_password:
            res_data['error'] = 'The passwords you entered do not match!'
        else: 
            fcuser = Fcuser(
                username = username,
                firstname = firstname,
                lastname = lastname,
                useremail = useremail,
                password = make_password(password)
            )
            fcuser.save()
            return redirect('/fcuser/login')

        return render(request, 'register.html', res_data)