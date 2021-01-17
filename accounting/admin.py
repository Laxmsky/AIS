from django.contrib import admin
from .models import Head_of_division, division, member_of_the_division, materially_responsible_person, transfer_form, equipment



@admin.register(Head_of_division)
class Head_of_divisionAdmin(admin.ModelAdmin):
    list_display = ('id','last_name','first_name','patronymic','position','id_member_of_the_division','division_number')

@admin.register(division)
class divisionAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','abbreviated_name')

@admin.register(member_of_the_division)
class member_of_the_divisionAdmin(admin.ModelAdmin):
    list_display = ('id','last_name','first_name','patronymic','position','division_number')

@admin.register(materially_responsible_person)
class materially_responsible_personAdmin(admin.ModelAdmin):
    list_display = ('id','last_name','first_name','patronymic','position','id_member_of_the_division','division_number')

@admin.register(transfer_form)
class transfer_formAdmin(admin.ModelAdmin):
    list_display = ('id','date_of_transfer','number_of_the_room','mater','inventory_number')

@admin.register(equipment)
class equipmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','acquisition_date','cost','number_of_the_room','mater')

