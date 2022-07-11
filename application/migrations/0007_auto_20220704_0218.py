# Generated by Django 3.2.13 on 2022-07-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_rename_contact_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='counted_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]