# Generated by Django 5.0 on 2023-12-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
