# Generated by Django 2.1.7 on 2019-03-28 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0006_auto_20190327_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('goal', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('carb', models.IntegerField()),
                ('fiber', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('foodID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.food_table')),
                ('planID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.DietPlan')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='undefined', max_length=20)),
                ('height', models.IntegerField()),
                ('age', models.IntegerField()),
                ('cur_weight', models.IntegerField()),
                ('tgt_weight', models.IntegerField()),
                ('is_cook', models.BooleanField()),
                ('plan', models.IntegerField()),
                ('total_cal', models.IntegerField()),
                ('carb', models.IntegerField()),
                ('fib', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dietplan',
            name='foods',
            field=models.ManyToManyField(through='database.GeneratedBy', to='database.food_table'),
        ),
        migrations.AddField(
            model_name='dietplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.UserProfile'),
        ),
    ]
