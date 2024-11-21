from django.db import models

# Create your models here.
class Job(models.Model):
    title=models.CharField(null=True,blank=True,max_length=1000)
    company_name=models.CharField(null=True,blank=True,max_length=1000)
    monthly_salary=models.CharField(null=True,blank=True,max_length=100)
    description=models.TextField(null=True,blank=True)
    location=models.TextField(null=True,blank=True)
    no_of_opening=models.IntegerField(null=True,blank=True)
    application_starting_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    application_ending_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
