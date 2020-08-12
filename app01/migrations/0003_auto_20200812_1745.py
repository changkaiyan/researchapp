# Generated by Django 2.2 on 2020-08-12 09:45

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20200808_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='description',
            field=mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='contribution',
            field=models.TextField(blank=True, null=True, verbose_name='Contribution'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='experiment',
            field=mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='Experiment'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='method',
            field=models.TextField(blank=True, null=True, verbose_name='Method'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='motivation',
            field=models.TextField(blank=True, null=True, verbose_name='Motivation'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=mdeditor.fields.MDTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='method',
            field=models.TextField(blank=True, null=True, verbose_name='Method'),
        ),
        migrations.AlterField(
            model_name='project',
            name='motivation',
            field=models.TextField(blank=True, null=True, verbose_name='Motivation'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='background',
            field=models.TextField(blank=True, null=True, verbose_name='Background'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='contribution',
            field=models.TextField(blank=True, null=True, verbose_name='Contribution'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='method',
            field=models.TextField(blank=True, null=True, verbose_name='Method'),
        ),
        migrations.AlterField(
            model_name='summary',
            name='motivation',
            field=models.TextField(blank=True, null=True, verbose_name='Motivation'),
        ),
        migrations.AlterField(
            model_name='task',
            name='realdeadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Finish Time'),
        ),
    ]
