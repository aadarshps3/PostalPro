from django.contrib import messages, auth
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from PostelApp.forms import UserReg, StaffForm, CustomerForm


# Create your views here.
def homepage(request):
    return render(request,'index.html')

def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('adminpage')
        elif user is not None and user.is_customer:
            if user.customers.approval_status==1:
                login(request,user)
                return redirect('customerpage')
            else:
                messages.info(request,"Your Are Not Approved To Login")
        elif user is not None and user.is_postalstaff:
            if user.Postalstaff.approval_status==1:
                login(request,user)
                return redirect('staffpage')
            else:
                messages.info(request,"Your Are Not Approved To Login")
        else:
            messages.info(request, "Not Registered User")
    return render(request,'login.html')

def staffregister(request):
    form1=UserReg()
    form2=StaffForm()
    if request.method=='POST':
        form1=UserReg(request.POST)
        form2=StaffForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save(commit=False)
            user.is_postalstaff=True
            user.save()
            po_staff=form2.save(commit=False)
            po_staff.user=user
            po_staff.save()
            messages.info(request,'Staff Registred succesfully')
            return redirect('loginpage')
    return render(request,'staffregister.html',{'form1':form1,'form2':form2})

def customerregister(request):
    form1 = UserReg()
    form2 = CustomerForm()
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = CustomerForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_customer = True
            user.save()
            customer = form2.save(commit=False)
            customer.user = user
            customer.save()
            messages.info(request, 'customer Registred succesfully')
            return redirect('loginpage')
    return render(request,'customerregister.html',{'form1':form1,'form2':form2})

def adminpage(request):
    return render(request,'adminpage.html')

def customerpage(request):
    return render(request,'customerpage.html')

def staffpage(request):
    return render(request,'staffpage.html')

def logout_view(request):
    logout(request)
    return redirect('loginpage')
