# Generated by Django 5.0.6 on 2024-05-25 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakes', '0007_alter_shake_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shake',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
