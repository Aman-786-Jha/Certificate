# certificates/urls.py
from django.urls import path
from . import views

app_name = 'myapps'

urlpatterns = [
    path('create/', views.create_certificate, name='create_certificate'),
    path('verify/', views.verify_certificate, name='verify_certificate'),
    # Add other URL patterns for additional views if needed
]
