# Generated by Django 4.2.4 on 2023-09-01 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted_to_client',
            field=models.BooleanField(default=False),
        ),
    ]
