# Generated by Django 4.1.5 on 2023-02-02 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]