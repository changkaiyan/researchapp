from django.contrib import admin
from django.db import models
from django import forms
from django.forms import Textarea, TextInput
from .models import *
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import Group, User

# Register your models here.
from openpyxl import Workbook
admin.site.site_url = None  # Remove the view site hyper link


class NoDisplay(admin.ModelAdmin):
    def get_model_perms(self, request):  # Hiden the model while register it.
        return {}


class Canexcel(admin.ModelAdmin):  # Derive from this can export an excel file
    actions = ["export_as_excel"]

    def export_as_excel(self, request, queryset):
        print("queryset", queryset)
        meta = self.model._meta  
        print("meta", meta)
        field_names = [field.name for field in meta.fields]  
        response = HttpResponse(content_type='application/msexcel')  
        response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
        wb = Workbook()  
        ws = wb.active  
        ws.append(field_names)  
        for obj in queryset: 
            print(obj)
            for field in field_names:
                data = [f'{getattr(obj, field)}' for field in field_names]
            ws.append(data)  
        wb.save(response)  
        return response

    export_as_excel.short_description = 'Export excel'  # Display verbose_name


class TaskCommentInline(admin.TabularInline):
    model = TaskComment


class PaperCommentInline(admin.TabularInline):
    model = PaperComment


class ProjectCommentInline(admin.TabularInline):
    model = ProjectComment


class ResearchAdmin(Canexcel):
    list_display = ('_id', 'name', 'Label', 'date')
    search_fields = ['name', 'content']
    list_filter = ['label']

    def Label(self, obj):  # Get the labels from manytomany field.
        return [bt.lab for bt in obj.label.all()]

class KnowledgeAdmin(Canexcel):
    list_display = ('_id', 'abstract')
    search_fields = ['abstract', 'question']
    list_filter = ['toresearch']

class PaperAdmin(Canexcel):
    list_display = ('_id', 'name',"typ")
    search_fields = ['name', 'typ',"contribution","motivation","method"]
    list_filter = ['typ']
    inlines = [PaperCommentInline,]

class ProjectAdmin(Canexcel):
    list_display = ('_id', 'name',"typ")
    search_fields = ['name', 'typ',"contribution","motivation","method"]
    list_filter = ['typ']
    inlines = [ProjectCommentInline,]

class MeetingAdmin(Canexcel):
    list_display = ('name', 'start', 'end')
    search_fields = ['name', 'duri', 'end']

class SummaryAdmin(Canexcel):
    list_display = ('name', "typ")
    search_fields = ['name', 'typ',"contribution","motivation","method"]
    list_filter = ['typ']

class TaskAdmin(Canexcel):
    list_display = ("_id", 'name', "typ","deadline")
    search_fields = ["_id", 'name', "typ","deadline"]
    list_filter = ['typ']
    inlines = [TaskCommentInline,]

class IdeaAdmin(Canexcel):
    search_fields = ['name']

admin.site.register(Research, ResearchAdmin)
admin.site.register(Label)
admin.site.register(Knowledge, KnowledgeAdmin)
admin.site.register(Paper, PaperAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Summary, SummaryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Idea, IdeaAdmin)