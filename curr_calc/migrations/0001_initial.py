# Generated by Django 3.1.3 on 2020-12-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pswd', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
