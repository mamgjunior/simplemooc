from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()

    template_name = 'accounts/register.html'
    context = {'form': form}
    return render(request, template_name, context)
