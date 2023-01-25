from django.urls import path
from . import views

urlpatterns = [
    path("/<int:pk>", views.OrderDetailView.as_view()),
    path("", views.OrderListView.as_view()),
]