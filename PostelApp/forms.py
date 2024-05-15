from django import forms
from django.contrib.auth.forms import UserCreationForm

from PostelApp.models import User, PostalStaff, Customers, Parcel, Shift, PostOffice, Feedback, SurveyResponse, Survey


class TimeInput(forms.TimeInput):
    input_type = 'time'
class DateInput(forms.DateInput):
    input_type = 'date'

class UserReg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='PassWord',widget=forms.PasswordInput)
    password2 = forms.CharField(label='PassWord',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','password1','password2')

class StaffForm(forms.ModelForm):
    class Meta:
        model=PostalStaff
        exclude=('user','approval_status')

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customers
        exclude=('user','approval_status')

class ParcelForm(forms.ModelForm):
    Expected_delivery_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Parcel
        fields = ['user','tracking_number', 'description', 'weight', 'Images', 'Live_Location','Expected_delivery_date','POSTOFFICE']

class shiftform(forms.ModelForm):
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)
    class Meta:
        model=Shift
        fields = '__all__'

class PO(forms.ModelForm):
    class Meta:
        model = PostOffice
        fields = '__all__'

class FeedbackForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Feedback
        fields = ('subject', 'Enquiry', 'date')

class SurveyResponseForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['response']


class Surveyadd(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'

class UpdateExpectedDeliveryDateForm(forms.ModelForm):
    Expected_delivery_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Parcel
        fields = ['Expected_delivery_date']