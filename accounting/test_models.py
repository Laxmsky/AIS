from django.test import TestCase
import unittest
from accounting.models import Head_of_division, division, member_of_the_division, materially_responsible_person, transfer_form, equipment
# Create your tests here.

class divisionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        division.objects.create(id = 1,full_name = "Финансовое подразделение", abbreviated_name = "Финансы")

    def test_id_label(self):
        div=division.objects.get(id=1)
        field_label = div._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')

    def test_full_name_label(self):
        div=division.objects.get(id=1)
        field_label = div._meta.get_field('full_name').verbose_name
        self.assertEquals(field_label,'full name')

    def test_full_name_max_length(self):
        div=division.objects.get(id=1)
        max_length = div._meta.get_field('full_name').max_length
        self.assertEquals(max_length,45)

    def test_abbreviated_name_label(self):
        div=division.objects.get(id=1)
        field_label = div._meta.get_field('abbreviated_name').verbose_name
        self.assertEquals(field_label,'abbreviated name')

    def test_abbreviated_name_max_length(self):
        div=division.objects.get(id=1)
        max_length = div._meta.get_field('abbreviated_name').max_length
        self.assertEquals(max_length,45)

class member_of_the_divisionlModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        member_of_the_division.objects.create(id = 1, last_name = "Суботин", first_name = "Вениамин",
                                              patronymic = "Касьянович", position = "Начальник",)

    def test_id_label(self):
        member=member_of_the_division.objects.get(id=1)
        field_label = member._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')

    def test_last_name_label(self):
        member=member_of_the_division.objects.get(id=1)
        field_label = member._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')

    def test_last_name_max_length(self):
        member=member_of_the_division.objects.get(id=1)
        max_length = member._meta.get_field('last_name').max_length
        self.assertEquals(max_length,45)

    def test_first_name_label(self):
        member=member_of_the_division.objects.get(id=1)
        field_label = member._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_first_name_max_length(self):
        member=member_of_the_division.objects.get(id=1)
        max_length = member._meta.get_field('first_name').max_length
        self.assertEquals(max_length,45)

    def test_patronymic_label(self):
        member=member_of_the_division.objects.get(id=1)
        field_label = member._meta.get_field('patronymic').verbose_name
        self.assertEquals(field_label,'patronymic')

    def test_patronymic_length(self):
        member=member_of_the_division.objects.get(id=1)
        max_length = member._meta.get_field('patronymic').max_length
        self.assertEquals(max_length,45)

    def test_position_label(self):
        member=member_of_the_division.objects.get(id=1)
        field_label = member._meta.get_field('position').verbose_name
        self.assertEquals(field_label,'position')

    def test_position_max_length(self):
        member=member_of_the_division.objects.get(id=1)
        max_length = member._meta.get_field('position').max_length
        self.assertEquals(max_length,45)

    def test_division_number_label(self):
        member=member_of_the_division.objects.get(id=1)
        field_label = member._meta.get_field('division_number').verbose_name
        self.assertEquals(field_label,'division number')

class  Head_of_divisionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Head_of_division.objects.create(id = 1,last_name = "Суботин", first_name = "Вениамин",
                                        patronymic = "Касьянович", position = "Начальник",)

    def test_id_label(self):
        Head=Head_of_division.objects.get(id=1)
        field_label = Head._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')

    def test_last_name_label(self):
        Head=Head_of_division.objects.get(id=1)
        field_label = Head._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')

    def test_last_name_max_length(self):
        Head=Head_of_division.objects.get(id=1)
        max_length = Head._meta.get_field('last_name').max_length
        self.assertEquals(max_length,45)

    def test_first_name_label(self):
        Head=Head_of_division.objects.get(id=1)
        field_label = Head._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_first_name_max_length(self):
        Head=Head_of_division.objects.get(id=1)
        max_length = Head._meta.get_field('first_name').max_length
        self.assertEquals(max_length,45)

    def test_patronymic_label(self):
        Head=Head_of_division.objects.get(id=1)
        field_label = Head._meta.get_field('patronymic').verbose_name
        self.assertEquals(field_label,'patronymic')

    def test_patronymic_max_length(self):
        Head=Head_of_division.objects.get(id=1)
        max_length = Head._meta.get_field('patronymic').max_length
        self.assertEquals(max_length,45)

    def test_position_label(self):
        Head=Head_of_division.objects.get(id=1)
        field_label = Head._meta.get_field('position').verbose_name
        self.assertEquals(field_label,'position')

    def test_position_max_length(self):
        Head=Head_of_division.objects.get(id=1)
        max_length = Head._meta.get_field('position').max_length
        self.assertEquals(max_length,45)

    def test_id_member_of_the_division_label(self):
        Head=Head_of_division.objects.get(id=1)
        field_label = Head._meta.get_field('id_member_of_the_division').verbose_name
        self.assertEquals(field_label,'id member of the division')

    def test_division_number_label(self):
        Head=Head_of_division.objects.get(id=1)
        field_label = Head._meta.get_field('division_number').verbose_name
        self.assertEquals(field_label,'division number')

