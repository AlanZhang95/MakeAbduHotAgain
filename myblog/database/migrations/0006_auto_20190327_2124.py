# Generated by Django 2.1.7 on 2019-03-27 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_food_table_sourcetpye'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food_table',
            old_name='SourceTpye',
            new_name='SourceType',
        ),
    ]
