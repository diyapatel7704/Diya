# Generated by Django 4.2.4 on 2023-09-09 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("housing_socity", "0011_complain"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complain",
            name="solve_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="housing_socity.housing_socity",
            ),
        ),
    ]