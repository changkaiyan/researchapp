# Generated by Django 2.2 on 2020-08-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_auto_20200815_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='_file',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
