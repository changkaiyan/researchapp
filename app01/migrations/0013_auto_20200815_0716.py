# Generated by Django 2.2 on 2020-08-14 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_auto_20200814_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='paper', verbose_name='Attachment')),
            ],
            options={
                'verbose_name_plural': 'Attachment',
            },
        ),
        migrations.RemoveField(
            model_name='paper',
            name='file',
        ),
    ]
