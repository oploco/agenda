# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contacto(models.Model):
    idcontacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacto'
        db_table_comment = 'Tabla para los contactos'


class Telefono(models.Model):
    numtel = models.CharField(max_length=45)
    idcontacto = models.ForeignKey(Contacto, models.DO_NOTHING, db_column='idContacto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telefono'
        db_table_comment = 'Tabla par telefonos de contacto'
