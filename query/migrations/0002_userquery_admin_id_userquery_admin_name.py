# Generated by Django 4.0.6 on 2022-10-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquery',
            name='admin_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userquery',
            name='admin_name',
            field=models.TextField(default='Abilash'),
            preserve_default=False,
        ),
    ]
