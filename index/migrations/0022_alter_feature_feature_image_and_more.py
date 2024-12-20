# Generated by Django 5.1.1 on 2024-11-05 00:58

import custom_storages
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_alter_service_options_service_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image1',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image10',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image11',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image12',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image2',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image3',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image4',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image5',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image6',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image7',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image8',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image9',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='home',
            name='hero_image',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='home',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=custom_storages.MediaStorage(), upload_to=''),
        ),
    ]
