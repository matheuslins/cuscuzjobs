from django.urls import path, include

from .views import DashboardView


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard')
]
