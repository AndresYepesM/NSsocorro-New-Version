# Generated by Django 3.1.3 on 2020-12-12 12:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20201212_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membersprofile',
            name='bio',
            field=ckeditor.fields.RichTextField(),
        ),
    ]