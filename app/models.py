from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Liga(models.Model):
	descripcion = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Ligas"
	def __unicode__(self):
		return self.user.des_liga

class Equipo(models.Model):
	nombre = models.CharField(max_length=50)
	lugar = models.CharField(max_length=50)
	class Meta:
		verbose_name_plural = "Equipos"
	def __unicode__(self):
		return self.nombre

class Entrenador(models.Model):
	usuario = models.OneToOneField(User)
	nombre = models.CharField(max_length=50)
	edad = models.IntegerField()
	equipo = models.ForeignKey(Equipo)
	amigos = models.ManyToManyField("self", blank=True)
	class Meta:
		verbose_name_plural = "Entrenadores"
	def __unicode__(self):
		return self.user.usuario

class Jugador(models.Model):
	usuario = models.OneToOneField(User)
	nombre = models.CharField(max_length=50)
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	correo = models.CharField(max_length=60)
	telefono = models.IntegerField()
	amigos = models.ManyToManyField("self", blank=True)
	equipo = models.ForeignKey(Equipo)
	class Meta:
		verbose_name_plural = "Jugadores"
	def __unicode__(self):
		return self.user.usuario

class Publicacion(models.Model):
	contenido = models.CharField(max_length=450)
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField('pub_date')
	class Meta:
		verbose_name_plural = "Publicaciones"
	def __unicode__(self):
		return self.user.contenido

class Queja(models.Model):
	contenido = models.CharField(max_length=450)
	usuario = models.OneToOneField(User)
	fecha = models.DateTimeField('pub_date')
	class Meta:
		verbose_name_plural = "Quejas"
	def __unicode__(self):
		return self.user.usuario

