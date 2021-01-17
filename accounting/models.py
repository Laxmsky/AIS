from django.db import models

class Head_of_division(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    id_member_of_the_division = models.ForeignKey('member_of_the_division', on_delete=models.CASCADE, null=True)
    division_number = models.ForeignKey('division', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class division(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=45)
    abbreviated_name = models.CharField(max_length=45)
    objects = models.Manager()

class member_of_the_division(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    division_number = models.ForeignKey('division', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class materially_responsible_person(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    patronymic = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    id_member_of_the_division = models.ForeignKey('member_of_the_division', on_delete=models.CASCADE,  null=True)
    division_number = models.ForeignKey('division', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class transfer_form(models.Model):
    id = models.IntegerField(primary_key=True)
    date_of_transfer = models.CharField(max_length=45)
    number_of_the_room = models.CharField(max_length=45)
    mater = models.ForeignKey('materially_responsible_person', on_delete=models.CASCADE, null=True)
    inventory_number = models.ForeignKey('equipment', on_delete=models.CASCADE, null=True)
    objects = models.Manager()

class equipment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    acquisition_date = models.CharField(max_length=45)
    cost = models.CharField(max_length=45)
    number_of_the_room = models.CharField(max_length=45)
    mater = models.ForeignKey('materially_responsible_person', on_delete=models.CASCADE, null=True)
    objects = models.Manager()











