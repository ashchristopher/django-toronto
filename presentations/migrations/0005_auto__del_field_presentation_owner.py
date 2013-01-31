# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Presentation.owner'
        db.delete_column('presentations_presentation', 'owner_id')


    def backwards(self, orm):
        # Adding field 'Presentation.owner'
        db.add_column('presentations_presentation', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)


    models = {
        'presentations.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'embed_code': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oembed': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['presentations']