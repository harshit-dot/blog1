# Generated by Django 3.1.3 on 2020-12-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20201213_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='', upload_to='app1/images/'),
        ),
    ]
