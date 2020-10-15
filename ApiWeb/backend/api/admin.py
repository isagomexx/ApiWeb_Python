from django.contrib import admin
from .models import Paciente, Doctor, GrupoFamilia, Examen, Cita, Incapacidad, Historial, FormulaMedica, Orden

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(GrupoFamilia)
admin.site.register(Examen)
admin.site.register(Cita)
admin.site.register(Incapacidad)
admin.site.register(Historial)
admin.site.register(FormulaMedica)
admin.site.register(Orden)