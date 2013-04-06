# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Location.description'
        db.add_column('events_location', 'description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Location.description'
        db.delete_column('events_location', 'description')


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Location']"}),
            'plancast_id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'presentations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentations.Presentation']", 'null': 'True', 'blank': 'True'})
        },
        'events.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
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

    complete_apps = ['events']