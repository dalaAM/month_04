# Generated by Django 2.2.13 on 2020-08-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myfile', models.FileField(upload_to='myfile')),
            ],
        ),
    ]