# Generated by Django 4.0.3 on 2022-06-18 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbateros', '0004_alter_post_contenido'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
    ]
