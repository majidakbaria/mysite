# Generated by Django 3.2.13 on 2022-07-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='something',
            field=models.CharField(default='hello', max_length=230),
        ),
    ]
