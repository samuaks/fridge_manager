# Generated by Django 3.0.3 on 2020-04-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridges', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewFridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
    ]