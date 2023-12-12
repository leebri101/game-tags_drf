# Generated by Django 3.2.23 on 2023-12-12 12:59

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at:')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated at:')),
                ('user_name', models.CharField(help_text='format: required, max_length=100', max_length=100, null=True, verbose_name='Username:')),
                ('first_name', models.CharField(help_text='format: not required, max_length=150', max_length=150, null=True, verbose_name='First Name:')),
                ('last_name', models.CharField(help_text='format: not required, max_length=150', max_length=150, null=True, verbose_name='Last Name:')),
                ('bio', models.TextField(blank=True, help_text='format: not required, max_length=255', max_length=255, verbose_name='Bio:')),
                ('avatar', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='avatar')),
                ('favourite_games', models.ManyToManyField(blank=True, related_name='profile', to='games.Game')),
                ('user', models.OneToOneField(help_text='format: required, unique=True', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]