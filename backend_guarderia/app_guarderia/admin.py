from django.contrib import admin
from .models import *

@admin.register(PadreMadre)
class PadreMadreAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono_principal', 'dni')
    search_fields = ('nombre', 'apellido', 'dni')

@admin.register(PersonalGuarderia)
class PersonalGuarderiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cargo', 'email', 'telefono', 'turno')
    list_filter = ('cargo', 'turno')
    search_fields = ('nombre', 'apellido', 'dni')

@admin.register(GrupoNinos)
class GrupoNinosAdmin(admin.ModelAdmin):
    list_display = ('nombre_grupo', 'edad_minima', 'edad_maxima', 'id_personal_cargo', 'num_ninos_actual', 'capacidad_maxima')
    list_filter = ('edad_minima', 'edad_maxima')

@admin.register(Nino)
class NinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'genero', 'id_padre_madre_principal', 'grupo_asignado')
    list_filter = ('genero', 'grupo_asignado')
    search_fields = ('nombre', 'apellido')

@admin.register(ActividadGuarderia)
class ActividadGuarderiaAdmin(admin.ModelAdmin):
    list_display = ('nombre_actividad', 'horario', 'duracion_minutos', 'id_grupo', 'es_obligatoria')
    list_filter = ('id_grupo', 'es_obligatoria')
    search_fields = ('nombre_actividad',)

@admin.register(AsistenciaNino)
class AsistenciaNinoAdmin(admin.ModelAdmin):
    list_display = ('id_nino', 'fecha_asistencia', 'hora_entrada', 'hora_salida', 'estuvo_enfermo')
    list_filter = ('fecha_asistencia', 'estuvo_enfermo')
    date_hierarchy = 'fecha_asistencia'

@admin.register(PagoMensualidad)
class PagoMensualidadAdmin(admin.ModelAdmin):
    list_display = ('id_nino', 'fecha_pago', 'monto_pagado', 'metodo_pago', 'mes_correspondiente', 'estado_pago')
    list_filter = ('estado_pago', 'metodo_pago', 'mes_correspondiente')
    date_hierarchy = 'fecha_pago'