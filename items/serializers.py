from rest_framework import serializers
from .models import Hunter, JobArea, Company, Internship, Stack, Roadmap, PlanItem, Test, Vacancy
from myauth.serializers import UserSerializer

class JobAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobArea
        fields = ('id', 'title', 'related_words', 'description','rank','popularity','created_on')

class HunterSerializer(serializers.ModelSerializer):
    job_area = JobAreaSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Hunter
        fields = ('id', "user",'full_name', 'email', 'phone', 'birthday', 'isFemale', 'address', 'city','position','thumbnailPath',"skills", "job_area",'experience', 'interests','github_link', 'linkedin_link', 'instagram_link', 'account_created_on' )

class CompanySerializer(serializers.ModelSerializer):
    job_area = JobAreaSerializer(read_only=True)
    class Meta:
        model = Company
        fields = ('id', 'name', 'address', 'city', 'description', 'rank', 'thumbnailPath', 'linkedin_link', 'instagram_link')

class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    job_area = JobAreaSerializer(read_only=True)
    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'company', 'job_area', 'requirements', 'min_exp_time', 'description', 'estimated_salary', 'perks', 'status', 'created_on')

class IntershipSerializer(serializers.ModelSerializer):
    job_area = JobAreaSerializer(read_only=True)
    class Meta:
        model = Internship
        fields = ('id', 'title', 'start_date', 'company','job_area', 'description', 'estimated_salary', 'duration', 'status', 'created_on')

class StackSerializer(serializers.ModelSerializer):
    job_area = JobAreaSerializer(read_only=True)
    class Meta:
        model = Stack
        fields = ('id', 'title', 'job_area', 'description', 'popularity','features', 'created_on' )

class RoadmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roadmap
        fields = ('id', 'title', 'plan','created_on' , 'updated_on')


class PlanItemSerializer(serializers.ModelSerializer):
    roadmap = RoadmapSerializer(read_only=True)
    class Meta:
        model = PlanItem
        fields = ('id', 'title', 'created_on' , 'updated_on', 'roadmap', 'technologies', 'useful_links', 'tutorials')

class TestSerializer(serializers.ModelSerializer):
    stack = StackSerializer(read_only=True)
    class Meta:
        model = Test
        fields = ('id', 'stack', 'questions', 'solutions')