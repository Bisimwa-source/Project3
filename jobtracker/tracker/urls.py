from django.urls import path
from . import views

urlpatterns = [
    # Home redirect
    path("", views.company_list, name="home"),

    # Companies
    path("companies/", views.company_list, name="company_list"),
    path("companies/create/", views.company_create, name="company_create"),
    path("companies/<int:pk>/edit/", views.company_update, name="company_update"),
    path("companies/<int:pk>/delete/", views.company_delete, name="company_delete"),

    # Jobs
    path("jobs/", views.job_list, name="job_list"),
    path("jobs/create/", views.job_create, name="job_create"),
    path("jobs/<int:pk>/edit/", views.job_update, name="job_update"),
    path("jobs/<int:pk>/delete/", views.job_delete, name="job_delete"),

    # Applications
    path("applications/", views.application_list, name="application_list"),
    path("applications/create/", views.application_create, name="application_create"),
    path("applications/<int:pk>/edit/", views.application_update, name="application_update"),
    path("applications/<int:pk>/delete/", views.application_delete, name="application_delete"),

    # Interviews
    path("interviews/", views.interview_list, name="interview_list"),
    path("interviews/create/", views.interview_create, name="interview_create"),
    path("interviews/<int:pk>/edit/", views.interview_update, name="interview_update"),
    path("interviews/<int:pk>/delete/", views.interview_delete, name="interview_delete"),

    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
]




