# Generated by Django 5.1.1 on 2025-01-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0027_home_address_home_business_name_home_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='facebook',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='instagram',
            field=models.TextField(blank=True, null=True),
        ),
    ]
