# myapp/urls.py

from django.urls import path
from .views import index, submit_form

urlpatterns = [
    path('', index, name='index'),
    path('submit_form/', submit_form, name='submit_form'),  # Add this line
    # Add other URL patterns as needed
]
