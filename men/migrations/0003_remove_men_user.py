# Generated by Django 4.1 on 2022-10-03 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0002_alter_category_options_alter_men_options_men_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='men',
            name='user',
        ),
    ]
