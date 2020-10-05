from django.shortcuts import render, get_object_or_404

from .forms import ContactCourse
from .models import Course


# Create your views here.

def index(request):
    courses = Course.object.all()
    template_name = "courses/index.html"
    context = {"courses": courses}
    return render(request, template_name, context)


# def details(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     template_name = "courses/details.html"
#     context = {"course": course}
#     return render(request, template_name, context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    if request.method == "POST":
        form = ContactCourse(request.POST)
    else:
        form = ContactCourse()

    template_name = "courses/details.html"
    context = {
        "course": course,
        "form": form
    }
    return render(request, template_name, context)
