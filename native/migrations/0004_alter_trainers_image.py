# Generated by Django 4.0.4 on 2022-05-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('native', '0003_gallery_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainers',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]
