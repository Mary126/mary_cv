# Generated by Django 4.1.4 on 2022-12-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_project_github_link_alter_image_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.FileField(blank=True, upload_to='database/files', verbose_name='Файл'),
        ),
    ]
