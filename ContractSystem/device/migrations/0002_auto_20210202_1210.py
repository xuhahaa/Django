# Generated by Django 2.1.7 on 2021-02-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Device',
        ),
    ]
