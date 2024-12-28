from django.urls import path
from django_distill import distill_path
from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
# ]

def get_index():
    return None

urlpatterns = [
    distill_path('', views.home, name='home', distill_func=get_index),
    distill_path('about/', views.about, name='about', distill_func=get_index),
    distill_path('contact/', views.contact, name='contact', distill_func=get_index),
]