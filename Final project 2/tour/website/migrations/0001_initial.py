# Generated by Django 5.0.6 on 2024-05-29 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listtour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('departure_date', models.CharField(max_length=100)),
                ('accomodation', models.CharField(max_length=100)),
                ('transportation', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('activities', models.CharField(max_length=500)),
                ('climate', models.CharField(max_length=100)),
            ],
        ),
    ]
