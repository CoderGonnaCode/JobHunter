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

            response_serializer = self.serializer_class(job_area)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            job_area = JobArea.objects.get(pk=request.POST["id"])
            job_area.title=serializer.validated_data.get("title")
            job_area.realated_words=serializer.validated_data.get("related_words") 
            job_area.rank=serializer.validated_data.get("rank") 
            job_area.popularity=serializer.validated_data.get("popularity") 
            job_area.save()
            response_serializer = self.serializer_class(job_area)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteJobAreaView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, format=None):
        JobArea.objects.get(pk=pk).delete()
        return Response({"success": "1 job_area deleted"}, status=200)

class HunterViews(APIView):

    serializer_class = HunterSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, format=None):
        hunters = Hunter.objects.all()
        serializer = self.serializer_class(hunters, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            hunter = Hunter(
            id = serializer.validated_data.get("id"),
            user = request.user,
            full_name = serializer.validated_data.get("full_name"),
            email = serializer.validated_data.get("email"),
            phone = serializer.validated_data.get("phone"),
            birthday = serializer.validated_data.get("birthday"),
            isFemale = serializer.validated_data.get("isFemale"),
            address = serializer.validated_data.get("address"),
            city = serializer.validated_data.get("city"),
            position = serializer.validated_data.get("position"),
            thumbnailPath = request.data.get("thumbnailPath"),
            skills = serializer.validated_data.get("skills"),
            job_area = JobArea.objects.get(pk=request.POST["job_area"]),
            experience = serializer.validated_data.get("experience"),
            interests = serializer.validated_data.get("interests"),
            github_link = serializer.validated_data.get("github_link"),
            linkedin_link = serializer.validated_data.get("linkedin_link"),
            instagram_link = serializer.validated_data.get("instagram_link"),
            account_created_on = serializer.validated_data.get("account_created_on"),
            )

            hunter.save()
            response_serializer = self.serializer_class(hunter)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            hunter = Hunter.objects.get(pk=request.POST["id"])
            hunter.full_name=serializer.validated_data.get("full_name")
            hunter.email=serializer.validated_data.get("email") 
            hunter.phone=serializer.validated_data.get("phone") 
            hunter.address=serializer.validated_data.get("address") 
            hunter.skills=serializer.validated_data.get("skills") 
            hunter.thumbnailPath=serializer.validated_data.get("thumbnailPath") 
            hunter.experience=serializer.validated_data.get("experience") 
            hunter.github_link=serializer.validated_data.get("github_link") 
            hunter.linkedin_link=serializer.validated_data.get("linkedin_link") 
            hunter.instagram_link=serializer.validated_data.get("instagram_link")
            hunter.interests=serializer.validated_data.get("interests")
            hunter.save()
            response_serializer = self.serializer_class(hunter)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteHunterView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, format=None):
        Hunter.objects.get(pk=pk).delete()
        return Response({"success": "1 user deleted"}, status=200)

