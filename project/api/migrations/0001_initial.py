# Generated by Django 3.0.4 on 2020-03-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('iin', models.IntegerField(max_length=12)),
                ('udv_number', models.IntegerField(max_length=8)),
                ('udv_place', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('bank_card', models.IntegerField(max_length=12)),
                ('iban', models.CharField(max_length=20)),
                ('contact_phone', models.CharField(max_length=20)),
                ('email_address', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_hr', models.BooleanField(default=False)),
            ],
        ),
    ]
