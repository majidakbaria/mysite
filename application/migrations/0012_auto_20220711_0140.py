# Generated by Django 3.2.13 on 2022-07-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='application.Category'),
        ),
    ]
