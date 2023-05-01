# Generated by Django 4.1.5 on 2023-02-05 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0004_subscribe_option_alter_subscribe_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='M', max_length=2),
        ),
    ]
