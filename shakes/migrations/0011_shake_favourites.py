# Generated by Django 5.0.6 on 2024-05-26 15:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakes', '0010_shake_categories'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shake',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favorite_shakes', to=settings.AUTH_USER_MODEL),
        ),
    ]
