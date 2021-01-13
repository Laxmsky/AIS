# Generated by Django 3.1.5 on 2021-01-12 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_auto_20210112_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materially_responsible_person',
            old_name='member_of_the_division_idmember_of_the_division',
            new_name='idmember_of_the_division',
        ),
        migrations.RenameField(
            model_name='transfer_form',
            old_name='materially_responsible_person_idmaterially_responsible_person',
            new_name='idmaterially_responsible_person',
        ),
        migrations.RenameField(
            model_name='transfer_form',
            old_name='equipment_inventory_number',
            new_name='inventory_number',
        ),
    ]
