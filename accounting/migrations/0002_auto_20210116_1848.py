# Generated by Django 3.1.5 on 2021-01-16 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='division',
            old_name='number',
            new_name='id',
        ),
    ]