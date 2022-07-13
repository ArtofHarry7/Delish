from dataclasses import field
from traceback import print_tb
from typing import OrderedDict
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Delish1.models import MENU, ORDER, ORDER_MENU
from Delish1.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import json

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
    if user != None:
        user = request.user
    if request.method == "POST":
        name = request.POST.get('name')
        mode = request.POST.get('mode')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        items = request.POST.get('itemsJason')
        items = json.loads(items)
        price = json.loads(request.POST.get('priceJason'))
        order = ORDER.objects.create(
            user_name=name, 
            user=user, 
            payment_mode=mode, 
            price=price,
            phone=phone, 
            address1=address1, 
            address2=address2, 
            city=city, 
            state=state, 
            zip_code=zip_code
        )
        for key, value in items.items():
            menu_item = MENU.objects.get(name = value[1])
            order_menu = ORDER_MENU(order=order, menu_item=menu_item, quantity=value[0], name=value[1])
            order_menu.save()
        params['thank'] = True
        return render(request, 'checkout.html', params)
    params['thank'] = False
    return render(request, 'checkout.html', params)

def your_orders(request):
    user = request.user
    objs = ORDER.objects.all().filter(user=user)
    orders = []
    price = 0
    index = 0
    for obj in objs:
        order = ORDER_MENU.objects.all().filter(order=obj)
        price = 0
        for m in order:
            price += m.quantity * m.menu_item.price
        index += 1
        orders.append({'order' : order, 'date' : obj.date, 'price' : price, 'index' : index})
    orders.reverse()
    params = {'orders' : orders, 'account' : 'authenticated', 'user' : user}
    return render(request, 'your_orders.html', params)
