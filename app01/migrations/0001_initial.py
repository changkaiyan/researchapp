# Generated by Django 2.2 on 2020-08-08 09:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
            options={
                'verbose_name_plural': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Label',
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('duri', models.DurationField(default=None, verbose_name='During')),
                ('description', mdeditor.fields.MDTextField(default=None, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Meeting',
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Time')),
                ('date2', models.DateTimeField(auto_now=True, verbose_name='Modified Time')),
                ('content', mdeditor.fields.MDTextField(verbose_name='Description')),
                ('label', models.ManyToManyField(to='app01.Label')),
            ],
            options={
                'verbose_name_plural': 'Research',
            },
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('typ', models.CharField(choices=[('p', 'Paper'), ('b', 'Blog')], default=None, max_length=100)),
                ('proposed', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Time')),
                ('file', models.FileField(default=None, upload_to='', verbose_name='Attachment')),
                ('background', models.TextField(null=True, verbose_name='Background')),
                ('contribution', models.TextField(null=True, verbose_name='Contribution')),
                ('motivation', models.TextField(null=True, verbose_name='Motivation')),
                ('method', models.TextField(null=True, verbose_name='Method')),
                ('description', mdeditor.fields.MDTextField(default=None, verbose_name='Summary')),
            ],
            options={
                'verbose_name_plural': 'Summary',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, unique=True)),
                ('proposed', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create Time')),
                ('deadline', models.DateTimeField(default=None, verbose_name='Deadline')),
                ('realdeadline', models.DateTimeField(null=True, verbose_name='Finish Time')),
                ('description', mdeditor.fields.MDTextField(default=None, verbose_name='Description')),
                ('comment', models.ManyToManyField(to='app01.Comment')),
                ('typ', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app01.Research')),
            ],
            options={
                'verbose_name_plural': 'Task',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('_id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, unique=True)),
                ('file', models.FileField(default=None, upload_to='', verbose_name='Attachment')),
                ('motivation', models.TextField(null=True, verbose_name='Motivation')),
                ('method', models.TextField(null=True, verbose_name='Method')),
                ('description', mdeditor.fields.MDTextField(null=True, verbose_name='Description')),
                ('comment', models.ManyToManyField(to='app01.Comment')),
                ('typ', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app01.Research')),
            ],
            options={
                'verbose_name_plural': 'Project',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('_id', models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, unique=True)),
                ('file', models.FileField(default=None, upload_to='', verbose_name='Attachment')),
                ('contribution', models.TextField(null=True, verbose_name='Contribution')),
                ('motivation', models.TextField(null=True, verbose_name='Motivation')),
                ('method', models.TextField(null=True, verbose_name='Method')),
                ('experiment', mdeditor.fields.MDTextField(null=True, verbose_name='Experiment')),
                ('comment', models.ManyToManyField(to='app01.Comment')),
                ('typ', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app01.Research')),
            ],
            options={
                'verbose_name_plural': 'Paper',
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('abstract', models.CharField(default=None, max_length=100, verbose_name='Abstract')),
                ('question', models.TextField(default=None, verbose_name='Question')),
                ('answer', mdeditor.fields.MDTextField(default=None, verbose_name='Answer')),
                ('comment', models.ManyToManyField(to='app01.Comment')),
                ('toresearch', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app01.Research')),
            ],
            options={
                'verbose_name_plural': 'Knowledge',
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, unique=True)),
                ('description', mdeditor.fields.MDTextField(null=True, verbose_name='Description')),
                ('comment', models.ManyToManyField(to='app01.Comment')),
            ],
            options={
                'verbose_name_plural': 'Idea',
            },
        ),
    ]
