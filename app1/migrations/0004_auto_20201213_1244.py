# Generated by Django 3.1.3 on 2020-12-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_blogpost_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='photoes'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
