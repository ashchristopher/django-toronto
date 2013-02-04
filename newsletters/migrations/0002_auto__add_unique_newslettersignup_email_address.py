# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'NewsletterSignup', fields ['active']
        db.create_index('newsletters_newslettersignup', ['active'])

        # Adding unique constraint on 'NewsletterSignup', fields ['email_address']
        db.create_unique('newsletters_newslettersignup', ['email_address'])


    def backwards(self, orm):
        # Removing unique constraint on 'NewsletterSignup', fields ['email_address']
        db.delete_unique('newsletters_newslettersignup', ['email_address'])

        # Removing index on 'NewsletterSignup', fields ['active']
        db.delete_index('newsletters_newslettersignup', ['active'])


    models = {
        'newsletters.newslettersignup': {
            'Meta': {'unique_together': "(('email_address',),)", 'object_name': 'NewsletterSignup'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['newsletters']