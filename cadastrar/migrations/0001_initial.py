# Generated by Django 2.2.1 on 2019-05-16 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dt_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=100)),
                ('dt_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='Foto_produtos')),
                ('descricao', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrar.Categoria')),
                ('produtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastrar.Produtor')),
            ],
        ),
    ]
