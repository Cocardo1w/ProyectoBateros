# Generated by Django 4.0.3 on 2022-06-16 21:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appbateros', '0003_post_delete_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
