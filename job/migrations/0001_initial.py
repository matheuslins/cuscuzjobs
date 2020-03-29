# Generated by Django 3.0.4 on 2020-03-29 22:32

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('users_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField()),
                ('_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Type')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('benefits', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='Benefits'), blank=True, null=True, size=None)),
                ('technologies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200, verbose_name='Technologies'), blank=True, null=True, size=None)),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Location')),
                ('experience_level', models.CharField(blank=True, max_length=100, null=True, verbose_name='Experience Level')),
                ('role', models.CharField(blank=True, max_length=100, null=True, verbose_name='Role')),
                ('industry', models.CharField(blank=True, max_length=100, null=True, verbose_name='Industry')),
                ('salary', models.CharField(blank=True, max_length=100, null=True, verbose_name='salary')),
                ('sponsor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sponsor')),
                ('paid', models.CharField(blank=True, max_length=100, null=True, verbose_name='Paid')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('link_apply', models.CharField(blank=True, max_length=800, null=True, verbose_name='Link to Apply')),
                ('url', models.CharField(blank=True, max_length=800, null=True, verbose_name='Url')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_company', to='company.Company', verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='JobCandidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jc_candidate', to='users_auth.Candidate', verbose_name='Candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jc_job', to='job.Job', verbose_name='Job')),
            ],
            options={
                'verbose_name': 'Job of Candidate',
                'verbose_name_plural': 'Jobs of Candidates',
            },
        ),
    ]
