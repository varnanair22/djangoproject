from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Currency_Details

from .models import Users, Currency_Details


def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def curr_conv(request):
    currencies = Currency_Details.objects.all()
    return render(request, 'currency.html', {'currencies':currencies})

def get_curr_rate(request):
    if request.method =="POST":
        curr1 = request.POST['curr1']
        curr2 = request.POST['curr2']
        curr_vals = Currency_Details.objects.all().filter(curr1=curr1, curr2=curr2)
        currencies = Currency_Details.objects.all()
        return render(request, 'currency.html', {'curr_vals':curr_vals,'currencies':currencies})

def curr_update(request):
    if request.method =="POST":
        curr1 = request.POST['curr1']
        curr2 = request.POST['curr2']
        curr_conv = float(request.POST['up_conv'])
        curr_vals = Currency_Details.objects.all().filter(curr1=curr1, curr2=curr2)
        currencies = Currency_Details.objects.all()
        curr_instance = Currency_Details.objects.filter(curr1=curr1, curr2=curr2).update(conversion_rate=curr_conv)
        messages.info(request, "Successfully Updated!!")
        return render(request, 'currency.html', {'curr_vals':curr_vals,'currencies':currencies})

def auth(request):
    name = request.POST['name']
    pswd = request.POST['pswd']
    cnf_pswd = request.POST['cnf_pswd']

    if pswd == cnf_pswd:
        if Users.objects.filter(name=name).exists():
            messages.info(request, "Username already exists!!!")
            return redirect('signup')
        else:
            try:
                validate_email(name)
            except ValidationError as e:
                messages.info(request, "Enter valid Email Address!!!")
                return redirect('signup')

            user_instance = Users.objects.create(name=name, pswd=pswd, type="")
            user_instance.save();
            messages.info(request, "Congratulations!!!Your account has been created.")
            return redirect('login')
    else:
        messages.info(request, "Passwords not matching!!!")
        return redirect('signup')

def logging(request):
    if request.GET.get('signin') == 'signin':
        return redirect('login')
    else:
        name = request.POST['uname']
        pswd = request.POST['psw']

        try:
            p = Users.objects.get(name=name, pswd=pswd)
            if p is not None:

                return redirect('curr_conv')
        except Users.DoesNotExist:
            messages.info(request, "Incorrect Username or Password!!!")
            return redirect('login')
