# Generated by Django 4.0.6 on 2022-07-27 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_remove_service_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='titulo',
        ),
    ]
