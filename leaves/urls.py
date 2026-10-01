from django.urls import path
from .views import LeaveListCreateView, LeaveDetailView


urlpatterns = [
    path('', LeaveListCreateView.as_view(), name='leave-list-create'),
    path('<int:pk>/', LeaveDetailView.as_view(), name='leave-detail'),
]