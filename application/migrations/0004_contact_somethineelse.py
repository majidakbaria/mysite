# Generated by Django 3.2.13 on 2022-07-04 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_contact_subject2'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='somethineelse',
            field=models.CharField(default='hi', max_length=22),
        ),
    ]
