# Generated by Django 4.2.14 on 2024-08-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='users/', verbose_name='Аватар'),
        ),
    ]
