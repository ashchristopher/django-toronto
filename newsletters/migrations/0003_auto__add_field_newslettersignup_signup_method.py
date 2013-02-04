# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewsletterSignup.signup_method'
        db.add_column('newsletters_newslettersignup', 'signup_method',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewsletterSignup.signup_method'
        db.delete_column('newsletters_newslettersignup', 'signup_method')


    models = {
        'newsletters.newslettersignup': {
            'Meta': {'unique_together': "(('email_address',),)", 'object_name': 'NewsletterSignup'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signup_method': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '16'})
        }
    }

    complete_apps = ['newsletters']