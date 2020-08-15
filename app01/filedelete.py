from django.db.models.signals import post_init, post_save, pre_delete
from django.dispatch.dispatcher import receiver
import os
from sitep.settings import MEDIA_ROOT
from .models import Paper, Project, Summary


@receiver(post_init, sender=Paper)
def welcom_paper(instance, **kwargs):
    instance._file = instance.file


@receiver(post_save, sender=Paper)
def welcome_paper(instance, created, **kwargs):
    if not created and instance._file != instance.file:
        fname = os.path.join(MEDIA_ROOT, instance._file)
        if os.path.isfile(fname):
            os.remove(fname)
        instance._file = instance.file


@receiver(post_init, sender=Project)
def welcom_project(instance, **kwargs):
    instance._file = instance.file


@receiver(post_save, sender=Project)
def welcome_project(instance, created, **kwargs):
    if not created and instance._file != instance.file:
        fname = os.path.join(MEDIA_ROOT, instance._file)
        if os.path.isfile(fname):
            os.remove(fname)
        instance._file = instance.file


@receiver(post_init, sender=Summary)
def welcom_summary(instance, **kwargs):
    instance._file = instance.file


@receiver(post_save, sender=Summary)
def welcome_summary(instance, created, **kwargs):
    if not created and instance._file != instance.file:
        fname = os.path.join(MEDIA_ROOT, instance._file)
        if os.path.isfile(fname):
            os.remove(fname)
        instance._file = instance.file

@receiver(pre_delete, sender=Paper)
def filedelete_paper(sender, instance, **kwargs):
    instance.file.delete(False)

@receiver(pre_delete, sender=Project)
def filedelete_paper(sender, instance, **kwargs):
    instance.file.delete(False)

@receiver(pre_delete, sender=Summary)
def filedelete_paper(sender, instance, **kwargs):
    instance.file.delete(False)