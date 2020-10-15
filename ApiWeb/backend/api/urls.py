from django.urls import path
from api import views
from .views import RegisterAPI


urlpatterns = [
    path('registrodoc', views.registroDoctor),
    path('registrogroup', views.registroGrupoFam),
    path('registropaciente', views.registroPaciente),
    path('api/register/', RegisterAPI.as_view(), name='register')
]