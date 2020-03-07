from django.shortcuts import render
from .models import Hunter, JobArea, Company, Internship, Stack, Roadmap, PlanItem, Test
from .serializers import HunterSerializer, JobAreaSerializer, CompanySerializer, IntershipSerializer, StackSerializer, RoadmapSerializer,PlanItemSerializer,TestSerializer
from rest_framework.views import APIView, Response

class JobAreaViews(APIView):

    serilizer_class = JobAreaSerializer
    def get(self, request, format=None):
        job_areas = JobArea.objects.all()
        serilized = self.serilizer_class(job_areas, many = True)
        return Response(serilized.data)