# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Presentation.twitter_handle'
        db.add_column('presentations_presentation', 'twitter_handle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=75, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Presentation.twitter_handle'
        db.delete_column('presentations_presentation', 'twitter_handle')


    models = {
        'presentations.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'embed_code': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oembed': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'twitter_handle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['presentations']