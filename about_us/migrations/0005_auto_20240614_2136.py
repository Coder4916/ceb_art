# Generated by Django 3.2.25 on 2024-06-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0004_rename_reviews_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('username', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='username',
        ),
    ]
