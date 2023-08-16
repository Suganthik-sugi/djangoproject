from django.db import models

# Create your models here.
class Details(models.Model):
    fname=models.CharField(max_length=20,null=False,blank=False,verbose_name="First Name")
    lname=models.CharField(max_length=20,null=False,blank=False,verbose_name="Last Name")
    username=models.CharField(max_length=20,null=False,blank=False,unique=True,verbose_name="User Name")
    email=models.EmailField(max_length=50,null=False,blank=False,unique=True,verbose_name="Email id")
    phno=models.CharField(max_length=20,null=False,blank=False,unique=True,verbose_name="Phone number")
    address=models.CharField(max_length=20,null=False,blank=False,verbose_name="Address")
    gstin=models.CharField(max_length=20,null=False,blank=False,unique=True,verbose_name="gstin")
    officename=models.CharField(max_length=20,null=False,blank=False,verbose_name="Office Name")
    gmname=models.CharField(max_length=20,null=False,blank=False,verbose_name="GM Name")
    officeaddress=models.CharField(max_length=20,null=False,blank=False,unique=True,verbose_name="Office address")
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    created_by=models.IntegerField(null=True,blank=True)
    modified_by=models.IntegerField(null=True)
    is_active=models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)
    # item_deleted=models.BooleanField(default=False)

class Employee(models.Model):
    empid = models.ForeignKey(Details, on_delete=models.CASCADE)
    designation=models.CharField(max_length=20,null=False,blank=False,verbose_name="designation")
    bankname=models.CharField(max_length=20,null=False,blank=False,verbose_name="Bank Name")
    pfnumber=models.CharField(max_length=20,null=False,blank=False,verbose_name="PF Number")
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    created_by=models.IntegerField(null=True,blank=True)
    modified_by=models.IntegerField(null=True)
    is_active=models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)

class image(models.Model):
    
     image = models.ImageField(upload_to='firstapp/images/')
     created_at=models.DateTimeField(auto_now_add=True)
     modified_at=models.DateTimeField(auto_now=True)
     created_by=models.IntegerField(null=True,blank=True)
     modified_by=models.IntegerField(null=True)
     is_active=models.BooleanField(default=True)
     is_deleted=models.BooleanField(default=False)