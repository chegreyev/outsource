# Generated by Django 3.0.4 on 2020-03-17 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='bank_card',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employees',
            name='iin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employees',
            name='udv_number',
            field=models.IntegerField(),
        ),
    ]