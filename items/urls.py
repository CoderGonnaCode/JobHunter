from django.urls import path
from . import views
urlpatterns = [
    path('job_areas', views.JobAreaViews.as_view())
]
