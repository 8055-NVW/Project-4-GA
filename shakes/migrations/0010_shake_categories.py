# Generated by Django 5.0.6 on 2024-05-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('shakes', '0009_remove_shake_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='shake',
            name='categories',
            field=models.ManyToManyField(related_name='shakes', to='categories.category'),
        ),
    ]
