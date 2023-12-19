# Generated by Django 3.2.23 on 2023-12-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20231212_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_bio',
            field=models.TextField(blank=True, help_text='Text input required, (max is length 255 characters)', max_length=255, verbose_name='Game Bio:'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_company',
            field=models.CharField(help_text='Text input required, (max is length 255 characters)', max_length=255, null=True, verbose_name='Game Company:'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(help_text='Text input required, (max is length 255 characters)', max_length=255, null=True, verbose_name='Game Name:'),
        ),
    ]