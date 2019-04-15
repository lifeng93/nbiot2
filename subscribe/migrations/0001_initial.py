# Generated by Django 2.1.4 on 2018-12-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceId', models.CharField(max_length=100)),
                ('temperature', models.IntegerField()),
                ('eventTime', models.DateTimeField()),
            ],
        ),
    ]