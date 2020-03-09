from django.db import models

from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

def upload_thumb(instance, filename):
    lastDot = filename.rfind('.')
    extension= filename[lastDot:len(filename):1]
    return '%s-%s%s' % (instance.full_name, time.time(), extension)

class JobArea(models.Model):
    title =models.CharField(max_length=100)
    related_words = ArrayField(models.CharField(max_length=200), default=list)
    description = models.TextField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Hunter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20,blank=True, null=True)
    birthday = models.DateField()
    isFemale = models.BooleanField()  # 0 - female, 1 - male
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True, null=True)  # beginner, junior , middle, senior, etc.
    thumbnailPath = models.ImageField(upload_to=upload_thumb,blank=True, null=True)
    skills =  ArrayField(models.CharField(max_length=200),default=list)
    job_area =models.ForeignKey(JobArea,on_delete=models.CASCADE,related_name='hunters')
    experience = models.IntegerField(blank=True, null=True) # TODO need  Map Field like {'python': 3, 'django': 1 }
    interests = ArrayField(models.CharField(max_length=200),default=list)
    github_link = models.CharField(max_length=200, blank=True, null=True)    # TODO change to  Map Field like {'github': "http://...", 'Linkedin':"http://..." }
    linkedin_link = models.CharField(max_length=200,  blank=True, null=True)
    instagram_link = models.CharField(max_length=200,  blank=True, null=True)
    account_created_on = models.DateField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.full_name

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    description = models.TextField()
    rank = models.IntegerField(blank=True, null=True)
    thumbnailPath = models.ImageField(blank=True, null=True)
    linkedin_link = models.CharField(max_length=200,  blank=True, null=True)
    instagram_link = models.CharField(max_length=200,  blank=True, null=True)


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='vacancies')
    job_area =models.ForeignKey(JobArea,on_delete=models.CASCADE,related_name='vacancies')
    requirements = ArrayField(models.CharField(max_length=200),default=list)
    min_exp_time = models.IntegerField()
    description = models.TextField()
    estimated_salary = models.IntegerField(blank=True, null=True)
    perks = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)

class Internship(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='interships')
    job_area =models.ForeignKey(JobArea,on_delete=models.CASCADE,related_name='interships')
    requirements = ArrayField(models.CharField(max_length=200),default=list)
    description = models.TextField()
    estimated_salary = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)

class Stack(models.Model):
    title = models.CharField(max_length=200)
    job_area = models.ForeignKey(JobArea,on_delete=models.CASCADE,related_name='stack')
    description = models.TextField()
    popularity = models.IntegerField(blank=True, null=True)
    features = ArrayField(models.CharField(max_length=200),default=list)
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)

class Roadmap(models.Model):
    title = models.CharField(max_length=200)
    plan = ArrayField(models.CharField(max_length=200),default=list)
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateField(auto_now_add=True, blank=True, null=True)


class PlanItem(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateField(auto_now_add=True, blank=True, null=True)
    roadmap = models.ForeignKey(Roadmap,on_delete=models.CASCADE,related_name='planItem')
    technologies = ArrayField(models.CharField(max_length=200),default=list)
    useful_links = ArrayField(models.CharField(max_length=200),default=list)
    tutorials = ArrayField(models.CharField(max_length=200),default=list)

class Test(models.Model):
    stack = models.ForeignKey(Stack,on_delete=models.CASCADE,related_name='Test')
    questions = ArrayField(models.CharField(max_length=200),default=list)  # TODO need  Map Field like {'python': 3, 'django': 1 }
    solutions = ArrayField(models.CharField(max_length=200),default=list) 




