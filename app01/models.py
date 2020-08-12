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

class TaskComment(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID")
    comment = models.TextField(verbose_name="Comment")
    point = models.ForeignKey(verbose_name="Task", to="Task", on_delete=models.CASCADE)
    def __str__(self):
        return "Task Comment: "+"{}".format(self._id)
    class Meta:
        verbose_name_plural = 'Comment'

class PaperComment(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID")
    comment = models.TextField(verbose_name="Comment")
    point = models.ForeignKey(verbose_name="Paper", to="Paper",on_delete=models.CASCADE)
    def __str__(self):
        return "Task Comment: "+"{}".format(self._id)
    class Meta:
        verbose_name_plural = 'Comment'

class ProjectComment(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID")
    comment = models.TextField(verbose_name="Comment")
    point = models.ForeignKey(verbose_name="Project", to="Project",on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Comment'
    def __str__(self):
        return "Task Comment: "+"{}".format(self._id)

class Research(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=150, verbose_name="Name")
    label = models.ManyToManyField(to='Label')
    date = models.DateTimeField('Create Time', default=timezone.now)
    date2 = models.DateTimeField('Modified Time', auto_now=True)
    content = MDTextField(verbose_name="Description")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Research'


class Task(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(verbose_name="Name",max_length=100,unique=True, default=None)
    typ = models.ForeignKey(verbose_name="Type",to="Research",on_delete=models.CASCADE, default=None)
    proposed = models.DateTimeField('Create Time', default=timezone.now)
    deadline = models.DateTimeField('Deadline', null=False, default=None)
    realdeadline = models.DateTimeField("Finish Time", null=True, blank=True)
    description = MDTextField(verbose_name="Description", default=None)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Task'


class Paper(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID", default=None)
    name = models.CharField(verbose_name="Name",max_length=100,unique=True, default=None)
    typ = models.ForeignKey(verbose_name="Type", to="Research",on_delete=models.CASCADE, default=None)
    file = models.FileField(verbose_name="Attachment", default=None,null=True, blank=True,upload_to='paper')
    contribution = models.TextField(verbose_name="Contribution",null=True, blank=True)
    motivation = models.TextField(verbose_name="Motivation",null=True, blank=True)
    method = models.TextField(verbose_name="Method", null=True, blank=True)
    experiment = MDTextField(verbose_name="Experiment",null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Paper'


class Project(models.Model):
    _id = models.AutoField(primary_key=True, verbose_name="ID", default=None)
    name = models.CharField(verbose_name="Name", max_length=100,unique=True, default=None)
    typ = models.ForeignKey(verbose_name="Type", to="Research",on_delete=models.CASCADE, default=None)
    file = models.FileField(verbose_name="Attachment", default=None,null=True, blank=True)
    motivation = models.TextField(verbose_name="Motivation",null=True, blank=True)
    method = models.TextField(verbose_name="Method", null=True, blank=True)
    description = MDTextField(verbose_name="Description",null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Project'


class Idea(models.Model):
    idea_choice = [('ing', "Doing"), ('p', "Prepare"),('done',"Done")]
    name = models.CharField(verbose_name="Name",max_length=100,unique=True,default=None)
    description = MDTextField(verbose_name="Description",null=True, blank=True)
    comment = MDTextField(verbose_name="Comment",null=True, blank=True)
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
    comment = MDTextField(verbose_name="Comment",null=True, blank=True)
    def __str__(self):
        return self.abstract
    class Meta:
        verbose_name_plural = 'Knowledge'


class Summary(models.Model):
    summ_choice = [('p', "Paper"), ('b', "Blog")]
    name = models.CharField(verbose_name="Name", max_length=100, default=None)
    typ = models.CharField(verbose_name="Type", max_length=100, choices=summ_choice, default=None)
    proposed = models.DateTimeField('Create Time', default=timezone.now)
    file = models.FileField(verbose_name="Attachment", default=None, blank=True)
    background = models.TextField(verbose_name="Background",null=True, blank=True)
    contribution = models.TextField(verbose_name="Contribution",null=True, blank=True)
    motivation = models.TextField(verbose_name="Motivation",null=True, blank=True)
    method = models.TextField(verbose_name="Method", null=True, blank=True)
    description = MDTextField(verbose_name="Summary", default=None)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Summary'


class Meeting(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100,default=None)
    start = models.DateTimeField(verbose_name="Start Time",default=None)
    end = models.DateTimeField(verbose_name="End Time",default=None)
    description = MDTextField(verbose_name="Description",default=None,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Meeting'

