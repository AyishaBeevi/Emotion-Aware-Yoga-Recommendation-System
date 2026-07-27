from django.urls import path
from . import views

urlpatterns = [

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "analysis/",
        views.analysis,
        name="analysis"
    ),

    path(
    "recommendation/",
    views.recommendation,
    name="recommendation"
),

    path(
        "history/",
        views.history,
        name="history"
    ),

]