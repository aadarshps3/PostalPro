import csv
from datetime import datetime, timedelta, date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

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


class MonthlyReportView(View):
    def get(self, request, *args, **kwargs):
        # Calculate start and end dates for the current month
        today = date.today()
        start_date = datetime(today.year, today.month, 1)
        end_date = datetime(today.year, today.month + 1, 1) - timedelta(days=1)

        # Filter parcels created within the current month
        parcels = Parcel.objects.filter(created_at__date__range=[start_date, end_date])

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="monthly_report.csv"'

        writer = csv.writer(response)
        writer.writerow(
            ['Tracking Number', 'Description', 'Weight', 'Live Location', 'Expected Delivery Date', 'Status',
             'Created At'])

        for parcel in parcels:
            writer.writerow([
                parcel.tracking_number,
                parcel.description,
                parcel.weight,
                parcel.Live_Location,
                parcel.Expected_delivery_date,
                parcel.status,
                parcel.created_at,
            ])

        return response