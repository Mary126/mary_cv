from django.shortcuts import render
from .models import Project, Category
from django.shortcuts import get_object_or_404


def main_page(request):
    return render(request, 'index.html')


def projects_page(request):
    categories = Category.objects.all()
    return render(request, 'projects.html', {'categories': categories})


def project(request, pk):
    proj = get_object_or_404(Project, pk=pk)
    return render(request, 'project_page.html', {'project': proj})


def cv_page(request):
    return render(request, 'cv_page.html')


def contacts_page(request):
    return render(request, 'contacts_page.html')
