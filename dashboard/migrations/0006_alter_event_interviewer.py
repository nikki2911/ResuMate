# Generated by Django 5.0.4 on 2024-10-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_for_designation_event_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='interviewer',
            field=models.JSONField(),
        ),
    ]
