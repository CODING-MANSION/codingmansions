# Generated by Django 3.2.2 on 2021-05-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='playlist',
            field=models.CharField(default='', max_length=100),
        ),
    ]
