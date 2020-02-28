# Generated by Django 2.2 on 2020-02-27 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200227_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favorites',
        ),
        migrations.CreateModel(
            name='favoriteTrail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_id', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='main_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='completedTrail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_id', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completed', to='main_app.User')),
            ],
        ),
    ]
