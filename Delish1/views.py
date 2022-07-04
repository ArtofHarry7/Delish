from dataclasses import field
from typing import OrderedDict
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Delish1.models import MENU
from Delish1.forms import CreateUserForm
from django.contrib import messages
import mysql.connector
from operator import itemgetter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# account = 'notSigned'
# user = 'None'

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, 'Hello ' + name + ', you have successfuly signed In. Now you can Sign In')
            return redirect('login')

    params = {'form' : form}
    return render(request, 'register.html', params)
    
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            # return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def index(request):
    user = None
    account = 'unauthenticated'
    if request.user.is_authenticated:
        account = 'authenticated'
        user = request.user.username
    params = {'account' : account, 'user' : user}
    return render(request, 'index.html', params)

def about(request):
    user = None
    account = 'unauthenticated'
    if request.user.is_authenticated:
        account = 'authenticated'
        user = request.user.username
    params = {'account' : account, 'user' : user}
    return render(request, 'about.html', params)

# def menu(request):
#     user = None
#     account = 'unauthenticated'
#     if request.user.is_authenticated:
#         account = 'authenticated'
#         user = request.user.username
#     params = {'account' : account, 'user' : user}
#     return render(request, 'menu.html', params)

def special(request):
    user = None
    account = 'unauthenticated'
    if request.user.is_authenticated:
        account = 'authenticated'
        user = request.user.username
    params = {'account' : account, 'user' : user}
    return render(request, 'special.html', params)

def menu(request):
    user = None
    account = 'unauthenticated'
    if request.user.is_authenticated:
        account = 'authenticated'
        user = request.user.username
    params = {'account' : account, 'user' : user}
    objs = MENU.objects.all()
    params = {'pop_menu': objs, 'account' : account, 'user' : user}
    return render(request, 'menu.html', params)

def review(request):
    user = None
    account = 'unauthenticated'
    if request.user.is_authenticated:
        account = 'authenticated'
        user = request.user.username
    params = {'account' : account, 'user' : user}
    return render(request, 'review.html', params)

def contactus(request):
    # if request.method == "POST":
    #     phone = request.POST.get('phone')
    #     age = request.POST.get('age')
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     query = request.POST.get('query')
    #     Quer = contactus(phone = phone, age = age, cust_name = name, email = email, query = query, date = datetime.today())
    #     Quer.save()
    #     messages.success(request, 'We have successfuly got your message')
    user = None
    account = 'unauthenticated'
    if request.user.is_authenticated:
        account = 'authenticated'
        user = request.user.username
    params = {'account' : account, 'user' : user}
    return render(request, 'contactus.html', params)

def checkout(request):
    user = None
    account = 'unauthenticated'
    if request.user.is_authenticated:
        account = 'authenticated'
        user = request.user.username
    else:
        return redirect('login')
    params = {'account' : account, 'user' : user}
    if request.method == "POST":
        cust = customer.objects.get(id=id)
        cust_name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = cust.email
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        order_str = request.POST.get('itemsJason')
        bookin = orders(order_str = order_str, cust_name = cust_name, phone = phone, email = email, address = address, city = city, state = state, zip_code = zip_code)
        bookin.save()
        items = request.POST.get('itemsJason')
        print('__________________________________________________________________________')
        # items = dict(items)
        ord = items[1:-1].split(", ")
        print(ord)
        print(ord[0])

        
        thank = True
        id = bookin.order_id
        # messages.success(request, 'We have successfuly got your order, We are just coming')
        return render(request, 'checkout.html', {'thank' : thank, 'id' : id})

    return render(request, 'checkout.html', params)
