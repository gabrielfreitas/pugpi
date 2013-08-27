# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table('multimidia_album', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('foto_destaque', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100, blank=True)),
            ('creditos', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('publicado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('cadastrado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('multimidia', ['Album'])

        # Adding model 'Foto'
        db.create_table('multimidia_foto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['multimidia.Album'])),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('legenda', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cadastrado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('multimidia', ['Foto'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table('multimidia_album')

        # Deleting model 'Foto'
        db.delete_table('multimidia_foto')


    models = {
        'multimidia.album': {
            'Meta': {'ordering': "('-cadastrado_em',)", 'object_name': 'Album'},
            'cadastrado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creditos': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'foto_destaque': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publicado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'multimidia.foto': {
            'Meta': {'ordering': "('-cadastrado_em',)", 'object_name': 'Foto'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['multimidia.Album']"}),
            'cadastrado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legenda': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['multimidia']