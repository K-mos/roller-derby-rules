# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Rule', fields ['number']
        db.create_unique(u'rules_rule', ['number'])

        # Adding unique constraint on 'Section', fields ['number']
        db.create_unique(u'rules_section', ['number'])


    def backwards(self, orm):
        # Removing unique constraint on 'Section', fields ['number']
        db.delete_unique(u'rules_section', ['number'])

        # Removing unique constraint on 'Rule', fields ['number']
        db.delete_unique(u'rules_rule', ['number'])


    models = {
        u'rules.rule': {
            'Meta': {'ordering': "['number']", 'object_name': 'Rule'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edition': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rules.Section']", 'null': 'True', 'blank': 'True'})
        },
        u'rules.section': {
            'Meta': {'ordering': "['number']", 'object_name': 'Section'},
            'creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_edition': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'})
        }
    }

    complete_apps = ['rules']