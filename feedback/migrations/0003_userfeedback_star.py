# Generated by Django 4.0.6 on 2022-09-27 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_userfeedback_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfeedback',
            name='Star',
            field=models.CharField(default='5', max_length=1),
            preserve_default=False,
        ),
    ]
