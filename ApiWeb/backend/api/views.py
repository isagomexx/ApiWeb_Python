from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Paciente, Doctor, GrupoFamilia, Examen, Cita, Incapacidad, Historial, FormulaMedica, Orden
from django.db import connection, transaction

@api_view(['POST'])
def registroDoctor(request):
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

@api_view(['POST'])
def registroGrupoFam(request):
    id_grupo_fam = request.data.get('id_grupo_familia')
    nom = request.data.get('nombre')

    try:
        grupoF = GrupoFamilia()
        grupoF.id_grupo_familia = id_grupo_fam
        grupoF.nombre = nom
        grupoF.save()

        insertarG = {
            'ID Grupo Familiar': grupoF.id_grupo_familia,
            'Nombre Grupo Familiar': nom,
            'Insertado': 'Ok',
            'error': 0
        }
    except Exception as e:
        error = 'No se ha podido insertar el registro.  ' + str(e)
        insertarG = {'Grupo Familiar': None,
                    'insertado': False,
                    'error': error}

    return Response(insertarG)

@api_view(['POST'])
def registroPaciente(request):
    # id_grupo_fam = request.data.get('id_grupo_familia')
    # nom = request.data.get('nombre')

    # try:
    #     grupoF = GrupoFamilia()
    #     grupoF.id_grupo_familia = id_grupo_fam
    #     grupoF.nombre = nom
    #     with connection.cursor() as cursor:
        
    #         cursor.execute("INSERT INTO grupo_familia VALUES(%s,'%s')"%(grupoF.id_grupo_familia,grupoF.nombre))

    #         insertarG = {
    #             'ID Grupo Familiar': grupoF.id_grupo_familia,
    #             'Nombre Grupo Familiar': nom,
    #             'Insertado': 'Ok',
    #             'error': 0
    #         }
    # except Exception as e:
    #     error = 'No se ha podido insertar el registro.  ' + str(e)
    #     insertarG = {'Grupo Familiar': None,
    #                 'insertado': False,
    #                 'error': error}

    # return Response(insertarG)
        
    tipo_doc = request.data.get('tipo_documento')
    num_id = request.data.get('numero_identificacion')
    nombre = request.data.get('nombres')
    apellidop = request.data.get('apellido_paterno')
    apellidom = request.data.get('apellido_materno')
    tel = request.data.get('telefono')
    direc = request.data.get('direccion')
    email = request.data.get('correo')
    est = request.data.get('estrato')
    fec_nac = request.data.get('fecha_nacimiento')
    grupo_f = request.data.get('id_grupo_familiar')
    doctor = request.data.get('id_doctor')
    usu = request.data.get('usuario')
    password = request.data.get('contrasena')

    try:
        paciente = Paciente()
        paciente.tipo_documento = tipo_doc
        paciente.numero_identificacion = num_id
        paciente.nombres = nombre
        paciente.apellido_paterno = apellidop
        paciente.apellido_materno = apellidom
        paciente.telefono = tel
        paciente.direccion = direc
        paciente.correo = email
        paciente.estrato = est
        paciente.fecha_nacimiento = fec_nac
        paciente.id_grupo_familiar = grupo_f
        paciente.id_doctor = doctor
        paciente.usuario = usu
        paciente.contrasena = password

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO grupo_familia VALUES('%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s',%s,%s,'%s','%s')"
                            %(paciente.tipo_documento,paciente.numero_identificacion,paciente.nombres,paciente.apellido_paterno,
                            paciente.apellido_materno,paciente.telefono,paciente.direccion,paciente.correo,paciente.estrato,
                            paciente.fecha_nacimiento,paciente.id_grupo_familiar,paciente.id_doctor,paciente.usuario,paciente.contrasena))

        insertarP = {'tipo de documento': tipo_doc,
                    'Numero de identificacion':num_id,
                    'Nombres':nombre,
                    'Apelido paterno':apellidop,
                    'Apelido materno':apellidom,
                    'Telefono':tel,
                    'Direccion':direc,
                    'Correo':email,
                    'Estrato':est,
                    'Fecha de Nacimiento':fec_nac,
                    'Grupo Familiar':grupo_f,
                    'Doctor':doctor,
                    'Usuario':usu,
                    'Contraseña':password,
                    'insertado': '200 Ok',
                    'error': 0}

    except Exception as e:
        error = 'No se ha podido insertar el registro.  ' + str(e)
        insertarP = {'paciente': None,
                    'insertado': False,
                    'error': error}
    
    return Response(insertarP)