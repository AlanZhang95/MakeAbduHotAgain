# Generated by Django 2.1.7 on 2019-03-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20190328_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tgt_weight',
            field=models.IntegerField(blank=True),
        ),
    ]