# Generated by Django 4.2.9 on 2024-06-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_actors_movie_description_movie_youtubelink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movieduration',
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(default='casting', max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(default='about the movie...', max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='youtubelink',
            field=models.CharField(default='youtube link here', max_length=100),
        ),
    ]
