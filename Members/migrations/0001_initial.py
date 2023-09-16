# Generated by Django 4.2.4 on 2023-08-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fname", models.CharField(max_length=30)),
                ("lname", models.CharField(max_length=30)),
                ("mobile", models.CharField(max_length=13)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("flat_no", models.IntegerField()),
                ("wing", models.CharField(max_length=1)),
                ("res_from", models.DateField(null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("res_type", models.CharField(default="owner", max_length=20)),
                ("verify", models.BooleanField(default=False)),
            ],
        ),
    ]
