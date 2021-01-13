
from django.contrib import admin
from django.urls import path
from accounting import views
from django.views.generic import TemplateView
from django.conf.urls import include, url

admin.autodiscover()



urlpatterns = [
    path('',views.great, name='great'),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('ais/', views.index, name='home'),
    path('Head_of_division/', views.index_Head_of_division, name='Head_of_division'),
    path('division/', views.index_division, name='division'),
    path('member_of_the_division/', views.index_member_of_the_division, name='member_of_the_division'),
    path('materially_responsible_person/', views.index_materially_responsible_person, name='materially_responsible_person'),
    path('transfer_form/', views.index_transfer_form, name='transfer_form'),
    path('equipment/', views.index_equipment, name='equipment'),
    #пути для Head_of_division
    path('Head_of_division/add/', views.view_Head_of_division.add_Head_of_division, name='add_Head_of_division'),
    path("Head_of_division/del/", views.view_Head_of_division.del_Head_of_division, name="del_Head_of_division"),
    path("Head_of_division/up/", views.view_Head_of_division.update_Head_of_division, name="update_Head_of_division"),
    #пути для division
    path('division/addb/', views.view_division.add_division, name='add_division'),
    path("division/delb/", views.view_division.del_division, name="del_division"),
    path("division/upb/", views.view_division.update_division, name="update_division"),
    #пути для member_of_the_division
    path('member_of_the_division/addo/', views.view_member_of_the_division.add_member_of_the_division, name='add_member_of_the_division'),
    path("member_of_the_division/delo/", views.view_member_of_the_division.del_member_of_the_division, name="del_member_of_the_division"),
    path("member_of_the_division/upo/", views.view_member_of_the_division.update_member_of_the_division, name="update_member_of_the_division"),
    #пути для materially_responsible_person
    path('materially_responsible_person/addma/', views.view_materially_responsible_person.add_materially_responsible_person, name='add_materially_responsible_person'),
    path("materially_responsible_person/delma/", views.view_materially_responsible_person.del_materially_responsible_person, name="del_materially_responsible_person"),
    path("materially_responsible_person/upma/", views.view_materially_responsible_person.update_materially_responsible_person, name="update_materially_responsible_person"),
    #пути для transfer_form
    path('transfer_form/addr/', views.view_transfer_form.add_transfer_form, name='add_transfer_form'),
    path("transfer_form/delr/", views.view_transfer_form.del_transfer_form, name="del_transfer_form"),
    path("transfer_form/upr/", views.view_transfer_form.update_transfer_form, name="update_transfer_form"),
    #пути для equipment
    path('equipment/adde/', views.view_equipment.add_equipment, name='add_equipment'),
    path("equipment/dele/", views.view_equipment.del_equipment, name="del_equipment"),
    path("equipment/upe/", views.view_equipment.update_equipment, name="update_equipment"),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]