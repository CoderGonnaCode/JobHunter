from django.shortcuts import render
from .models import Hunter, JobArea, Company, Internship, Stack, Roadmap, PlanItem, Test, Vacancy
from .serializers import HunterSerializer, JobAreaSerializer, CompanySerializer, IntershipSerializer, StackSerializer, RoadmapSerializer,PlanItemSerializer,TestSerializer,VacancySerializer
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAdminUser, AllowAny, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly

class JobAreaViews(APIView):

    serilizer_class = JobAreaSerializer
    def get(self, request, format=None):
        job_areas = JobArea.objects.all()
        serilized = self.serilizer_class(job_areas, many = True)
        return Response(serilized.data)

class HunterViews(APIView):

    serializer_class = HunterSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        hunters = Hunter.objects.all()
        serilized = self.serializer_class(hunters, many = True)
        return Response(serilized.data)


class CompanyViews(APIView):

    serilizer_class = CompanySerializer
    def get(self, request, format=None):
        companies = Company.objects.all()
        serilized = self.serilizer_class(companies, many = True)
        return Response(serilized.data)

class VacancyViews(APIView):

    serilizer_class = VacancySerializer
    def get(self, request, format=None):
        vacancies = Vacancy.objects.all()
        serilized = self.serilizer_class(vacancies, many = True)
        return Response(serilized.data)

class InternshipViews(APIView):

    serilizer_class = IntershipSerializer
    def get(self, request, format=None):
        internships = Internship.objects.all()
        serilized = self.serilizer_class(internships, many = True)
        return Response(serilized.data)

class StackViews(APIView):

    serilizer_class = StackSerializer
    def get(self, request, format=None):
        stacks = Stack.objects.all()
        serilized = self.serilizer_class(stacks, many = True)
        return Response(serilized.data)

class RoadmapViews(APIView):

    serilizer_class = RoadmapSerializer
    def get(self, request, format=None):
        roadmaps = Roadmap.objects.all()
        serilized = self.serilizer_class(roadmaps, many = True)
        return Response(serilized.data)

class PlanItemViews(APIView):

    serilizer_class = PlanItemSerializer
    def get(self, request, format=None):
        plan_items = PlanItem.objects.all()
        serilized = self.serilizer_class(plan_items, many = True)
        return Response(serilized.data)

class TestViews(APIView):

    serilizer_class = TestSerializer
    def get(self, request, format=None):
        tests = Test.objects.all()
        serilized = self.serilizer_class(tests, many = True)
        return Response(serilized.data)