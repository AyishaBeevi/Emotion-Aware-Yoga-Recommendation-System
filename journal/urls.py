from django.urls import path
from . import views

urlpatterns = [
    path("journal/", views.journal, name="journal"),
]