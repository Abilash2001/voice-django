# Generated by Django 4.0.6 on 2022-09-27 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plan_price', models.TextField()),
                ('plan_talktime', models.TextField()),
                ('plan_data', models.TextField()),
                ('plan_validity', models.TextField()),
                ('plan_usage', models.IntegerField()),
            ],
        ),
    ]
