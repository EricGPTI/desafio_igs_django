# Generated by Django 3.2.9 on 2021-12-13 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_employee_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='department_id',
            new_name='department',
        ),
    ]