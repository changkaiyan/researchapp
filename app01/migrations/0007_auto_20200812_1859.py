# Generated by Django 2.2 on 2020-08-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20200812_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='', verbose_name='Attachment'),
        ),
    ]
