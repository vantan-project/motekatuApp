# Generated by Django 5.1.1 on 2024-09-21 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_review_img_path_review_gender_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='motekatu-app/'),
        ),
    ]
