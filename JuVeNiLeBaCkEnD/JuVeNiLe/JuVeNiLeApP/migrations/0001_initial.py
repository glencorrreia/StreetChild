# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-26 21:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorizedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChildCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChildGender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CriminalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('schoolAdmission', models.BooleanField()),
                ('schoolName', models.CharField(blank=True, max_length=255, null=True)),
                ('criminalRecord', models.BooleanField()),
                ('locationOfChild', models.TextField(blank=True, null=True)),
                ('parentsEmployment', models.BooleanField()),
                ('parentsLocationOfWork', models.TextField(blank=True, null=True)),
                ('income', models.IntegerField(blank=True, null=True)),
                ('criminalRecordDescription', models.TextField(blank=True, null=True)),
                ('medicalRecord', models.BooleanField()),
                ('medicalRecordDescription', models.TextField(blank=True, null=True)),
                ('imageOfChild1', models.ImageField(blank=True, null=True, upload_to='')),
                ('imageOfChild2', models.ImageField(blank=True, null=True, upload_to='')),
                ('imageOfChild3', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JuVeNiLeApP.ChildCategory')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JuVeNiLeApP.ChildGender')),
            ],
        ),
        migrations.CreateModel(
            name='LostAndFound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gaurdianName', models.CharField(blank=True, max_length=255, null=True)),
                ('schoolAdmission', models.BooleanField()),
                ('schoolName', models.CharField(blank=True, max_length=255, null=True)),
                ('locationOfChildLost', models.TextField(blank=True, null=True)),
                ('locationToContact', models.TextField(blank=True, null=True)),
                ('gaurdianContactNumber', models.IntegerField(blank=True, null=True)),
                ('imageOfChild1', models.ImageField(blank=True, null=True, upload_to='')),
                ('imageOfChild2', models.ImageField(blank=True, null=True, upload_to='')),
                ('imageOfChild3', models.ImageField(blank=True, null=True, upload_to='')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JuVeNiLeApP.ChildGender')),
            ],
        ),
        migrations.CreateModel(
            name='PendingUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredChildren',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('schoolAdmission', models.BooleanField()),
                ('schoolName', models.CharField(blank=True, max_length=255, null=True)),
                ('criminalRecord', models.BooleanField()),
                ('locationOfChild', models.TextField(blank=True, null=True)),
                ('childFoundTime', models.DateTimeField(blank=True, null=True)),
                ('parentsEmployment', models.BooleanField()),
                ('parentsLocationOfWork', models.TextField(blank=True, null=True)),
                ('income', models.IntegerField(blank=True, null=True)),
                ('imageOfChild', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JuVeNiLeApP.ChildCategory')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JuVeNiLeApP.ChildGender')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='JuVeNiLeApP.AuthorizedUsers')),
            ],
        ),
    ]