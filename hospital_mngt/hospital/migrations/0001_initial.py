# Generated by Django 3.2.8 on 2022-01-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('Specialist', models.CharField(max_length=50)),
            ],
        ),
    ]