class CompanyViews(APIView):

    serializer_class = CompanySerializer
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = self.serializer_class(companies, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            company = Company(
            id = serializer.validated_data.get("id"),
            name = serializer.validated_data.get("name"),
            address = serializer.validated_data.get("address"),
            city = serializer.validated_data.get("city"),
            description = serializer.validated_data.get("description"),
            rank = serializer.validated_data.get("rank"),
            thumbnailPath = request.data.get("thumbnailPath"),
            linkedin_link = serializer.validated_data.get("linkedin_link"),
            instagram_link = serializer.validated_data.get("instagram_link"),
            )
            company.save()
            response_serializer = self.serializer_class(company)
            return Response(response_serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            company = Company.objects.get(pk=request.POST["id"])
            company.name=serializer.validated_data.get("name")
            company.address=serializer.validated_data.get("address") 
            company.city=serializer.validated_data.get("city") 
            company.description=serializer.validated_data.get("description") 
            company.rank=serializer.validated_data.get("rank") 
            company.thumbnailPath=serializer.validated_data.get("thumbnailPath") 
            company.linkedin_link=serializer.validated_data.get("linkedin_link") 
            company.instagram_link=serializer.validated_data.get("instagram_link") 
            company.save()
            response_serializer = self.serializer_class(company)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteCompanyAreaView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, format=None):
        Company.objects.get(pk=pk).delete()
        return Response({"success": "1 company deleted"}, status=200)

        

class VacancyViews(APIView):

    serializer_class = VacancySerializer
    def get(self, request, format=None):
        vacancies = Vacancy.objects.all()
        serializer = self.serializer_class(vacancies, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            vacancy = Vacancy(
            id = serializer.validated_data.get("id"),
            title = serializer.validated_data.get("title"),
            company = Company.objects.get(pk=request.POST["company"]),
            job_area = JobArea.objects.get(pk=request.POST["job_area"]),
            requirements = serializer.validated_data.get("requirements"),
            min_exp_time = serializer.validated_data.get("min_exp_time"),
            description = serializer.validated_data.get("description"),
            estimated_salary = serializer.validated_data.get("estimated_salary"),
            perks = serializer.validated_data.get("perks"),
            status = serializer.validated_data.get("status"),
            created_on = serializer.validated_data.get("created_on"),
            )
            vacancy.save()
            response_serializer = self.serializer_class(vacancy)
            return Response(response_serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            vacancy = Vacancy.objects.get(pk=request.POST["id"])
            vacancy.title=serializer.validated_data.get("title")
            vacancy.min_exp_time=serializer.validated_data.get("min_exp_time") 
            vacancy.requirements=serializer.validated_data.get("requirements") 
            vacancy.description=serializer.validated_data.get("description") 
            vacancy.estimated_salary=serializer.validated_data.get("estimated_salary") 
            vacancy.perks=serializer.validated_data.get("perks") 
            vacancy.status=serializer.validated_data.get("status")
            vacancy.job_area=JobArea.objects.get(pk=request.POST["job_area"]) 
            vacancy.company=Company.objects.get(pk=request.POST["company"]) 
            vacancy.save()
            response_serializer = self.serializer_class(vacancy)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteVacancyAreaView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, format=None):
        Vacancy.objects.get(pk=pk).delete()
        return Response({"success": "1 vacancy deleted"}, status=200)
    
class InternshipViews(APIView):

    serializer_class = IntershipSerializer
    def get(self, request, format=None):
        internships = Internship.objects.all()
        serializer = self.serializer_class(internships, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            internship = Internship(
            id = serializer.validated_data.get("id"),
            title = serializer.validated_data.get("title"),
            start_date = serializer.validated_data.get("start_date"),
            company = Company.objects.get(pk=request.POST["company"]),
            job_area = JobArea.objects.get(pk=request.POST["job_area"]),
            description = serializer.validated_data.get("description"),
            estimated_salary = serializer.validated_data.get("estimated_salary"),
            duration = serializer.validated_data.get("duration"),
            status = serializer.validated_data.get("status"),
            created_on = serializer.validated_data.get("created_on")
            )
            internship.save()
            response_serializer = self.serializer_class(internship)
            return Response(response_serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            internship = Internship.objects.get(pk=request.POST["id"])
            internship.title=serializer.validated_data.get("title")
            internship.start_date=serializer.validated_data.get("start_date") 
            internship.requirements=serializer.validated_data.get("requirements") 
            internship.description=serializer.validated_data.get("description") 
            internship.estimated_salary=serializer.validated_data.get("estimated_salary") 
            internship.duration=serializer.validated_data.get("duration") 
            internship.status=serializer.validated_data.get("status")
            internship.job_area=JobArea.objects.get(pk=request.POST["job_area"]) 
            internship.company=Company.objects.get(pk=request.POST["company"]) 
            internship.save()
            response_serializer = self.serializer_class(internship)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteInternshipAreaView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, format=None):
        Internship.objects.get(pk=pk).delete()
        return Response({"success": "1 internship deleted"}, status=200)
        
class StackViews(APIView):

    serializer_class = StackSerializer
    def get(self, request, format=None):
        stacks = Stack.objects.all()
        serializer = self.serializer_class(stacks, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            stack = Stack(
            id = serializer.validated_data.get("id"),
            title = serializer.validated_data.get("title"),
            job_area = JobArea.objects.get(pk=request.POST["job_area"]),
            description = serializer.validated_data.get("description"),
            popularity = serializer.validated_data.get("popularity"),
            features = serializer.validated_data.get("features"),
            created_on = serializer.validated_data.get("created_on")
            )
            stack.save()
            response_serializer = self.serializer_class(stack)
            return Response(response_serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            stack = Stack.objects.get(pk=request.POST["id"])
            stack.title=serializer.validated_data.get("title")
            stack.description=serializer.validated_data.get("description") 
            stack.features=serializer.validated_data.get("features") 
            stack.popularity=serializer.validated_data.get("popularity") 
            stack.job_area=JobArea.objects.get(pk=request.POST["job_area"]) 
            stack.save()
            response_serializer = self.serializer_class(stack)
            return Response(response_serializer.data)
        else:
            return Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteStackAreaView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, format=None):
        Stack.objects.get(pk=pk).delete()
        return Response({"success": "1 stack deleted"}, status=200)


class RoadmapViews(APIView):

    serializer_class = RoadmapSerializer
    def get(self, request, format=None):
        roadmaps = Roadmap.objects.all()
        serializer = self.serializer_class(roadmaps, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            roadmap = Roadmap(
            id = serializer.validated_data.get("id"),
            title = serializer.validated_data.get("title"),
            plan = serializer.validated_data.get("plan"),
            created_on = serializer.validated_data.get("created_on"),
            updated_on = serializer.validated_data.get("updated_on")
            )
            roadmap.save()
            response_serializer = self.serializer_class(roadmap)
            return Response(response_serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# 'id', 'title', 'created_on' , 'updated_on', 'roadmap', 'technologies', 'useful_links', 'tutorials'

class DeleteRoadmapView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, format=None):
        Roadmap.objects.get(pk=pk).delete()
        return Response({"success": "1 roadmap deleted"}, status=200)

class PlanItemViews(APIView):

    serializer_class = PlanItemSerializer
    def get(self, request, format=None):
        plan_items = PlanItem.objects.all()
        serializer = self.serializer_class(plan_items, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            plan_item = PlanItem(
            id = serializer.validated_data.get("id"),
            title = serializer.validated_data.get("title"),
            created_on = serializer.validated_data.get("created_on"),
            updated_on = serializer.validated_data.get("updated_on"),
            roadmap = Roadmap.objects.get(pk=request.POST["roadmap"]),
            technologies = serializer.validated_data.get("technologies"),
            useful_links = serializer.validated_data.get("useful_links"),
            tutorials = serializer.validated_data.get("tutorials")
            )
            plan_item.save()
            response_serializer=self.serializer_class(plan_item)
            return Response(response_serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeletePlanView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, format=None):
        PlanItem.objects.get(pk=pk).delete()
        return Response({"success": "1 plan deleted"}, status=200)

class TestViews(APIView):

    serializer_class = TestSerializer
    def get(self, request, format=None):
        tests = Test.objects.all()
        serializer = self.serializer_class(tests, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            test = Test(
            id = serializer.validated_data.get("id"),
            stack = Stack.objects.get(pk=request.POST["stack"]),
            questions = serializer.validated_data.get("questions"),
            solutions = serializer.validated_data.get("solutions")
            )
            test.save()
            response_serializer=self.serializer_class(test)
            return Response(response_serializer.data)
        else:
            Response({"msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DeleteTestView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request, pk, format=None):
        Test.objects.get(pk=pk).delete()
        return Response({"success": "1 test deleted"}, status=200)