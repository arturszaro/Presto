# Generated by Django 3.2 on 2022-06-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrestoApp', '0007_auto_20220111_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemmenu',
            name='price3',
        ),
        migrations.AlterField(
            model_name='itemmenu',
            name='price2',
            field=models.IntegerField(default=0),
        ),
    ]
