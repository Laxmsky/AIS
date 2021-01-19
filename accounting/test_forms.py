from django.test import TestCase
import unittest
from accounting.forms import AddHead_of_division, Adddivision, Addmember_of_the_division, Addmaterially_responsible_person, Addtransfer_form, Addequipment

class AddHead_of_divisionFormTest(TestCase):

    def test_id_label(self):
        form = AddHead_of_division()
        self.assertTrue(form.fields['id'].label == None or form.fields['id'].label == 'id')

    def test_last_name_label(self):
        form = AddHead_of_division()
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Имя')

    def test_first_name_label(self):
        form = AddHead_of_division()
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'Фамилия')

    def test_patronymic_label(self):
        form = AddHead_of_division()
        self.assertTrue(form.fields['patronymic'].label == None or form.fields['patronymic'].label == 'Отчество')

    def test_position_label(self):
        form = AddHead_of_division()
        self.assertTrue(form.fields['position'].label == None or form.fields['position'].label == 'Должность')

    def test_id_member_of_the_division_label(self):
        form = AddHead_of_division()
        self.assertTrue(form.fields['id_member_of_the_division'].label == None or form.fields['id_member_of_the_division'].label == 'id члена Подразделения')

    def test_division_number_label(self):
        form = AddHead_of_division()
        self.assertTrue(form.fields['division_number'].label == None or form.fields['division_number'].label == 'номер Подразделения')

    def test_proverka(self):
        form = AddHead_of_division(data={'id': 1,'last_name': "Суботин", 'first_name': "Вениамин", 'patronymic': "Касьянович", 'position': "Начальник", 'id_member_of_the_division': 1, 'division_number': 1})
        self.assertTrue(form.is_valid())

class AdddivisionFormTest(TestCase):

    def test_id_label(self):
        form = Adddivision()
        self.assertTrue(form.fields['id'].label == None or form.fields['id'].label == 'Номер')

    def test_full_name_label(self):
        form = Adddivision()
        self.assertTrue(form.fields['full_name'].label == None or form.fields['full_name'].label == 'Полное название')

    def test_abbreviated_name_label(self):
        form = Adddivision()
        self.assertTrue(form.fields['abbreviated_name'].label == None or form.fields['abbreviated_name'].label == 'Краткое название')

    def test_proverka(self):
        form = Adddivision(data={'id': 1,'full_name': "Финансовое подразделение", 'abbreviated_name': "Финансы"})
        self.assertTrue(form.is_valid())

class Addmember_of_the_divisionTest(TestCase):

    def test_id_label(self):
        form = Addmember_of_the_division()
        self.assertTrue(form.fields['id'].label == None or form.fields['id'].label == 'id')

    def test_last_name_label(self):
        form = Addmember_of_the_division()
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Имя')

    def test_first_name_label(self):
        form = Addmember_of_the_division()
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'Фамилия')

    def test_patronymic_label(self):
        form = Addmember_of_the_division()
        self.assertTrue(form.fields['patronymic'].label == None or form.fields['patronymic'].label == 'Отчество')

    def test_position_label(self):
        form = Addmember_of_the_division()
        self.assertTrue(form.fields['position'].label == None or form.fields['position'].label == 'Должность')

    def test_division_number_label(self):
        form = Addmember_of_the_division()
        self.assertTrue(form.fields['division_number'].label == None or form.fields['division_number'].label == 'номер Подразделения')

    def test_proverka(self):
        form = Addmember_of_the_division(data={'id': 1, 'last_name': "Суботин", 'first_name': "Вениамин", 'patronymic': "Касьянович",
                                         'position': "Начальник", 'division_number': 1})
        self.assertTrue(form.is_valid())

class Addmaterially_responsible_personFormTest(TestCase):

    def test_id_label(self):
        form = Addmaterially_responsible_person()
        self.assertTrue(form.fields['id'].label == None or form.fields['id'].label == 'id')

    def test_last_name_label(self):
        form = Addmaterially_responsible_person()
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Имя')

    def test_first_name_label(self):
        form = Addmaterially_responsible_person()
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'Фамилия')

    def test_patronymic_label(self):
        form = Addmaterially_responsible_person()
        self.assertTrue(form.fields['patronymic'].label == None or form.fields['patronymic'].label == 'Отчество')

    def test_position_label(self):
        form = Addmaterially_responsible_person()
        self.assertTrue(form.fields['position'].label == None or form.fields['position'].label == 'Должность')

    def test_id_member_of_the_division_label(self):
        form = Addmaterially_responsible_person()
        self.assertTrue(form.fields['id_member_of_the_division'].label == None or form.fields['id_member_of_the_division'].label == 'id члена Подразделения')

    def test_division_number_label(self):
        form = Addmaterially_responsible_person()
        self.assertTrue(form.fields['division_number'].label == None or form.fields['division_number'].label == 'номер Подразделения')

    def test_proverka(self):
        form = Addmaterially_responsible_person(data={'id': 1,'last_name': "Суботин", 'first_name': "Вениамин", 'patronymic': "Касьянович",
                                         'position': "Начальник", 'id_member_of_the_division': 1, 'division_number': 1})
        self.assertTrue(form.is_valid())

class AddequipmentFormTest(TestCase):

    def test_id_label(self):
        form = Addequipment()
        self.assertTrue(form.fields['id'].label == None or form.fields['id'].label == 'Инвентарный номер')

    def test_name_label(self):
        form = Addequipment()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Название')

    def test_acquisition_date_label(self):
        form = Addequipment()
        self.assertTrue(form.fields['acquisition_date'].label == None or form.fields['acquisition_date'].label == 'Дата получения')

    def test_cost_label(self):
        form = Addequipment()
        self.assertTrue(form.fields['cost'].label == None or form.fields['cost'].label == 'Цена')

    def test_number_of_the_room_label(self):
        form = Addequipment()
        self.assertTrue(form.fields['number_of_the_room'].label == None or form.fields['number_of_the_room'].label == 'Номер комнаты')

    def test_mater_label(self):
        form = Addequipment()
        self.assertTrue(form.fields['mater'].label == None or form.fields['mater'].label == 'id Материально ответственного лица')

    def test_proverka(self):
        form = Addequipment(data={'id': 1, 'name': "Принтер", 'acquisition_date': "10.05.2019",'cost': "1500 руб", 'number_of_the_room': 12, 'mater': 1})
        self.assertTrue(form.is_valid())

class Addtransfer_formFormTest(TestCase):

    def test_id_form_label(self):
        form = Addtransfer_form()
        self.assertTrue(form.fields['id'].label == None or form.fields['id'].label == 'номер формы')

    def test_date_of_transfer_form_label(self):
        form = Addtransfer_form()
        self.assertTrue(form.fields['date_of_transfer'].label == None or form.fields['date_of_transfer'].label == 'Дата передачи')

    def test_number_of_the_room_label(self):
        form = Addtransfer_form()
        self.assertTrue(form.fields['number_of_the_room'].label == None or form.fields['number_of_the_room'].label == 'Номер комнаты')

    def test_mater_label(self):
        form = Addtransfer_form()
        self.assertTrue(form.fields['mater'].label == None or form.fields['mater'].label == 'id Материально ответственного лица')

    def test_inventory_number_label(self):
        form = Addtransfer_form()
        self.assertTrue(form.fields['inventory_number'].label == None or form.fields['inventory_number'].label == 'Инвентарный номер')

    def test_proverka(self):
        form = Addtransfer_form(data={'id': 1,'date_of_transfer': "12.12.2020", 'number_of_the_room': "12", 'mater': 1, 'inventory_number': 1})
        self.assertTrue(form.is_valid())