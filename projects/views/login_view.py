from django.shortcuts import render
from projects.models.models import Project
from django.conf import settings


def project_index(request):
    print(settings.BASE_DIR)
    print(settings.STATIC_ROOT)
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'login.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
