from django.test import TestCase
import unittest
from accounting.models import Head_of_division, division, member_of_the_division, materially_responsible_person, transfer_form, equipment
# Create your tests here.
from django.urls import reverse


class divisionViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        division.objects.create(id = 1,full_name = "Финансовое подразделение", abbreviated_name = "Финансы")

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/division/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('division'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('division'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'accounting/Template_division.html')

class Head_of_divisionViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Head_of_division.objects.create(id = 1,last_name = "Суботин", first_name = "Вениамин",
                                        patronymic = "Касьянович", position = "Начальник",)

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/Head_of_division/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('Head_of_division'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('Head_of_division'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'accounting/Template_Head_of_division.html')

class member_of_the_divisionViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        member_of_the_division.objects.create(id = 1, last_name = "Суботин", first_name = "Вениамин",
                                              patronymic = "Касьянович", position = "Начальник",)

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/member_of_the_division/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('member_of_the_division'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('member_of_the_division'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'accounting/Template_member_of_the_division.html')

class materially_responsible_personViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        materially_responsible_person.objects.create(id = 1,last_name = "Суботин", first_name = "Вениамин",
                                                     patronymic = "Касьянович", position = "Начальник")

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/materially_responsible_person/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('materially_responsible_person'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('materially_responsible_person'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'accounting/Template_materially_responsible_person.html')

class transfer_formViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        transfer_form.objects.create(id = 1,date_of_transfer = "12.12.2020", number_of_the_room = "12")

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/transfer_form/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('transfer_form'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('transfer_form'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'accounting/Template_transfer_form.html')

class equipmentViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        equipment.objects.create(id = 1, name = "Принтер", acquisition_date = "10.05.2019",
                                 cost = "1500 руб", number_of_the_room = '12')

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/equipment/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('equipment'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('equipment'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'accounting/Template_equipment.html')

class AnotherViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        division.objects.create(id = 1,full_name = "Финансовое подразделение", abbreviated_name = "Финансы")

    def test_view_url_exists_at_desired_location(self): # существование url по адресу
        resp = self.client.get('/ais/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self): # существование url по имени
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): # соответствие шаблону
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_view_url_exists_at_desired_location1(self): # существование url по адресу
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name1(self): # существование url по имени
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template1(self): # соответствие шаблону
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'great.html')