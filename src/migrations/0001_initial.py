# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_pgjson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_data', django_pgjson.fields.JsonField(default={})),
                ('team_number', models.IntegerField(default=0)),
                ('team_name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raw_groups', to='events.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TicketInGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_data', django_pgjson.fields.JsonField(default={})),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='groups.Group')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='events.Ticket')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
