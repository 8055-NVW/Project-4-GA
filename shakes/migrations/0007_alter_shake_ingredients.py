# Generated by Django 5.0.6 on 2024-05-25 16:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakes', '0006_alter_shake_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shake',
            name='ingredients',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None),
        ),
    ]