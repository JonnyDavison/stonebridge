# Generated by Django 5.1.1 on 2024-09-12 16:23

import django_summernote.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]
