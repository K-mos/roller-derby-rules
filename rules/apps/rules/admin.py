# -*- coding:utf-8 -*-
from django.contrib import admin
from models import *


class RuleAdmin(admin.ModelAdmin):
    list_display = ('section', 'number', 'content', 'creation', 'last_edition',)
    search_fields = ('number', 'content',)
    list_filter = ('section',)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('number', 'label', 'creation', 'last_edition',)
    search_fields = ('number', 'label',)
    list_filter = ('number',)


admin.site.register(Rule, RuleAdmin)
admin.site.register(Section, SectionAdmin)