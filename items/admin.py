from django.contrib import admin
from .models import JobArea,Hunter,Company,Vacancy,Internship,Stack,Roadmap,PlanItem,Test
# Register your models here.
admin.site.register(JobArea)
admin.site.register(Hunter)
admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Internship)
admin.site.register(Stack)
admin.site.register(Roadmap)
admin.site.register(PlanItem)
admin.site.register(Test)