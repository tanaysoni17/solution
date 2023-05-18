from django.urls import path
from . import views

urlpatterns = [
    path('innovation/', views.innovation),
]
