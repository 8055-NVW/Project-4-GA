# Generated by Django 5.0.6 on 2024-05-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
