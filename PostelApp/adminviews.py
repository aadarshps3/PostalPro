from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from PostelApp.forms import ParcelForm, StaffForm, shiftform, PO, Surveyadd
from PostelApp.models import PostalStaff, Customers, Parcel, Shift, PostOffice, SurveyResponse


def view_staffs(request):
    data=PostalStaff.objects.all()
    return render(request,'view_staff.html',{'data':data})

def view_customers(request):
    data=Customers.objects.all()
    return render(request,'view_customers.html',{'data':data})

def approve_staffs(request,id):
    staff = PostalStaff.objects.get(user_id=id)
    staff.approval_status = True
    staff.save()
    messages.info(request,'approved')
    return redirect('view_staffs')

def approve_user(request,id):
    cus = Customers.objects.get(user_id=id)
    cus.approval_status = True
    cus.save()
    messages.info(request, 'approved')
    return redirect('view_customers')

# def add_parcel(request):
#     if request.method == 'POST':
#         form = ParcelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('adminpage')  # Redirect to admin panel or any desired page
#     else:
#         form = ParcelForm()
#     return render(request, 'add_parcel.html', {'form': form})

def view_parcel_admin(request):
    data = Parcel.objects.all()
    return render(request,'view_parcel_admin.html',{'data':data})

@login_required
def manage_staff(request):
    staff = PostalStaff.objects.all()
    return render(request, 'manage_staff.html', {'staff': staff})

@login_required
def add_shift(request):
    if request.method == 'POST':
        form = shiftform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_shifts')
    else:
        form = shiftform()
    return render(request, 'add_shift.html', {'form': form})


@login_required
def manage_shifts(request):
    shifts = Shift.objects.all()
    return render(request, 'manage_shifts.html', {'shifts': shifts})

# Add views for adding, editing, and deleting shifts as needed

@login_required
def generate_schedule(request):
    # Implement scheduling algorithm to generate staff schedules
    pass

@login_required
def view_schedule(request):
    # Implement view to display generated staff schedules
    pass

def AddPO(request):
    form = PO()
    if request.method=='POST':
        form = PO(request.POST)
        if form.is_valid():
            form.save()
            return redirect('View_PO')
    return render(request,'AddPO.html',{'form':form})

def View_PO(request):
    data = PostOffice.objects.all()
    return render(request,'View_PO.html',{'data':data})

def AddSurvey(request):
    form = Surveyadd()
    if request.method == 'POST':
        form = Surveyadd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpage')
    return render(request,'AddSurvey.html',{'form':form})

def viewSurvey(request):
    data = SurveyResponse.objects.all()
    return render(request,'viewSurvey.html',{'data':data})

def view_scanned_parcels(request):
    data = Parcel.objects.all()
    return render(request,'view_scanned_parcels.html',{'data':data})

def approve_parcel_admin(request, id):
    student = Parcel.objects.get(user_id=id)
    student.approval_status = True
    student.save()
    messages.info(request, "Registered Successfully")
    return redirect('view_scanned_parcels')


