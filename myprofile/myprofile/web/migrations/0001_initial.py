# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-06-18 05:52
from __future__ import unicode_literals

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FunProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
                ('description', django_markdown.models.MarkdownField()),
                ('repo_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', django_markdown.models.MarkdownField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(help_text='Your skill, eg. Python', max_length=100)),
                ('rate', models.IntegerField(help_text='Skill level in %')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Website title', max_length=100)),
                ('about', django_markdown.models.MarkdownField()),
                ('profile_img', models.ImageField(help_text='profile picture', upload_to='uploads/img')),
            ],
        ),
    ]