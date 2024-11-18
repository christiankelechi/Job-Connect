#!/usr/bin/env python3fr
from django.urls import path
import job.views as job

urlpatterns = [
    path("", job.landing_page, name="landingpage"),
    path("about-us", job.about_us, name="aboutus"),
    path('contact_us', job.contact_us, name="contactus"),
    path("admin_login", job.admin_login, name="adminlogin"),
    path('job_list', job.job_list_post, name="joblistpost"),
    path("admin_signup", job.admin_signup, name="adminsignup"),
    path('student_login', job.student_login, name="studentlogin"),
    path('student_signup', job.student_signup, name="studentsignup"),
    path("single-job/<str:primary_key>", job.job_single, name="singlejob"),
    path("reset_password", job.reset_password, name="resetpassword"),
    path("change_password", job.change_password, name="changepassword"),
    path("admin_profile", job.admin_profile, name="adminprofile"),
    path("student_profile", job.student_profile, name="studentprofile"),
    path("company_profile", job.company_profile, name="companyprofile")
]