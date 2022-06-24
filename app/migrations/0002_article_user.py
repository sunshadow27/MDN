# Generated by Django 3.1.5 on 2021-03-19 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('path', models.CharField(max_length=64)),
                ('classes', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('sex', models.CharField(max_length=2)),
                ('point', models.IntegerField()),
                ('status', models.IntegerField()),
                ('head_portrait', models.CharField(max_length=64)),
                ('juris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usertype')),
            ],
        ),
    ]
