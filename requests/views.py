from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import ServiceRequest, Customer
from .forms import ServiceRequestForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import SignUpForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('requests:account_info')  # Redirect to account_info after successful submission
    else:
        form = ServiceRequestForm()
    return render(request, 'requests/submit_request.html', {'form': form})

@login_required
def request_status(request):
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'requests/request_status.html', {'requests': requests})

@login_required
def account_info(request):
    customer = request.user.customer
    requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'requests/account_info.html', {'customer': customer, 'requests': requests})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            Customer.objects.create(user=user, address=address, phone=phone)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('requests:signup')
