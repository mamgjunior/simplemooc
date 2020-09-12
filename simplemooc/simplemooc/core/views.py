from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "home.html", {"usuario": "Marcos Maia"})


def contato(request, template_name="contato.html"):
    return render(request, template_name)
