from django.shortcuts import render
from .models import Hunter, JobArea, Company, Internship, Stack, Roadmap, PlanItem, Test, Vacancy
from .serializers import HunterSerializer, JobAreaSerializer, CompanySerializer, IntershipSerializer, StackSerializer, RoadmapSerializer,PlanItemSerializer,TestSerializer,VacancySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

class JobAreaViews(APIView):

    serializer_class = JobAreaSerializer
    def get(self, request, format=None):
        job_areas = JobArea.objects.all()
        serializer = self.serializer_class(job_areas, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            job_area = JobArea(
            id = serializer.validated_data.get("id"),
            title=serializer.validated_data.get("title"),
            related_words=serializer.validated_data.get("related_words"),
            description=serializer.validated_data.get("description"),
            rank=serializer.validated_data.get("rank"),
            popularity=serializer.validated_data.get("popularity"),
            )
            job_area.save()

            response_serializer = self.serilizer_class(job_area)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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