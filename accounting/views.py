from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.generic import FormView
from .models import Head_of_division, division, member_of_the_division, materially_responsible_person, transfer_form, equipment
from .forms import AddHead_of_division, Adddivision, Addmember_of_the_division, Addmaterially_responsible_person, Addtransfer_form, Addequipment
from django.views import generic
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from accounting import forms

def great(request):
    return render(request, "great.html")

def index(request):
    return render(request, "index.html")

def index_Head_of_division(request):
    form_add = AddHead_of_division()
    data = Head_of_division.objects.all()
    return render(request, "accounting/Template_Head_of_division.html", {"form":form_add, "data_show":data})

def index_division(request):
    form_ex = Adddivision()
    data = division.objects.all()
    return render(request, "accounting/Template_division.html", {"form":form_ex, "data_show":data})

def index_member_of_the_division(request):
    form_er = Addmember_of_the_division()
    data = member_of_the_division.objects.all()
    return render(request, "accounting/Template_member_of_the_division.html", {"form":form_er, "data_show":data})

def index_materially_responsible_person(request):
    form_ca = Addmaterially_responsible_person()
    data = materially_responsible_person.objects.all()
    return render(request, "accounting/Template_materially_responsible_person.html", {"form":form_ca, "data_show":data})

def index_transfer_form(request):
    form_ra = Addtransfer_form()
    data = transfer_form.objects.all()
    return render(request, "accounting/Template_transfer_form.html", {"form":form_ra, "data_show":data})

def index_equipment(request):
    form_b = Addequipment()
    data = equipment.objects.all()
    return render(request, "accounting/Template_equipment.html", {"form":form_b, "data_show":data})

#Определение view

class view_Head_of_division(View):
    def add_Head_of_division(request):
        if request.method == "POST":
            head = Head_of_division()
            head.last_name = request.POST.get("last_name")
            head.first_name = request.POST.get("first_name")
            head.patronymic = request.POST.get("patronymic")
            head.position = request.POST.get("position")
            head.id_member_of_the_division = member_of_the_division.objects.get(id=request.POST.get("id_member_of_the_division"))
            head.division_number = division.objects.get(id=request.POST.get("division_number"))
            head.save()
            return HttpResponseRedirect("/Head_of_division")

    def del_Head_of_division(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Head_of_division.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Head_of_division")

    def update_Head_of_division(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Head_of_division.objects.get(id=q)
            que.last_name = request.POST.get("last_name")
            que.first_name = request.POST.get("first_name")
            que.patronymic = request.POST.get("patronymic")
            que.position = request.POST.get("position")
            que.id_member_of_the_division = member_of_the_division.objects.get(id=request.POST.get("id_member_of_the_division"))
            que.division_number = division.objects.get(id=request.POST.get("division_number"))
            que.save()
            return HttpResponseRedirect("/Head_of_division")

class view_division(View):
    def add_division(request):
        if request.method == "POST":
            divis = division()
            divis.full_name = request.POST.get("full_name")
            divis.abbreviated_name = request.POST.get("abbreviated_name")
            divis.save()
            return HttpResponseRedirect("/division")

    def del_division(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = division.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/division")

    def update_division(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = division.objects.get(id=q)
            que.full_name = request.POST.get("full_name")
            que.abbreviated_name = request.POST.get("abbreviated_name")
            que.save()
            return HttpResponseRedirect("/division")

class view_member_of_the_division(View):
    def add_member_of_the_division(request):
        if request.method == "POST":
            member = member_of_the_division()
            member.last_name = request.POST.get("last_name")
            member.first_name = request.POST.get("first_name")
            member.patronymic = request.POST.get("patronymic")
            member.position = request.POST.get("position")
            member.division_number = division.objects.get(id=request.POST.get("division_number"))
            member.save()
            return HttpResponseRedirect("/member_of_the_division")

    def del_member_of_the_division(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = member_of_the_division.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/member_of_the_division")

    def update_member_of_the_division(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = member_of_the_division.objects.get(id=q)
            que.last_name = request.POST.get("last_name")
            que.first_name = request.POST.get("first_name")
            que.patronymic = request.POST.get("patronymic")
            que.position = request.POST.get("position")
            que.division_number = division.objects.get(id=request.POST.get("division_number"))
            que.save()
            return HttpResponseRedirect("/member_of_the_division")

class view_materially_responsible_person(View):
    def add_materially_responsible_person(request):
        if request.method == "POST":
            materially = materially_responsible_person()
            materially.last_name = request.POST.get("last_name")
            materially.first_name = request.POST.get("first_name")
            materially.patronymic = request.POST.get("patronymic")
            materially.position = request.POST.get("position")
            materially.id_member_of_the_division = member_of_the_division.objects.get(id=request.POST.get("id_member_of_the_division"))
            materially.division_number = division.objects.get(id=request.POST.get("division_number"))
            materially.save()
            return HttpResponseRedirect("/materially_responsible_person")

    def del_materially_responsible_person(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = materially_responsible_person.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/materially_responsible_person")

    def update_materially_responsible_person(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = materially_responsible_person.objects.get(id=q)
            que.last_name = request.POST.get("last_name")
            que.first_name = request.POST.get("first_name")
            que.patronymic = request.POST.get("patronymic")
            que.position = request.POST.get("position")
            que.id_member_of_the_division = member_of_the_division.objects.get(id=request.POST.get("id_member_of_the_division"))
            que.division_number = division.objects.get(id=request.POST.get("division_number"))

            que.save()
            return HttpResponseRedirect("/materially_responsible_person")

class view_transfer_form(View):
    def add_transfer_form(request):
        if request.method == "POST":
            transfer = transfer_form()
            transfer.date_of_transfer = request.POST.get("date_of_transfer")
            transfer.number_of_the_room = request.POST.get("number_of_the_room")
            transfer.mater = materially_responsible_person.objects.get(id=request.POST.get("mater"))
            transfer.inventory_number = equipment.objects.get(id=request.POST.get("inventory_number"))
            transfer.save()
            return HttpResponseRedirect("/transfer_form")

    def del_transfer_form(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = transfer_form.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/transfer_form")

    def update_transfer_form(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = transfer_form.objects.get(id=q)
            que.date_of_transfer = request.POST.get("date_of_transfer")
            que.number_of_the_room = request.POST.get("number_of_the_room")
            que.mater = materially_responsible_person.objects.get(id=request.POST.get("mater"))
            que.inventory_number = equipment.objects.get(id=request.POST.get("inventory_number"))
            que.save()
            return HttpResponseRedirect("/transfer_form")

class view_equipment(View):
    def add_equipment(request):
        if request.method == "POST":
            equ = equipment()
            equ.name = request.POST.get("name")
            equ.acquisition_date = request.POST.get("acquisition_date")
            equ.cost = request.POST.get("cost")
            equ.save()
            return HttpResponseRedirect("/equipment")

    def del_equipment(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = equipment.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/equipment")

    def update_equipment(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = equipment.objects.get(id=q)
            que.name = request.POST.get("name")
            que.acquisition_date = request.POST.get("acquisition_date")
            que.cost = request.POST.get("cost")
            que.save()
            return HttpResponseRedirect("/equipment")


