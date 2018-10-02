# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def create_core_accounts(apps, schema_editor):
    # Please use `manage.py izi_accounts_init`
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('izi_accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_core_accounts)
    ]
