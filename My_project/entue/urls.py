from django.urls import path
from . import views
urlpatterns = [
    # path('', views.hey, name='Greet')
    path('', views.fm, name='Greet'),
    path('<str:name>', views.salute, name="salute"),
    path('eduard', views.eduard, name="eduard")
]