from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Paciente, Doctor, GrupoFamilia, Examen, Cita, Incapacidad, Historial, FormulaMedica, Orden

@api_view(['POST'])
def registro(request):
    tipo_doc = request.data.get('tipo_documento')
    num_id = request.data.get('numero_identificacion')
    nombre = request.data.get('nombres')
    apellidop = request.data.get('apellido_paterno')
    apellidom = request.data.get('apellido_materno')
    tel = request.data.get('telefono')
    direc = request.data.get('direccion')
    email = request.data.get('correo')
    espec = request.data.get('especialidad')
    usu = request.data.get('usuario')
    password = request.data.get('contrasena')

    try:
        doctor = Doctor()
        doctor.tipo_documento = tipo_doc
        doctor.numero_identificacion = num_id
        doctor.nombres = nombre
        doctor.apellido_paterno = apellidop
        doctor.apellido_materno = apellidom
        doctor.telefono = tel
        doctor.direccion = direc
        doctor.correo = email
        doctor.especialidad = espec
        doctor.usuario = usu
        doctor.contrasena = password
        doctor.save()

        insertar = {'tipo de documento': tipo_doc,
                    'Numero de identificacion':num_id,
                    'Nombres':nombre,
                    'Apelido paterno':apellidop,
                    'Apelido materno':apellidom,
                    'Telefono':tel,
                    'Direccion':direc,
                    'Correo':email,
                    'Especialidad':espec,
                    'Usuario':usu,
                    'Contraseña':password,
                    'insertado': '200 Ok',
                    'error': 0}

    except Exception as e:
        error = 'No se ha podido insertar el registro.  ' + str(e)
        insertar = {'doctor': None,
                    'insertado': False,
                    'error': error}
    
    return Response(insertar)
