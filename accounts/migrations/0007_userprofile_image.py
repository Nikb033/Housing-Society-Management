# Generated by Django 3.0.5 on 2020-04-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
