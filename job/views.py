from django.core.paginator import Paginator
from django.shortcuts import render, redirect
import datetime
import uuid

# Create your views here.
jobs = [ 
        dict(
            pk=str(uuid.uuid4()),
            opening=30,
            title="software Engineer", 
            details="Experienced in Node.Js, Java, Spring, Bootstrap, Python and Selenium integration and Unit Testing",
            salary="26K - 30k Monthly",
            place='Poland',
            time=datetime.date.fromisoformat("2024-04-24").isoformat(),
            image_url="jobs/job_1.jpeg",
            app_date=datetime.datetime.now(),
            last_date=datetime.datetime.now(),
            company_name="Microsoft"
        ),
        dict(
            pk=str(uuid.uuid4()),
            title="mobile App Engineer",
            details="Experienced in Flutter or React native for uilding a startup app",
            opening=10,
            salary="8k - 10K Monthly",
            place="USA",
            time=datetime.date.fromisoformat("2024-04-24").isoformat(),
            image_url="jobs/job_2.jpeg",
            app_date=datetime.datetime.now(),
            last_date=datetime.datetime.now(),
            company_name="Microsoft"
        ),
        dict(
            pk=str(uuid.uuid4()),
            title="mobile App Developer needed in Binance",
            details="Binance is looking for senior mobile app developer with at least 10 years of experience building cross platform application with flutter, firebase and react native. The role is also remote based and also  willing to attend yearly meeting at binance head quarters in your country",
            opening=10,
            salary="50k - 100K Monthly",
            place="USA",
            time=datetime.date.fromisoformat("2024-04-24").isoformat(),
            image_url="jobs/job_5.jpeg",
            app_date=datetime.datetime.now(),
            last_date=datetime.datetime.now(),
            company_name="Microsoft"
        ),
    ]

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

def job_list_post(requests):
    global jobs
    length = 10
    pages = Paginator(jobs, length)
    page_number = requests.GET.get("page", 1)
    page_obj = pages.get_page(page_number)
    context = {'jobs': jobs[(int(page_number)*length)-length: (int(page_number)*length)], 'page_obj': page_obj}
    if query := requests.GET.get("query"):
        context['query'] = query
    print(jobs, end="\n\n")
    return render(requests, "job/job_list.html", context)

def job_single(requests, primary_key):
    print(jobs, end="\n\n")
    if not (single := [i for i in jobs if i['pk'] == primary_key]):
        return redirect('landingpage')
    single = single[0]
    return render(requests, "job/single_job.html", context={'single':single})

def reset_password(requests):
    return render(requests, "auth/reset_password.html")

def change_password(requests):
    return render(requests, "auth/change_password.html")

def company_profile(requests):
    return render(requests, "job/company_profile.html")

def student_profile(requests):
    return render(requests, "job/student_profile.html")

def admin_profile(requests):
    return render(requests, "job/admin_profile.html")