# Generated by Django 4.2 on 2024-01-16 14:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answers",
            name="user",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="question",
            name="user",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]