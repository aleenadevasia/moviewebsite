# Generated by Django 4.2.11 on 2024-05-21 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_last_name'),
        ('movies', '0004_alter_movie_added_by_alter_movie_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_movies', to='users.customuser'),
        ),
    ]
