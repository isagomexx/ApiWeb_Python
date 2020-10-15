from django.urls import path
from api import views


urlpatterns = [
    path('registrodoc', views.registroDoctor),
    path('registrogroup', views.registroGrupoFam),
    path('registropaciente', views.registroPaciente),
    path('registrohistorial', views.registroHistoria),
    # path('Listadoc/', DoctorList.as_view())
]