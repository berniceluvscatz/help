# Generated by Django 3.1.5 on 2021-01-20 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20210120_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='picture',
        ),
    ]
