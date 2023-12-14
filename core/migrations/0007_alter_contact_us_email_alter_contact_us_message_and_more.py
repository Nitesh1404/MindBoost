# Generated by Django 5.0 on 2023-12-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_contact_us_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
