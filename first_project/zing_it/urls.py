from django.urls import path
from zing_it import views

urlpatterns = [
    path('', views.home, name="home"),
    path('playlist/<int:id>', views.playlist, name="playlist"),
]