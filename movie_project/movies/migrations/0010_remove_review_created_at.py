# Generated by Django 4.2.11 on 2024-05-22 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created_at',
        ),
    ]
