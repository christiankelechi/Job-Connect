#!/usr/bin/env python3fr
from django.urls import path
import job.views as job

urlpatterns = [
    path("", job.landing_page, name="landingpage"),
    path("about-us", job.about_us, name="aboutus"),
    path('contact_us', job.contact_us, name="contactus"),
    path("admin_login", job.admin_login, name="adminlogin"),
    path("admin_signup", job.admin_signup, name="adminsignup"),
    path('student_login', job.student_login, name="studentlogin"),
    path('student_signup', job.student_signup, name="studentsignup"),
    path('job_list', job.job_list_post, name="joblistpost"),
]