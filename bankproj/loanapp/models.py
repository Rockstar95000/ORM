from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
    Loan_id=models.IntegerField(primary_key=True)
    Cust_id=models.IntegerField(max_length=50)
    Cust_name=models.CharField(max_length=100)
    Loan_amt=models.IntegerField()
    Mail_id=models.EmailField()
 
class BankloanAdmin(admin.ModelAdmin):
    list_display=('Loan_id','Cust_id','Cust_name','Loan_amt','Mail_id')