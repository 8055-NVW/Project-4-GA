# Generated by Django 5.0.6 on 2024-05-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1, null=True),
        ),
    ]