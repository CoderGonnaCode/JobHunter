from django.urls import path
from . import views

urlpatterns = [
    path('job_areas', views.JobAreaViews.as_view()),
    path('job_areas/<int:pk>', views.DeleteJobAreaView.as_view()),
    path('hunters', views.HunterViews.as_view()),
    path('hunters/<int:pk>', views.DeleteHunterView.as_view()),
    path('companies', views.CompanyViews.as_view()),
    path('companies/<int:pk>', views.DeleteCompanyAreaView.as_view()),
    path('vacancies', views.VacancyViews.as_view()),
    path('vacancies/<int:pk>', views.DeleteVacancyAreaView.as_view()),
    path('internships', views.InternshipViews.as_view()),
    path('internships/<int:pk>', views.DeleteInternshipAreaView.as_view()),
    path('stacks', views.StackViews.as_view()),
    path('stacks/<int:pk>', views.DeleteStackAreaView.as_view()),
    path('roadmaps', views.RoadmapViews.as_view()),
    path('plan_items', views.PlanItemViews.as_view()),
    path('tests', views.TestViews.as_view())
]
