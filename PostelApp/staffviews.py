from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from PostelApp.forms import ParcelForm
from PostelApp.models import Customers, ParcelTracking, Parcel, Shift, Feedback


def view_cust(request):
    data = Customers.objects.filter(approval_status=1)
    return render(request,'view_cust.html',{'data':data})

def viewparcel(request):
    data = Parcel.objects.all()
    return render(request,'viewparcel.html',{'data':data})

def approve_parcel(request, id):
    student = Parcel.objects.get(user_id=id)
    student.approval_status = True
    student.save()
    messages.info(request, "Registered Successfully")
    return redirect('viewparcel')

def View_Time(request):
    u=request.user
    data = Shift.objects.all()
    return render(request,'View_Time.html',{'data':data})


def view_feedback(request):
    data = Feedback.objects.all()
    return render(request,'view_feedback.html',{'data':data})
@login_required
def reply_Feedback(request, id):
    f = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        f.reply = r
        f.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('view_feedback')
    return render(request, 'reply_Feedback.html', {'feedback': f})

def scan_parcels(request):
    form = ParcelForm()
    if request.method == 'POST':
        form = ParcelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_scanned')
    return render(request,'scan_parcels.html',{'form':form})

def view_scanned(request):
    data = Parcel.objects.all()
    return render(request,'view_scanned.html',{'data':data})
