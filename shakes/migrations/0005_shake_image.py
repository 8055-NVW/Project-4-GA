# Generated by Django 5.0.6 on 2024-05-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakes', '0004_alter_shake_instructions'),
    ]

    operations = [
        migrations.AddField(
            model_name='shake',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shakes/images/'),
        ),
    ]
