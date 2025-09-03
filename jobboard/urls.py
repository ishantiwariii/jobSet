from django.urls import path
from . import views

urlpatterns = [
    path('find-jobs/', views.find_jobs_view, name='find-jobs'),   
    path('jobs/apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('applied-jobs/', views.applied_jobs_, name='applied-jobs'),
    path("jobs/<int:job_id>/", views.job_detail, name="job_detail"),
]
