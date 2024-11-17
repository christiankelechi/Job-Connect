from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
import datetime
import uuid

# Create your views here.
jobs = [ 
        dict(
            pk=uuid.uuid4(),
            distance=30,
            title="software Engineer", 
            details="Experienced in Node.Js, Java, Spring, Bootstrap, Python and Selenium integration and Unit Testing",
            salary="26K - 30k Monthly",
            place='Poland',
            time=datetime.date.fromisoformat("2024-04-24").isoformat(),
            image_url="jobs/job_1.jpeg",
        ),
        dict(
            pk=uuid.uuid4(),
            title="mobile App Engineer",
            details="Experienced in Flutter or React native for uilding a startup app",
            distance=10,
            salary="8k - 10K Monthly",
            place="USA",
            time=datetime.date.fromisoformat("2024-04-24").isoformat(),
            image_url="jobs/job_2.jpeg"
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
    return render(requests, "job/job_list.html", context)

def job_single(requests, primary_key):
    single = [i for i in jobs if i['px'] == primary_key][0]
    return render(requests, "job/single_job.html", context={'single':single})