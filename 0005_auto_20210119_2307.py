# Generated by Django 3.1.5 on 2021-01-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_movies_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='picture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
