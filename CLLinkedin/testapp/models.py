from django.db import models
# Create your models here.

class Employee(models.Model):
    fname = models.CharField(max_length = 50) # First Name
    lname = models.CharField(max_length = 50) # Last Name
    hs_diploma = models.BooleanField() # High School Diploma
    post_hs = models.BooleanField() # Post Highschool Education
    as_degree = models.BooleanField() # Has AS degree
    ba_degree = models.BooleanField() # Has BA degree
    ma_degree = models.BooleanField() # Has MA degree
    phd_degree = models.BooleanField() # Has PHD degree

    
class Employer(models.Model):
    pass

class Certification(models.Model):
    pass

class Interst(models.Model):
    pass