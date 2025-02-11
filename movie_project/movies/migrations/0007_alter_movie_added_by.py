# Generated by Django 4.2.11 on 2024-05-22 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_remove_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
