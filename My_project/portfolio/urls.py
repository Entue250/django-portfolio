from django.urls import path
from django_distill import distill_path
from . import views

urlpatterns = [
    path('', distill_path(views.home, name='home')),
    path('about/', distill_path(views.about, name='about')),
    path('contact/', distill_path(views.contact, name='contact')),
]