from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileM(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    Phone=models.CharField(max_length=100,null=True,blank=True)
    Present_Address=models.CharField(max_length=255,null=True,blank=True)
    Permanant_Address=models.CharField(max_length=255,null=True,blank=True)
    Image=models.ImageField(upload_to='User',null=True,blank=True)
    objects=models.Manager()

    def images(self):
        try:
            urls=self.Image.url
        except:
            urls=''
        return urls

class ItemEntryM(models.Model):
    Itemname=models.CharField(max_length=255,null=True,blank=True)
    Unit=models.CharField(max_length=255,null=True,blank=True)
    objects=models.Manager()

class SupplierInfoM(models.Model):
    Suppliername=models.CharField(max_length=255,null=True,blank=True)
    Address=models.TextField(max_length=2000,null=True,blank=True)
    Phone=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    objects=models.Manager()
    def __str__(self):
        return self.Suppliername

class EmployeesInformationM(models.Model):
    Name=models.CharField(max_length=255,null=True,blank=True)
    Designation=models.CharField(max_length=255,null=True,blank=True)
    Depertment=models.CharField(max_length=255,null=True,blank=True)
    Employees_id=models.CharField(max_length=255,null=True,blank=True)
    Present_address=models.TextField(max_length=1500,null=True,blank=True)
    Permanent_address=models.TextField(max_length=1500,null=True,blank=True)
    Date_of_Birth=models.DateField(null=True,blank=True)
    Phone=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    objects = models.Manager()

class PurchageExtendM(models.Model):
    Pdate = models.DateField(null=True, blank=True)
    Invoice_no = models.CharField(max_length=100, null=True, blank=True)
    Supplier_name = models.ForeignKey(SupplierInfoM, on_delete=models.CASCADE, null=True, blank=True)
    Vat = models.IntegerField(null=True, blank=True)
    Less = models.IntegerField(null=True, blank=True)
    objects=models.Manager()

class PurchageInfoM(models.Model):
    pex=models.ForeignKey(PurchageExtendM,on_delete=models.CASCADE,null=True,blank=True)
    Item_name=models.CharField(max_length=255,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Rate=models.CharField(max_length=255,   null=True,blank=True)
    Invoice_nos = models.CharField(max_length=100, null=True, blank=True)
    objects=models.Manager()

class IssueExtendM(models.Model):
    Pdate = models.DateField(null=True, blank=True)
    Invoice_no = models.CharField(max_length=100, null=True, blank=True)
    issue_name = models.ForeignKey(EmployeesInformationM, on_delete=models.CASCADE, null=True, blank=True)

    objects=models.Manager()

class issueInfoM(models.Model):
    pex=models.ForeignKey(IssueExtendM,on_delete=models.CASCADE,null=True,blank=True)
    Item_name=models.CharField(max_length=255,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Invoice_nos = models.CharField(max_length=100, null=True, blank=True)
    objects=models.Manager()



