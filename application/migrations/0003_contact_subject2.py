# Generated by Django 3.2.13 on 2022-07-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_contact_something'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject2',
            field=models.CharField(default='hi', max_length=240),
        ),
    ]
