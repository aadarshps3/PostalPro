from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_postalstaff=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)

class PostalStaff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="Postalstaff")
    Name=models.CharField(max_length=100)
    Designation=models.CharField(max_length=100)
    Emp_ID=models.CharField(max_length=100)
    Photo=models.ImageField(upload_to='Staff')
    Email_Id=models.EmailField()
    Phone_No=models.CharField(max_length=10)
    approval_status = models.BooleanField(default=0)

    def __str__(self):
        return self.Name

class Customers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='customers')
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=255)
    Phone_No=models.CharField(max_length=10)
    Email=models.EmailField()
    Photo=models.ImageField(upload_to='customer')
    Aadhar_Proof=models.ImageField(upload_to='Aadhar')
    approval_status = models.BooleanField(default=0)

    def __str__(self):
        return self.Name

class PostOffice(models.Model):
    Name = models.CharField(max_length=100)
    PIN_code = models.CharField(max_length=6)
    Address = models.CharField(max_length=255)

    def __str__(self):
        return self.Name

class Parcel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    Images = models.ImageField(upload_to='parcel')
    Live_Location = models.CharField(max_length=100)
    Expected_delivery_date = models.DateField()
    Your_POSTOFFICE = models.ForeignKey(PostOffice,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='In Transit')
    created_at = models.DateTimeField(auto_now_add=True)
    approval_status = models.BooleanField(default=0)


    def __str__(self):
        return f"Parcel #{self.tracking_number}"

class ParcelTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered')])
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tracking for Parcel #{self.parcel.tracking_number}"

class Delivery(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    # Add other fields as needed

class PostalPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for postal preferences (e.g., notification settings, delivery preferences, etc.)

class Shift(models.Model):
    name = models.ForeignKey(PostalStaff,on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Schedule(models.Model):
    staff = models.ForeignKey(PostalStaff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    date = models.DateField()

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    Enquiry = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)

class Survey(models.Model):
    question = models.CharField(max_length=255)

class SurveyResponse(models.Model):
    response = models.CharField(max_length=255)