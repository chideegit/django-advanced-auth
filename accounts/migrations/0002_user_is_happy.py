# Generated by Django 5.0.3 on 2024-03-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_happy',
            field=models.BooleanField(default=True),
        ),
    ]
