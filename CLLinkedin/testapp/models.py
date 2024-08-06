from django.db import models
from django.contrib.auth.models import User

# Choices the User Can make
Ethnicities = (
    ("AI", "American Indian or Alask Native"), ("A", "Asian"),
    ("B", "Black or African American"), ("PI", "Native Hawaiian or Pacific Islander"),
    ("W", "White"), ("NA", "Prefer Not to Answer")
)

Gender = (
    ("M", "Male"), ("W", "Women"), ("TM", "Trans Male"), ("TW", "Trans Women"),
    ("NC", "NonConforming"), ("O", "Other"), ("NA", "Prefer Not to Answer")
)

NonCitizen = (
    ("1", "Permanent Resident (Green Card)"), ("2", "F-1 Visa"), ("3", "J-1 Visa"),
    ("4", "H-1B Visa"), ("4", "DACA"), ("5", "Asylum Seeker"), ("0", "Other Noncitizen Designation")
)

SexO = (
    ("H", "Heterosexual"), ("G", "Homosexual"), ("B", "Bisexual"), ("O", "Other"),
    ("NA", "Prefer Not to Answer")
)

Income = (
    ("1", "0.00 - 10,000.00"), ("2", "10,000.00 - 25,000.00"), ("3", "25,000.00 - 50,000.00"),
    ("4", "50,000.00 - 100,000.00"), ("5", "Over 100,000.00")
)

statuses = (("G", "Graduated"), ("W", "Withdrawn"), ("C", "Current"))

current = (("f", "freshman"), ("s", "sophomore"), ("j", "junior"), ("sn", "senior"))

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    fname = models.CharField(max_length=50, null=True, blank=True)  # First Name
    lname = models.CharField(max_length=50, null=True, blank=True)  # Last Name
    phone = models.CharField(max_length=11, null=True, blank=True)  # Phone Number
    email = models.EmailField(null=True, blank=True)  # Email
    age = models.PositiveIntegerField(null=True, blank=True)  # Age
    dob = models.DateField(null=True, blank=True)  # Date of Birth
    hispanic = models.BooleanField(null=True, blank=True)  # Y/N Hispanic
    ethnicity = models.CharField(max_length=2, choices=Ethnicities, default='NA', null=True, blank=True)  # Ethnicity/Race Choice
    gender = models.CharField(max_length=2, choices=Gender, default='NA', null=True, blank=True)  # Gender Choice
    orientation = models.CharField(max_length=2, choices=SexO, default='NA', null=True, blank=True)  # Sexual Orientation Choice
    us_citizenship = models.BooleanField(null=True, blank=True)  # Y/N US Citizenship
    non_citizen = models.CharField(max_length=1, choices=NonCitizen, default='0', null=True, blank=True)
    gross_income = models.CharField(max_length=1, choices=Income, default='1', null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)

    def is_complete(self):
        return all([
            self.fname,
            self.lname,
            self.phone,
            self.email,
            self.dob,
            self.ethnicity != 'NA',
            self.gender != 'NA',
            self.orientation != 'NA',
            self.non_citizen != '0',
            self.gross_income != '1',
        ])

# Academic Tables
class Degree(models.Model):
    degree_name = models.CharField(max_length=100)

class Program(models.Model):
    program_name = models.CharField(max_length=50)
    degree = models.ForeignKey(Degree, on_delete=models.SET_DEFAULT, default=1)

class Institution(models.Model):
    name = models.CharField(max_length=100, default="Unknown Institution")
    ranking = models.IntegerField(default=0)

class AcademicRecord(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=1, choices=statuses)
    current_year = models.CharField(max_length=2, choices=current)
    gpa = models.FloatField()

# Extracirrucular Tables
class Orgtype(models.Model):
    description = models.CharField(max_length=255)

class JPosition(models.Model): # J for Job Positions
    description = models.CharField(max_length=255)

class SPosition(models.Model): # S for Student Positions
    description = models.CharField(max_length=255)

class Extracurricular(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=100)
    org_type = models.ForeignKey(Orgtype,on_delete=models.CASCADE)
    position = models.ForeignKey(SPosition, on_delete=models.CASCADE)

class JobInternship(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=100)
    position = models.ForeignKey(JPosition, on_delete=models.CASCADE)
    internship = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)