class materially_responsible_personModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        materially_responsible_person.objects.create(id = 1,last_name = "Суботин", first_name = "Вениамин",
                                                     patronymic = "Касьянович", position = "Начальник")

    def test_id_label(self):
        materially=materially_responsible_person.objects.get(id=1)
        field_label = materially._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')

    def test_last_name_label(self):
        materially=materially_responsible_person.objects.get(id=1)
        field_label = materially._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')

    def test_last_name_max_length(self):
        materially=materially_responsible_person.objects.get(id=1)
        max_length = materially._meta.get_field('last_name').max_length
        self.assertEquals(max_length,45)

    def test_first_name_label(self):
        materially=materially_responsible_person.objects.get(id=1)
        field_label = materially._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_first_name_max_length(self):
        materially=materially_responsible_person.objects.get(id=1)
        max_length = materially._meta.get_field('first_name').max_length
        self.assertEquals(max_length,45)

    def test_patronymic_label(self):
        materially=materially_responsible_person.objects.get(id=1)
        field_label = materially._meta.get_field('patronymic').verbose_name
        self.assertEquals(field_label,'patronymic')

    def test_patronymic_max_length(self):
        materially=materially_responsible_person.objects.get(id=1)
        max_length = materially._meta.get_field('patronymic').max_length
        self.assertEquals(max_length,45)

    def test_position_label(self):
        materially=materially_responsible_person.objects.get(id=1)
        field_label = materially._meta.get_field('position').verbose_name
        self.assertEquals(field_label,'position')

    def test_position_max_length(self):
        materially=materially_responsible_person.objects.get(id=1)
        max_length = materially._meta.get_field('position').max_length
        self.assertEquals(max_length,45)

    def test_id_member_of_the_division_label(self):
        materially=materially_responsible_person.objects.get(id=1)
        field_label = materially._meta.get_field('id_member_of_the_division').verbose_name
        self.assertEquals(field_label,'id member of the division')

    def test_division_number_label(self):
        materially=materially_responsible_person.objects.get(id=1)
        field_label = materially._meta.get_field('division_number').verbose_name
        self.assertEquals(field_label,'division number')

class equipmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        equipment.objects.create(id = 1, name = "Принтер", acquisition_date = "10.05.2019",
                                 cost = "1500 руб", number_of_the_room = '12')

    def test_id_label(self):
        user=equipment.objects.get(id=1)
        field_label = user._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')

    def test_name_label(self):
        user=equipment.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_name_max_length(self):
        user=equipment.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEquals(max_length,45)

    def test_acquisition_date_label(self):
        user=equipment.objects.get(id=1)
        field_label = user._meta.get_field('acquisition_date').verbose_name
        self.assertEquals(field_label,'acquisition date')

    def test_acquisition_date_max_length(self):
        user=equipment.objects.get(id=1)
        max_length = user._meta.get_field('acquisition_date').max_length
        self.assertEquals(max_length,45)

    def test_cost_label(self):
        user=equipment.objects.get(id=1)
        field_label = user._meta.get_field('cost').verbose_name
        self.assertEquals(field_label,'cost')

    def test_cost_max_length(self):
        user=equipment.objects.get(id=1)
        max_length = user._meta.get_field('cost').max_length
        self.assertEquals(max_length,45)

    def test_number_of_the_room_label(self):
        user=equipment.objects.get(id=1)
        field_label = user._meta.get_field('number_of_the_room').verbose_name
        self.assertEquals(field_label,'number of the room')

    def test_number_of_the_room_max_length(self):
        user=equipment.objects.get(id=1)
        max_length = user._meta.get_field('number_of_the_room').max_length
        self.assertEquals(max_length,45)

    def test_mater_label(self):
        user=equipment.objects.get(id=1)
        field_label = user._meta.get_field('mater').verbose_name
        self.assertEquals(field_label,'mater')

class transfer_formModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        transfer_form.objects.create(id = 1,date_of_transfer = "12.12.2020", number_of_the_room = "12")

    def test_id_label(self):
        transfer=transfer_form.objects.get(id=1)
        field_label = transfer._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')

    def test_date_of_transfer_label(self):
        transfer=transfer_form.objects.get(id=1)
        field_label = transfer._meta.get_field('date_of_transfer').verbose_name
        self.assertEquals(field_label,'date of transfer')

    def test_date_of_transfer_max_length(self):
        transfer=transfer_form.objects.get(id=1)
        max_length = transfer._meta.get_field('date_of_transfer').max_length
        self.assertEquals(max_length,45)

    def test_number_of_the_room_label(self):
        transfer=transfer_form.objects.get(id=1)
        field_label = transfer._meta.get_field('number_of_the_room').verbose_name
        self.assertEquals(field_label,'number of the room')

    def test_number_of_the_room_max_length(self):
        transfer=transfer_form.objects.get(id=1)
        max_length = transfer._meta.get_field('number_of_the_room').max_length
        self.assertEquals(max_length,45)

    def test_mater_label(self):
        transfer = transfer_form.objects.get(id=1)
        field_label = transfer._meta.get_field('mater').verbose_name
        self.assertEquals(field_label, 'mater')

    def test_inventory_number_label(self):
        transfer = transfer_form.objects.get(id=1)
        field_label = transfer._meta.get_field('inventory_number').verbose_name
        self.assertEquals(field_label, 'inventory number')

