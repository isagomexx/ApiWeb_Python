from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Paciente, Doctor, GrupoFamilia, Examen, Cita, Incapacidad, Historial, FormulaMedica, Orden
from django.db import connection, transaction
from rest_framework import generics, permissions
from knox.models import AuthToken

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
        g= GrupoFamilia()
        d = Doctor()
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
        g.id_grupo_familiar = grupo_f
        d.id_doctor = doctor
        paciente.usuario = usu
        paciente.contrasena = password

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO paciente VALUES('%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s',%s,%s,'%s','%s')"
                            %(paciente.tipo_documento,paciente.numero_identificacion,paciente.nombres,paciente.apellido_paterno,
                            paciente.apellido_materno,paciente.telefono,paciente.direccion,paciente.correo,paciente.estrato,
                            paciente.fecha_nacimiento,g.id_grupo_familiar,d.id_doctor,paciente.usuario,paciente.contrasena))

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

@api_view(['POST'])
def registroHistoria(request):   
    id_histo = request.data.get('id_historial')
    id_paciente = request.data.get('id_paciente')
    sintomas = request.data.get('descripcion')
    diagnostico = request.data.get('diagnostico')
    antecedente = request.data.get('antecedente')
    evolucion = request.data.get('evolucion')
    tratamiento =request.data.get('tratamiento')

    try:
        
        historia = Historial()
        paciente = Paciente()
        historia.id_historial = id_histo
        paciente.id_paciente = id_paciente
        historia.descripcion = sintomas
        historia.diagnostico = diagnostico
        historia.antecedente = antecedente
        historia.evolucion = evolucion
        historia.tratamiento = tratamiento

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO historial (id_paciente,descripcion, diagnostico, antecedente, evolucion, tratamiento) VALUES (%s,'%s','%s','%s','%s','%s')"
                          %(paciente.id_paciente,historia.descripcion,historia.diagnostico,historia.antecedente, historia.evolucion, historia.tratamiento))

        insertarH = {'id historial': paciente.id_paciente,
                    'Descipcion de los sintomas':sintomas,
                    'Diagnostico':diagnostico,
                    'Antecedentes':antecedente,
                    'Evolucion del paciente':evolucion,
                    'Tratamiento':tratamiento,
                    'Paciente':id_paciente,
                    'insertado': '200 Ok',
                    'error': 0}

    except Exception as e:
        error = 'No se ha podido insertar el registro.  ' + str(e)
        insertarH = {'paciente': None,
                    'insertado': False,
                    'error': error}
    
    return Response(insertarH)    

