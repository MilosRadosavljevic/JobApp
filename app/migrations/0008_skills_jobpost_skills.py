# Generated by Django 4.1.5 on 2023-01-31 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_author_jobpost_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='jobpost',
            name='skills',
            field=models.ManyToManyField(to='app.skills'),
        ),
    ]
