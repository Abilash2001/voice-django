# Generated by Django 4.0.6 on 2022-09-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Email', models.TextField()),
                ('Feedback', models.TextField()),
            ],
        ),
    ]
