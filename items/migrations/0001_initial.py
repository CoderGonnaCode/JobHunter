# Generated by Django 3.0.3 on 2020-03-07 09:58

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('thumbnailPath', models.ImageField(blank=True, null=True, upload_to='')),
                ('linkedin_link', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('related_words', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('description', models.TextField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('popularity', models.IntegerField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('plan', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('updated_on', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('popularity', models.IntegerField(blank=True, null=True)),
                ('features', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('job_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stack', to='items.JobArea')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('requirements', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('min_exp_time', models.IntegerField()),
                ('description', models.TextField()),
                ('estimated_salary', models.IntegerField(blank=True, null=True)),
                ('perks', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='items.Company')),
                ('job_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='items.JobArea')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('solutions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('stack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Test', to='items.Stack')),
            ],
        ),
        migrations.CreateModel(
            name='PlanItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('updated_on', models.DateField(auto_now_add=True, null=True)),
                ('technologies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('useful_links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('tutorials', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('roadmap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planItem', to='items.Roadmap')),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('requirements', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('description', models.TextField()),
                ('estimated_salary', models.IntegerField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interships', to='items.Company')),
                ('job_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interships', to='items.JobArea')),
            ],
        ),
        migrations.CreateModel(
            name='Hunter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birthday', models.DateField()),
                ('isFemale', models.BooleanField()),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('thumbnailPath', models.ImageField(blank=True, null=True, upload_to='')),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('interests', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('github_link', models.CharField(blank=True, max_length=200, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=200, null=True)),
                ('account_created_on', models.DateField(auto_now_add=True, null=True)),
                ('job_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunters', to='items.JobArea')),
            ],
        ),
    ]