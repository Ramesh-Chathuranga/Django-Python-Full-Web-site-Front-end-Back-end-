# Generated by Django 2.2.2 on 2019-06-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miriapp', '0002_auto_20190611_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]