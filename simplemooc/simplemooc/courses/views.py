from django.shortcuts import render
from .models import Course


# Create your views here.

def index(request):
    courses = Course.object.all()
    template_name = "courses/index.html"
    context = {"courses": courses}
    return render(request, template_name, context)


def details(request, pk):
    course = Course.object.get(pk=pk)
    template_name = "courses/details.html"
    context = {"course": course}
    return render(request, template_name, context)
