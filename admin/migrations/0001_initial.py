# -*- coding: utf-8 -*-

# Generated by Django 1.10 on 2016-08-23 11:27


import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import djangoplus.admin.models
import djangoplus.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Fun\xe7\xe3o',
                'db_table': 'admin_user_groups',
                'managed': False,
                'verbose_name_plural': 'Fun\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', djangoplus.db.models.fields.CharField(blank=True, max_length=30, verbose_name='Nome')),
                ('username', djangoplus.db.models.fields.CharField(max_length=30, unique=True, verbose_name='Login')),
                ('email', djangoplus.db.models.fields.CharField(blank=True, default=b'', max_length=75, verbose_name='E-mail')),
                ('active', djangoplus.db.models.fields.BooleanField(default=True, verbose_name='Ativo?')),
                ('photo', djangoplus.db.models.fields.ImageField(blank=True, default=b'/static/images/user.png', null=True, upload_to=b'profiles', verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            managers=[
                ('objects', djangoplus.admin.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', djangoplus.db.models.fields.CharField(default='Django+', max_length=255, verbose_name='Nome')),
                ('name', djangoplus.db.models.fields.CharField(default='Django Plus', max_length=255, verbose_name='Descrição')),
                ('logo', djangoplus.db.models.fields.ImageField(blank=True, default=b'', null=True, upload_to=b'config', verbose_name='Logotipo')),
                ('logo_pdf', djangoplus.db.models.fields.ImageField(blank=True, default=b'', help_text='Imagem sem fundo transparente', null=True, upload_to=b'config', verbose_name='Logotipo para PDF')),
                ('icon', djangoplus.db.models.fields.ImageField(blank=True, default=b'/static/images/blank.png', null=True, upload_to=b'config', verbose_name='\xcdcone')),
                ('background', djangoplus.db.models.fields.ImageField(blank=True, default=b'', upload_to=b'config', verbose_name='Background')),
                ('twitter', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Twitter')),
                ('facebook', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook')),
                ('google', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Google')),
                ('pinterest', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='pinterest')),
                ('linkedin', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Linkedin')),
                ('rss', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='RSS')),
                ('activated', djangoplus.db.models.fields.BooleanField(default=False, verbose_name='Ativado')),
                ('mail_confirmation', djangoplus.db.models.fields.BooleanField(default=False, verbose_name='Confirma\xe7\xe3o via E-mail')),
                ('admin_activation', djangoplus.db.models.fields.BooleanField(default=False, verbose_name='Ativa\xe7\xe3o pelo Administrador')),
                ('address', djangoplus.db.models.fields.TextField(blank=True, null=True, verbose_name='Endere\xe7o')),
                ('phone_1', djangoplus.db.models.fields.PhoneField(blank=True, max_length=255, null=True, verbose_name='Telefone Principal')),
                ('phone_2', djangoplus.db.models.fields.PhoneField(blank=True, max_length=255, null=True, verbose_name='Telefone Secund\xe1rio')),
                ('email', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='E-mail')),
                ('default_color', djangoplus.db.models.fields.CharField(default='#009688', max_length=255, verbose_name='Cor')),
                ('version', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Vers\xe3o do Sistema')),
                ('server_address', djangoplus.db.models.fields.CharField(default='http://localhost:8000', max_length=255, verbose_name='Endere\xe7o de Acesso')),
                ('system_email_address', djangoplus.db.models.fields.CharField(default='no-reply@djangoplus.net', max_length=255, verbose_name='E-mail de Notifica\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Configura\xe7\xe3o',
                'verbose_name_plural': 'Configura\xe7\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ascii', djangoplus.db.models.fields.SearchField(blank=True, default=b'', editable=False)),
            ],
            options={
                'verbose_name': 'Unidade',
                'verbose_name_plural': 'Unidades',
            },
        ),
        migrations.CreateModel(
            name='UnitRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', djangoplus.db.models.fields.ModelChoiceField(on_delete=django.db.models.deletion.CASCADE, to='admin.Role', verbose_name='Fun\xe7\xe3o')),
                ('unit', djangoplus.db.models.fields.ModelChoiceField(on_delete=django.db.models.deletion.CASCADE, to='admin.Unit', verbose_name='Unidade')),
            ],
            options={
                'verbose_name': 'Fun\xe7\xe3o na Unidade',
                'verbose_name_plural': 'Fun\xe7\xf5es na Unidade',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AddField(
            model_name='settings',
            name='associated_groups',
            field=djangoplus.db.models.fields.MultipleModelChoiceField(blank=True, to='admin.Group', verbose_name='Grupos Associados'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
