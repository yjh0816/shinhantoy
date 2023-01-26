from django.urls import path
from . import views

urlpatterns = [
    path("/<int:order_id>/comment/<int:pk>", views.CommentCreateView.as_view()),
    path("/<int:order_id>/comment", views.CommentListView.as_view()),
    path("/<int:pk>", views.OrderDetailView.as_view()),
    path("/comment", views.CommentCreateView.as_view()),
    path("", views.OrderListView.as_view()),
]