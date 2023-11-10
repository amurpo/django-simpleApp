# myapp/views.py

from django.shortcuts import render, redirect
from .models import FormData

def index(request):
    return render(request, 'index.html')

def submit_form(request):
    if request.method == 'POST':
        # Process form submission
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Save data to the database
        form_data = FormData(name=name, email=email)
        form_data.save()

        # Redirect to a success page or render a template
        return render(request, 'success.html', {'form_data': form_data})

    return redirect('index')
