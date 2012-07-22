# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactUsMessage'
        db.create_table('contact_us_contactusmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('submitter_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('contact_us', ['ContactUsMessage'])

        # Adding model 'BannedIp'
        db.create_table('contact_us_bannedip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('banned_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('contact_us', ['BannedIp'])


    def backwards(self, orm):
        # Deleting model 'ContactUsMessage'
        db.delete_table('contact_us_contactusmessage')

        # Deleting model 'BannedIp'
        db.delete_table('contact_us_bannedip')


    models = {
        'contact_us.bannedip': {
            'Meta': {'object_name': 'BannedIp'},
            'banned_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contact_us.contactusmessage': {
            'Meta': {'object_name': 'ContactUsMessage'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'submitter_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['contact_us']