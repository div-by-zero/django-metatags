# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MetaTag'
        db.create_table('metatags_metatag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=250, blank=True)),
            ('index', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('archive', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('snippet', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('follow', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('metatags', ['MetaTag'])

        # Adding unique constraint on 'MetaTag', fields ['content_type', 'object_id']
        db.create_unique('metatags_metatag', ['content_type_id', 'object_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'MetaTag', fields ['content_type', 'object_id']
        db.delete_unique('metatags_metatag', ['content_type_id', 'object_id'])

        # Deleting model 'MetaTag'
        db.delete_table('metatags_metatag')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'metatags.metatag': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'MetaTag'},
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'follow': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'snippet': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['metatags']
