from django.db import models
from mdeditor.fields import MDTextField
import django.utils.timezone as timezone
# Create your models here.


class Label(models.Model):
    lab = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Label'

    def __str__(self):
        return self.lab

class Comment(models.Model):
    comment = models.TextField(verbose_name="Comment")
    class Meta:
        verbose_name_plural = 'Comment'

class Research(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=150, verbose_name="Name")
    label = models.ManyToManyField(to='Label')
    date = models.DateTimeField('Create Time', default=timezone.now)
    date2 = models.DateTimeField('Modified Time', auto_now=True)
    content = MDTextField(verbose_name="Description")

    class Meta:
        verbose_name_plural = 'Research'


class Task(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(verbose_name="Name",max_length=100,unique=True, default=None)
    typ = models.ForeignKey(verbose_name="Type",to="Research",on_delete=models.CASCADE, default=None)
    proposed = models.DateTimeField('Create Time', default=timezone.now)
    deadline = models.DateTimeField('Deadline', null=False, default=None)
    realdeadline = models.DateTimeField("Finish Time", null=True)
    description = MDTextField(verbose_name="Description", default=None)
    comment = models.ManyToManyField(to="Comment")
    class Meta:
        verbose_name_plural = 'Task'


class Paper(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID", default=None)
    name = models.CharField(verbose_name="Name",max_length=100,unique=True, default=None)
    typ = models.ForeignKey(verbose_name="Type", to="Research",on_delete=models.CASCADE, default=None)
    file = models.FileField(verbose_name="Attachment", default=None)
    contribution = models.TextField(verbose_name="Contribution",null=True)
    motivation = models.TextField(verbose_name="Motivation",null=True)
    method = models.TextField(verbose_name="Method", null=True)
    experiment = MDTextField(verbose_name="Experiment",null=True)
    comment = models.ManyToManyField(verbose_name="Comment", to="Comment")
    class Meta:
        verbose_name_plural = 'Paper'


class Project(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID", default=None)
    name = models.CharField(verbose_name="Name", max_length=100,unique=True, default=None)
    typ = models.ForeignKey(verbose_name="Type", to="Research",on_delete=models.CASCADE, default=None)
    file = models.FileField(verbose_name="Attachment", default=None)
    motivation = models.TextField(verbose_name="Motivation",null=True)
    method = models.TextField(verbose_name="Method", null=True)
    description = MDTextField(verbose_name="Description",null=True)
    comment = models.ManyToManyField(to="Comment")
    class Meta:
        verbose_name_plural = 'Project'


class Idea(models.Model):
    idea_choice = [('ing', "Doing"), ('p', "Prepare"),('done',"Done")]
    name = models.CharField(verbose_name="Name",max_length=100,unique=True,default=None)
    description = MDTextField(verbose_name="Description",null=True)
    comment = models.ManyToManyField(verbose_name="Comment", to="Comment")
    class Meta:
        verbose_name_plural = 'Idea'
    def __str__(self):
        return self.name


class Knowledge(models.Model):
    _id = models.AutoField(primary_key=True, default=None)
    abstract = models.CharField(
        max_length=100, verbose_name="Abstract", default=None)
    question = models.TextField(verbose_name="Question", default=None)
    toresearch = models.ForeignKey(verbose_name="Research",
        to="Research", on_delete=models.CASCADE, default=None)
    answer = MDTextField(verbose_name="Answer", default=None)
    comment = models.ManyToManyField(to="Comment")
    class Meta:
        verbose_name_plural = 'Knowledge'


class Summary(models.Model):
    summ_choice = [('p', "Paper"), ('b', "Blog")]
    name = models.CharField(verbose_name="Name", max_length=100, default=None)
    typ = models.CharField(verbose_name="Type", max_length=100, choices=summ_choice, default=None)
    proposed = models.DateTimeField('Create Time', default=timezone.now)
    file = models.FileField(verbose_name="Attachment", default=None)
    background = models.TextField(verbose_name="Background",null=True)
    contribution = models.TextField(verbose_name="Contribution",null=True)
    motivation = models.TextField(verbose_name="Motivation",null=True)
    method = models.TextField(verbose_name="Method", null=True)
    description = MDTextField(verbose_name="Summary", default=None)
    class Meta:
        verbose_name_plural = 'Summary'


class Meeting(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100,default=None)
    duri = models.DurationField(verbose_name="During",default=None)
    description = MDTextField(verbose_name="Description",default=None)
    class Meta:
        verbose_name_plural = 'Meeting'
