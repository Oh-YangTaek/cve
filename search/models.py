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


class CveTable(models.Model):
    no = models.IntegerField(db_column='No', primary_key=True)  # Field name made lowercase.
    platform = models.CharField(db_column='Platform', max_length=30, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=20, blank=True, null=True)  # Field name made lowercase.
    platform_version = models.CharField(db_column='Platform_Version', max_length=40, blank=True, null=True)  # Field name made lowercase.
    platform_type = models.CharField(db_column='Platform_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=20, blank=True, null=True)  # Field name made lowercase.
    etc = models.CharField(max_length=20, blank=True, null=True)
    up_date = models.CharField(db_column='Up_date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='Edition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cve_id = models.CharField(db_column='CVE_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cwe_id = models.IntegerField(db_column='CWE_ID', blank=True, null=True)  # Field name made lowercase.
    n_of_exploits = models.IntegerField(db_column='n_of_Exploits', blank=True, null=True)  # Field name made lowercase.
    vulnerability_type = models.CharField(db_column='Vulnerability_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    publish_year = models.IntegerField(db_column='Publish_Year', blank=True, null=True)  # Field name made lowercase.
    publish_date = models.CharField(db_column='Publish_Date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    update_date = models.CharField(db_column='Update_Date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    gained_access_level = models.CharField(db_column='Gained_Access_Level', max_length=20, blank=True, null=True)  # Field name made lowercase.
    access = models.CharField(db_column='Access', max_length=20, blank=True, null=True)  # Field name made lowercase.

    conf = models.CharField(db_column='Conf', max_length=20, blank=True, null=True)  # Field name made lowercase.
    integ = models.CharField(db_column='Integ', max_length=20, blank=True, null=True)  # Field name made lowercase.
    avail = models.CharField(db_column='Avail', max_length=20, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cve_table'


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
