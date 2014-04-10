# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Liga'
        db.create_table(u'app_liga', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Liga'])

        # Adding model 'Equipo'
        db.create_table(u'app_equipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Equipo'])

        # Adding model 'Entrenador'
        db.create_table(u'app_entrenador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Equipo'])),
        ))
        db.send_create_signal(u'app', ['Entrenador'])

        # Adding M2M table for field amigos on 'Entrenador'
        m2m_table_name = db.shorten_name(u'app_entrenador_amigos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_entrenador', models.ForeignKey(orm[u'app.entrenador'], null=False)),
            ('to_entrenador', models.ForeignKey(orm[u'app.entrenador'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_entrenador_id', 'to_entrenador_id'])

        # Adding model 'Jugador'
        db.create_table(u'app_jugador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellido_paterno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellido_materno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('correo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')()),
            ('equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Equipo'])),
        ))
        db.send_create_signal(u'app', ['Jugador'])

        # Adding M2M table for field amigos on 'Jugador'
        m2m_table_name = db.shorten_name(u'app_jugador_amigos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_jugador', models.ForeignKey(orm[u'app.jugador'], null=False)),
            ('to_jugador', models.ForeignKey(orm[u'app.jugador'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_jugador_id', 'to_jugador_id'])

        # Adding model 'Publicacion'
        db.create_table(u'app_publicacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contenido', self.gf('django.db.models.fields.CharField')(max_length=450)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app', ['Publicacion'])

        # Adding model 'Queja'
        db.create_table(u'app_queja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contenido', self.gf('django.db.models.fields.CharField')(max_length=450)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app', ['Queja'])


    def backwards(self, orm):
        # Deleting model 'Liga'
        db.delete_table(u'app_liga')

        # Deleting model 'Equipo'
        db.delete_table(u'app_equipo')

        # Deleting model 'Entrenador'
        db.delete_table(u'app_entrenador')

        # Removing M2M table for field amigos on 'Entrenador'
        db.delete_table(db.shorten_name(u'app_entrenador_amigos'))

        # Deleting model 'Jugador'
        db.delete_table(u'app_jugador')

        # Removing M2M table for field amigos on 'Jugador'
        db.delete_table(db.shorten_name(u'app_jugador_amigos'))

        # Deleting model 'Publicacion'
        db.delete_table(u'app_publicacion')

        # Deleting model 'Queja'
        db.delete_table(u'app_queja')


    models = {
        u'app.entrenador': {
            'Meta': {'object_name': 'Entrenador'},
            'amigos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'amigos_rel_+'", 'blank': 'True', 'to': u"orm['app.Entrenador']"}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Equipo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'app.equipo': {
            'Meta': {'object_name': 'Equipo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.jugador': {
            'Meta': {'object_name': 'Jugador'},
            'amigos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'amigos_rel_+'", 'blank': 'True', 'to': u"orm['app.Jugador']"}),
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'correo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Equipo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'app.liga': {
            'Meta': {'object_name': 'Liga'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.publicacion': {
            'Meta': {'object_name': 'Publicacion'},
            'contenido': ('django.db.models.fields.CharField', [], {'max_length': '450'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'app.queja': {
            'Meta': {'object_name': 'Queja'},
            'contenido': ('django.db.models.fields.CharField', [], {'max_length': '450'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']