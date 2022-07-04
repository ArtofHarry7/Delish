from django.contrib import admin
from django.urls import path
from Delish1 import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    # path('signin/', views.signin, name='signin'),
    # path('signup/', views.signup, name='signup'),
    path('special/', views.special, name='special'),
    path('menu/', views.menu, name='menu'),
    path('review/', views.review, name='review'),
    # path('order/', views.order, name='order'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.registerPage , name='register'),
    path('login/', views.loginPage , name='login'),
    path('logout/', views.logoutUser , name='logout'),
]