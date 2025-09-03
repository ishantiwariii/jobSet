from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from . models import Job,AppliedJob

# Create your views here.
@login_required(login_url='/login/')
def find_jobs_view(request):
    jobs = Job.objects.all()
    return render(request, 'find-jobs.html', {'jobs': jobs})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if AppliedJob.objects.filter(user=request.user, job=job).exists():
        messages.warning(request, "You already applied to this job.")
    else:
        AppliedJob.objects.create(user=request.user, job=job)
        messages.success(request, "Job applied successfully.")

    return redirect('applied-jobs')

@login_required
def applied_jobs_(request):
    applied_jobs = AppliedJob.objects.filter(user=request.user).select_related('job').order_by('-applied_at')
    return render(request, 'applied-jobs.html', {'applied_jobs': applied_jobs})

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "info.html", {"job": job})