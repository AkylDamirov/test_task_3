# Generated by Django 5.0.4 on 2024-04-17 23:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("task_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="collect",
            name="amount_donations",
        ),
    ]
