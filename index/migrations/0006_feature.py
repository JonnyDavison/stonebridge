# Generated by Django 4.1.13 on 2024-08-29 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_gallery_gallery_image11_gallery_gallery_image12'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_title', models.TextField()),
                ('feature_sub_title', models.TextField()),
                ('feature_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Feature',
            },
        ),
    ]
