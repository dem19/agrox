# Generated by Django 2.2.1 on 2019-09-10 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar', '0011_usuarioperfil_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarioperfil',
            name='user',
        ),
    ]
