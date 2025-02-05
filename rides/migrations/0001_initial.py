# Generated by Django 5.1.5 on 2025-01-19 15:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_location', models.CharField(max_length=255)),
                ('dropoff_location', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('accepted', 'Accepted'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='requested', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rides_driven', to=settings.AUTH_USER_MODEL)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rides_requested', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
