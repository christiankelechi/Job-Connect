# Generated by Django 4.2.4 on 2024-11-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_root_api_security_user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
