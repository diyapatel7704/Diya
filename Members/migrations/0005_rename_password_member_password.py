# Generated by Django 4.2.4 on 2023-09-05 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Members", "0004_member_password"),
    ]

    operations = [
        migrations.RenameField(
            model_name="member",
            old_name="password",
            new_name="Password",
        ),
    ]