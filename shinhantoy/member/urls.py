from django.urls import path
from . import views

urlpatterns = [
    path("/password", views.MemberDetailView.as_view()),
    path("", views.MemberRegisterView.as_view()),
]