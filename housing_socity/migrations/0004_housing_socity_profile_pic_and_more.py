# Generated by Django 4.2.4 on 2023-08-21 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("housing_socity", "0003_alter_housing_socity_sec_from"),
    ]

    operations = [
        migrations.AddField(
            model_name="housing_socity",
            name="profile_pic",
            field=models.FileField(default="avatar.jpg", upload_to="profile"),
        ),
        migrations.AlterField(
            model_name="housing_socity",
            name="sec_from",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 21, 9, 34, 42, 281686, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
