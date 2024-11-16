from django.shortcuts import render

# Create your views here.

def landing_page(requests):
    return render(requests, "landing_page.html")

def about_us(requests):
    return render(requests, "about_us.html")

def contact_us(requests):
    return render(requests, "contact_us.html")

def student_login(requests):
    return render(requests, "auth/student_login.html")

def student_signup(requests):
    return render(requests, "auth/student_signup.html")

def admin_login(requests):
    return render(requests, "auth/company_login.html")

def admin_signup(requests):
    return render(requests, 'auth/company_signup.html')