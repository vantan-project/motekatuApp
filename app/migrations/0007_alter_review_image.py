# Generated by Django 5.1.1 on 2024-09-23 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
