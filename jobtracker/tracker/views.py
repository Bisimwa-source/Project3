from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from .forms import CompanyForm
from .models import Company, Job, Application, Interview
from .forms import CompanyForm, JobForm, ApplicationForm, InterviewForm
from django.db.models import Count, Avg

# Create your views here.
def company_list(request):
    companies = Company.objects.all()
    return render(request, "companies/list.html", {"companies": companies})

def company_create(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("company_list")
    return render(request, "companies/form.html", {"form": form})

def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    form = CompanyForm(request.POST or None, instance=company)
    if form.is_valid():
        form.save()
        return redirect("company_list")
    return render(request, "companies/form.html", {"form": form})

def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return redirect("company_list")

# ============================
# JOBS CRUD
# ============================

def job_list(request):
    jobs = Job.objects.all()
    return render(request, "jobs/list.html", {"jobs": jobs})

def job_create(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("job_list")
    return render(request, "jobs/form.html", {"form": form})

def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect("job_list")
    return render(request, "jobs/form.html", {"form": form})

def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    job.delete()
    return redirect("job_list")

# ============================
# APPLICATIONS CRUD
# ============================

def application_list(request):
    applications = Application.objects.all()
    return render(request, "applicationss/list.html", {"applications": applications})

def application_create(request):
    form = ApplicationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("application_list")
    return render(request, "applicationss/form.html", {"form": form})

def application_update(request, pk):
    application = get_object_or_404(Application, pk=pk)
    form = ApplicationForm(request.POST or None, instance=application)
    if form.is_valid():
        form.save()
        return redirect("application_list")
    return render(request, "applicationss/form.html", {"form": form})

def application_delete(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.delete()
    return redirect("application_list")

# ============================
# INTERVIEWS CRUD
# ============================

def interview_list(request):
    interviews = Interview.objects.all()
    return render(request, "interviews/list.html", {"interviews": interviews})

def interview_create(request):
    form = InterviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("interview_list")
    return render(request, "interviews/form.html", {"form": form})

def interview_update(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    form = InterviewForm(request.POST or None, instance=interview)
    if form.is_valid():
        form.save()
        return redirect("interview_list")
    return render(request, "interviews/form.html", {"form": form})

def interview_delete(request, pk):
    interview = get_object_or_404(Interview, pk=pk)
    interview.delete()
    return redirect("interview_list")


from django.db.models import Count, Avg

def dashboard(request):
    total_companies = Company.objects.count()
    total_jobs = Job.objects.count()
    total_applications = Application.objects.count()
    total_interviews = Interview.objects.count()

    apps_per_company = Company.objects.annotate(
        app_count=Count("job__application")
    )

    return render(request, "dashboard.html", {
        "total_companies": total_companies,
        "total_jobs": total_jobs,
        "total_applications": total_applications,
        "total_interviews": total_interviews,
        "apps_per_company": apps_per_company,
    })
