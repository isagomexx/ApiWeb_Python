# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    fecha_cita = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cita'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctor(models.Model):
    tipo_documento = models.CharField(max_length=20)
    numero_identificacion = models.CharField(primary_key=True, max_length=20)
    nombres = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    correo = models.CharField(unique=True, max_length=60)
    especialidad = models.CharField(max_length=40)
    usuario = models.CharField(unique=True, max_length=50)
    contrasena = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'doctor'


class Examen(models.Model):
    id_examen = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    resultados = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'examen'


class FormulaMedica(models.Model):
    id_formula = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    medicamentos = models.TextField()
    tratamiento = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'formula_medica'


class GrupoFamilia(models.Model):
    id_grupo_familia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'grupo_familia'


class Historial(models.Model):
    id_historial = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=400)
    diagnostico = models.CharField(max_length=400)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')

    class Meta:
        managed = False
        db_table = 'historial'


class Incapacidad(models.Model):
    id_incapacidad = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    descripcion = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'incapacidad'


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    id_doctor = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='id_doctor')
    medicamentos = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'orden'


class Paciente(models.Model):
    tipo_documento = models.CharField(max_length=20)
    numero_identificacion = models.CharField(primary_key=True, max_length=20)
    nombres = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    correo = models.CharField(unique=True, max_length=60)
    estrato = models.IntegerField()
    fecha_nacimiento = models.DateField()
    id_grupo_familiar = models.ForeignKey(GrupoFamilia, models.DO_NOTHING, db_column='id_grupo_familiar')
    id_doctor = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='id_doctor')
    usuario = models.CharField(unique=True, max_length=50)
    contrasena = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'paciente'
