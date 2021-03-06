# Generated by Django 3.0.6 on 2020-05-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advuser',
            name='is_activated',
            field=models.BooleanField(default=True, verbose_name='came through activation?'),
        ),
        migrations.AddField(
            model_name='advuser',
            name='send_messages',
            field=models.BooleanField(default=True, verbose_name='inform about our hot offers?'),
        ),
    ]
