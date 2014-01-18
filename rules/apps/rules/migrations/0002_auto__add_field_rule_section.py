# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Rule.section'
        db.add_column(u'rules_rule', 'section',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rules.Section'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Rule.section'
        db.delete_column(u'rules_rule', 'section_id')


    models = {
        u'rules.rule': {
            'Meta': {'ordering': "['number']", 'object_name': 'Rule'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_edition': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rules.Section']", 'null': 'True', 'blank': 'True'})
        },
        u'rules.section': {
            'Meta': {'ordering': "['number']", 'object_name': 'Section'},
            'creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_edition': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['rules']