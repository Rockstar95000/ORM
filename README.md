# Ex02 Django ORM Web Application
## Date: 18/11/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![DIAGRAM](https://github.com/user-attachments/assets/8c505653-75d3-4c6a-b558-21c86d0cb294)
 

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
MODELS.PY
```
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
```

ADMIN.PY

```
from django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)

```

## OUTPUT

![Screenshot 2024-11-19 220843](https://github.com/user-attachments/assets/26d9f822-30cb-4f15-a76f-8a9bde23b7c2)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
