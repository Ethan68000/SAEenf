# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Capteur(models.Model):
    id_capteur = models.CharField(primary_key=True, max_length=100)
    piece = models.CharField(db_column='PIECE', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'capteur'

    def __str__(self):
        return f"Capteur {self.id_capteur} {self.piece}."

    def dic(self):
        return { "piece": self.piece,}


class CapteurCapteur(models.Model):
    id_capteur = models.CharField(primary_key=True, max_length=40)
    nom = models.CharField(db_column='Nom', max_length=100)  # Field name made lowercase.
    temperature = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'capteur_capteur'


class Details(models.Model):
    id_capteur = models.ForeignKey(Capteur, models.DO_NOTHING, db_column='id_capteur', blank=True, null=True)
    piece = models.CharField(db_column='PIECE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'details'

    def __str__(self):
        chaine = f"{self.id_capteur} {self.piece} {self.date} {self.time} {self.temp}"
        return chaine


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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


class Donnees(models.Model):
    id_capteur = models.ForeignKey(CapteurCapteur, models.DO_NOTHING, db_column='id_capteur')
    date = models.DateTimeField()
    time = models.DateTimeField()
    temperature = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'donnees'
