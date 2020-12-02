from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login),
    path('login/', views.login, name= "login"),
    path('signup', views.signup, name = "signup"),
    path('signup/auth', views.auth, name="auth"),
    path('auth', views.auth, name="auth"),
    path('login/logging', views.logging, name="logging"),
    path('logging', views.logging, name="logging"),
    path('currency_conv', views.curr_conv, name="curr_conv"),
    path('curr_update', views.curr_update, name="curr_update"),
    path('get_curr_rate', views.get_curr_rate, name="get_curr_rate"),
    path('login/signup', views.signup, name="signup"),
    path('login/auth', views.auth, name="auth"),

]
