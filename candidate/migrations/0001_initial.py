# Generated by Django 5.0.4 on 2024-08-29 06:27

import candidate.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('contact', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('dob', models.DateField(blank=True, null=True)),
                ('doc', models.DateField(blank=True, default=candidate.models.today)),
                ('linkedin', models.URLField(blank=True, max_length=255, null=True)),
                ('github', models.URLField(blank=True, max_length=255, null=True)),
                ('portfolio', models.URLField(blank=True, max_length=255, null=True)),
                ('blog', models.URLField(blank=True, max_length=255, null=True)),
                ('education', models.CharField(max_length=255)),
                ('experience', models.PositiveIntegerField(blank=True, default=0)),
                ('current_designation', models.CharField(blank=True, max_length=255, null=True)),
                ('current_organization', models.CharField(blank=True, max_length=255, null=True)),
                ('current_ctc', models.FloatField(blank=True, default=0, max_length=255)),
                ('current_ctc_ih', models.FloatField(blank=True, default=0, max_length=255)),
                ('expected_ctc', models.FloatField(blank=True, default=0, max_length=255)),
                ('expected_ctc_ih', models.FloatField(blank=True, default=0, max_length=255)),
                ('offer_in_hand', models.FloatField(blank=True, default=0, max_length=255)),
                ('notice_period', models.PositiveIntegerField(blank=True, default=0)),
                ('reason_for_change', models.CharField(blank=True, max_length=500, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('job_openings', models.ManyToManyField(blank=True, to='manager.jobopening')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_resume', models.FileField(upload_to='resumes/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc'], message='Select pdf, docx or doc files only')])),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('filename', models.CharField(blank=True, max_length=255)),
                ('text_content', models.TextField()),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to='candidate.candidate')),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
