# Generated by Django 3.2.25 on 2024-06-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0009_auto_20240625_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
