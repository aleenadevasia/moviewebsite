# Generated by Django 4.2.11 on 2024-05-21 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_last_name'),
        ('movies', '0003_alter_movie_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='added_movies', to='users.customuser'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
