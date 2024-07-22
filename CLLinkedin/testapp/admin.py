from django.contrib import admin
from .models import Employee, Degree, Program, Institution, AcademicRecord, JPosition, Extracurricular, JobInternship, SPosition, Orgtype

#Register User
admin.site.register(Employee)

#Employee Attributes
admin.site.register(Degree)
admin.site.register(Program)
admin.site.register(Institution)
admin.site.register(AcademicRecord)
admin.site.register(JPosition)
admin.site.register(SPosition)
admin.site.register(Orgtype)
admin.site.register(Extracurricular)
admin.site.register(JobInternship)

#Employer Attributes