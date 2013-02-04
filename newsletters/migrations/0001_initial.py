# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsletterSignup'
        db.create_table('newsletters_newslettersignup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('newsletters', ['NewsletterSignup'])


    def backwards(self, orm):
        # Deleting model 'NewsletterSignup'
        db.delete_table('newsletters_newslettersignup')


    models = {
        'newsletters.newslettersignup': {
            'Meta': {'object_name': 'NewsletterSignup'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['newsletters']