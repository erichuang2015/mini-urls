# Generated by Django 2.1.2 on 2018-10-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='hits',
            field=models.IntegerField(),
        ),
    ]
