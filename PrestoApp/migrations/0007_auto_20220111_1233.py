# Generated by Django 3.2 on 2022-01-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrestoApp', '0006_auto_20220111_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmenu',
            name='ingredients',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itemmenu',
            name='number',
            field=models.IntegerField(),
        ),
    ]