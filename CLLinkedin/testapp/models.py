from django.db import models

# Choices the User Can make
Ethnicities  = (("AI","American Indian or Alask Native"),("A","Asian"),
                ("B","Black or African American"),("PI","Native Hawaiian or Pacific Islander"),
                ("W","White"),("NA","Prefer Not to Answer"))

Gender = (("M","Male"),("W","Women"),("TM","Trans Male"),("TW","Trans Women"),("NC","NonConforming"),
          ("O","Other"),("NA","Prefer Not to Answer"))

SexO = (("H","Heterosexual"),("G","Homosexual"),("B","Bisexual"),("O","Other"),("NA","Prefer Not to Answer"))

# Python SQL Table Implementation
class Employee(models.Model):
    fname = models.CharField(max_length = 50) # First Name
    lname = models.CharField(max_length = 50) # Last Name
    phone = models.CharField(max_length=11) # Phone Number (Check for valid Number)
    email = models.EmailField() # Email 
    age = models.PositiveIntegerField(max_length=3) # Age 0-999
    dob = models.DateField() # Date of Birth 
    hispanic = models.BooleanField() # Y/N Hispanic
    ethnicity = models.CharField(max_length=50, choices=Ethnicities,default='NA') # Ethnicity/Race Choice
    gender = models.CharField(max_length=50, choices=Gender,default='NA') # Gender Choice
    orientation = models.CharField(max_length=50, choices=SexO,default='NA') # Sexual Orientation Choice
    citizenship = None # US Citizenship Choice - Incomplete
    GrossIncome = None # Gross Income Ranges Choice - Incomplete
    createdon = models.models.DateTimeField(auto_now=True)



    
# Academic Tables 

class Degree(models.Model):
    pass

class Program(models.Model):
    pass

class Institution(models.Model):
    pass


# Extracirrucular Tables




# Job/Internship Tables