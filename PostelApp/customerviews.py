from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from PostelApp.forms import ParcelForm, FeedbackForm, SurveyResponseForm
from PostelApp.models import ParcelTracking, Parcel, Feedback, Survey, Customers


@login_required
def track_parcel(request):
    parcels = ParcelTracking.objects.filter(user=request.user)
    return render(request, 'track_parcel.html', {'parcels': parcels})

@login_required
def add_parcel(request):
    u=request.user
    print(u)
    if request.method == 'POST':
        parcel_form = ParcelForm(request.POST, request.FILES)
        if parcel_form.is_valid():
            parcel = parcel_form.save(commit=False)
            parcel.user = u
            parcel.save()
            ParcelTracking.objects.create(user=request.user, parcel=parcel, status='In Transit')
            return redirect('view_parcel')
    else:
        parcel_form = ParcelForm()
    return render(request, 'add_parcel.html', {'parcel_form': parcel_form})

def view_parcel(request):
    data = Parcel.objects.filter(user=request.user)
    return render(request,'view_parcel.html',{'data':data})
@login_required
def parcel_detail(request, parcel_id):
    parcel = get_object_or_404(ParcelTracking, pk=parcel_id, user=request.user)
    return render(request, 'parcel_detail.html', {'parcel': parcel})

@login_required
def add_feedback(request):
    form = FeedbackForm()
    u = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('Feedback_view_user')
    return render(request, 'add_feedback.html', {'form': form})

def Feedback_view_user(request):
    f = Feedback.objects.filter(user=request.user)
    return render(request, 'Feedback_view_user.html', {'feedback': f})

def take_survey(request):
    user = request.user
    survey = Survey.objects.all()  # Assuming there's only one survey for simplicity
    form=SurveyResponseForm()
    if request.method == 'POST':
        form = SurveyResponseForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user=user
            data.save()
            return redirect('customerpage')
    return render(request, 'take_survey.html', {'form':form,'survey':survey})

def view_parcels_cus(request):
    u=Customers.objects.get(user=request.user)
    data = Parcel.objects.filter(user=u)
    return render(request,'view_parcels_cus.html',{'data':data})

def approve_parcel_cus(request,id):
    ow = Parcel.objects.get(id=id)
    ow.approval_status = 2
    ow.save()
    messages.info(request, 'approved')
    return redirect('view_parcels_cus')