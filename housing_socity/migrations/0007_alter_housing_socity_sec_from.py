# Generated by Django 4.2.4 on 2023-08-27 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("housing_socity", "0006_alter_housing_socity_sec_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="housing_socity",
            name="sec_from",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 27, 8, 29, 10, 85908, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]