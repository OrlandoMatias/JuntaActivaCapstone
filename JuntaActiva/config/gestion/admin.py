from django.contrib import admin
from .models import Vecino, ProyectoVecinal, CertificadoResidencia, Actividad, Noticia


@admin.register(Vecino)
class VecinoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'email', 'es_miembro', 'fecha_inscripcion']
    search_fields = ['rut', 'nombre', 'apellido', 'email']
    list_filter = ['es_miembro', 'fecha_inscripcion']


@admin.register(ProyectoVecinal)
class ProyectoVecinalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'vecino', 'estado', 'fecha_postulacion']
    list_filter = ['estado', 'fecha_postulacion']
    search_fields = ['nombre', 'vecino__nombre', 'vecino__apellido']


@admin.register(CertificadoResidencia)
class CertificadoResidenciaAdmin(admin.ModelAdmin):
    list_display = ['vecino', 'fecha_solicitud', 'aprobado', 'codigo_certificado', 'pdf_generado']
    list_filter = ['aprobado', 'pdf_generado', 'fecha_solicitud']
    search_fields = ['vecino__nombre', 'vecino__apellido', 'codigo_certificado']


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'cupos', 'get_inscritos_count']
    list_filter = ['fecha']
    search_fields = ['nombre', 'descripcion']
    
    def get_inscritos_count(self, obj):
        return obj.inscritos.count()
    get_inscritos_count.short_description = 'Inscritos'


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha_publicacion']
    list_filter = ['fecha_publicacion']
    search_fields = ['titulo', 'autor', 'contenido']
    ordering = ['-fecha_publicacion']
