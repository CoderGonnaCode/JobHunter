# Generated by Django 3.0.3 on 2020-03-09 08:20

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_hunter_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hunter',
            name='thumbnailPath',
            field=models.ImageField(blank=True, null=True, upload_to=items.models.upload_thumb),
        ),
    ]