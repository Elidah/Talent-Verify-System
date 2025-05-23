# Generated by Django 5.2 on 2025-04-11 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registration_date', models.DateField()),
                ('registration_number', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('contact_person', models.CharField(max_length=255)),
                ('number_of_employees', models.IntegerField()),
                ('contact_phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('employee_id', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('date_started', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
                ('duties', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.company')),
            ],
        ),
    ]
