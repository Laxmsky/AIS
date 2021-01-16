from django import forms

class AddHead_of_division(forms.Form):
    last_name = forms.CharField(label="Имя")
    first_name = forms.CharField(label="Фамилия")
    patronymic = forms.CharField(label="Отчество")
    position = forms.CharField(label="Должность")
    id_member_of_the_division = forms.CharField(label="id члена дивизии")
    division_number = forms.CharField(label="номер девизии")

class Adddivision(forms.Form):
    full_name = forms.CharField(label="Полное название")
    abbreviated_name = forms.CharField(label="Краткое название")

class Addmember_of_the_division(forms.Form):
    last_name = forms.CharField(label="Имя")
    first_name = forms.CharField(label="Фамилия")
    patronymic = forms.CharField(label="Отчество")
    position = forms.CharField(label="Должность")
    division_number = forms.CharField(label="номер девизии")

class Addmaterially_responsible_person(forms.Form):
    last_name = forms.CharField(label="Имя")
    first_name = forms.CharField(label="Фамилия")
    patronymic = forms.CharField(label="Отчество")
    position = forms.CharField(label="Должность")
    id_member_of_the_division = forms.CharField(label="id члена дивизии")
    division_number = forms.CharField(label="номер девизии")

class Addtransfer_form(forms.Form):
    date_of_transfer = forms.CharField(label="Дата передачи")
    number_of_the_room = forms.CharField(label="Номер комнаты")
    mater = forms.CharField(label="id Материально ответственного лица")
    inventory_number = forms.CharField(label="Инвентарный номер")

class Addequipment(forms.Form):
    name = forms.CharField(label="Название")
    acquisition_date = forms.CharField(label="Дата получения")
    cost = forms.CharField(label="Цена")




