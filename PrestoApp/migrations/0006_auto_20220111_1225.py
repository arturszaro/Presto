# Generated by Django 3.2 on 2022-01-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrestoApp', '0005_auto_20220111_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmenu',
            name='size',
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='number',
            field=models.IntegerField(default=0, max_length=256),
            preserve_default=False,
        ),
    ]
