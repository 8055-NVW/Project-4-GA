# Generated by Django 5.0.6 on 2024-05-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_diets'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
