# Generated by Django 4.0.6 on 2022-09-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.TextField()),
                ('planId', models.TextField()),
            ],
        ),
    ]
