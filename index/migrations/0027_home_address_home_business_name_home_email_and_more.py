# Generated by Django 5.1.1 on 2025-01-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0026_home_description_home_google_site_verification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='business_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='phone_number',
            field=models.TextField(blank=True, null=True),
        ),
    ]