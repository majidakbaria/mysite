# Generated by Django 3.2.13 on 2022-07-05 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_f'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='f',
        ),
    ]