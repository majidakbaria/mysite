# Generated by Django 3.2.13 on 2022-07-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='f',
            field=models.CharField(default='hello', max_length=230),
        ),
    ]
