# Generated by Django 4.0.6 on 2022-07-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0007_alter_service_created_alter_service_uploaded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='titulo',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(null=True, upload_to='services'),
        ),
    ]
