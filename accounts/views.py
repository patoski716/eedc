from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def search(request):
    posts = Customer.objects.order_by('-date_added')
    if 'c_phone' in request.GET:
        c_phone = request.GET['c_phone']
        if c_phone:
            query = Customer.objects.filter(c_phone__iexact=c_phone)    
    context={'query':query,'posts':posts}
    return render(request,'search.html',context)

def check(request):
    return render(request,'check.html')

def payment(request):
    posts = Customer.objects.all()
    if request.method == 'POST':    
        amount = request.POST['amount']
        c_phone = request.POST['c_phone']
        contact = Payment(amount=amount,c_phone=c_phone)
        contact.save()
        return render(request,"sent.html")
    context={'posts':posts}
    return render(request,'payment.html',context)

def sent(request):
    return render(request,'sent.html')

def success(request):
    posts = Payment.objects.all()
    context={'posts':posts}
    return render(request,'success.html',context)