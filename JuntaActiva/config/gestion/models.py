from django.db import models
from django.contrib.auth.models import User
import uuid


class Vecino(models.Model):
    """Modelo para representar a un vecino registrado en el sistema"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='vecino')
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    es_miembro = models.BooleanField(default=False)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"

    class Meta:
        verbose_name = "Vecino"
        verbose_name_plural = "Vecinos"


class ProyectoVecinal(models.Model):
    """Modelo para representar proyectos vecinales propuestos por vecinos"""
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_postulacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    vecino = models.ForeignKey(Vecino, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.get_estado_display()}"

    class Meta:
        verbose_name = "Proyecto Vecinal"
        verbose_name_plural = "Proyectos Vecinales"


class CertificadoResidencia(models.Model):
    """Modelo para representar solicitudes de certificados de residencia"""
    vecino = models.ForeignKey(Vecino, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)
    codigo_certificado = models.CharField(max_length=50, blank=True)
    pdf_generado = models.BooleanField(default=False)

    def generar_codigo_certificado(self):
        """Genera un código único para el certificado"""
        if not self.codigo_certificado:
            self.codigo_certificado = f"CERT-{uuid.uuid4().hex[:8].upper()}"
            self.save()
        return self.codigo_certificado

    def __str__(self):
        estado = "Aprobado" if self.aprobado else "Pendiente"
        return f"Certificado {self.vecino.nombre} {self.vecino.apellido} - {estado}"

    class Meta:
        verbose_name = "Certificado de Residencia"
        verbose_name_plural = "Certificados de Residencia"


class Actividad(models.Model):
    """Modelo para representar actividades comunitarias con cupos limitados"""
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    cupos = models.IntegerField()
    inscritos = models.ManyToManyField(Vecino, blank=True, related_name='actividades')

    def cupos_disponibles(self):
        """Verifica cuántos cupos están disponibles"""
        return self.cupos - self.inscritos.count()

    def tiene_cupos_disponibles(self):
        """Verifica si hay cupos disponibles"""
        return self.cupos_disponibles() > 0

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"


class Noticia(models.Model):
    """Modelo para representar noticias publicadas para la comunidad"""
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} - {self.fecha_publicacion}"

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha_publicacion']


class EspacioComunitario(models.Model):
    """Modelo para representar espacios comunitarios disponibles para reserva"""
    TIPO_CHOICES = [
        ('cancha', 'Cancha'),
        ('sala', 'Sala'),
        ('plaza', 'Plaza'),
    ]
    
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    capacidad = models.IntegerField(help_text="Capacidad máxima de personas")
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.nombre}"
    
    class Meta:
        verbose_name = "Espacio Comunitario"
        verbose_name_plural = "Espacios Comunitarios"


class ReservaEspacio(models.Model):
    """Modelo para representar reservas de espacios comunitarios"""
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
        ('cancelada', 'Cancelada'),
    ]
    
    HORARIO_CHOICES = [
        ('manana', 'Mañana (08:00 - 13:00)'),
        ('tarde', 'Tarde (13:00 - 18:00)'),
        ('noche', 'Noche (18:00 - 22:00)'),
        ('dia_completo', 'Día Completo (08:00 - 22:00)'),
    ]
    
    vecino = models.ForeignKey(Vecino, on_delete=models.CASCADE, related_name='reservas')
    espacio = models.ForeignKey(EspacioComunitario, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    horario = models.CharField(max_length=20, choices=HORARIO_CHOICES)
    motivo = models.TextField(help_text="Motivo de la reserva")
    cantidad_personas = models.IntegerField(help_text="Cantidad estimada de personas")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
    observaciones_admin = models.TextField(blank=True, help_text="Observaciones del administrador")
    
    def __str__(self):
        return f"{self.espacio.nombre} - {self.fecha} ({self.get_horario_display()}) - {self.get_estado_display()}"
    
    class Meta:
        verbose_name = "Reserva de Espacio"
        verbose_name_plural = "Reservas de Espacios"
        ordering = ['-fecha_solicitud']
        unique_together = ['espacio', 'fecha', 'horario', 'estado']
    
    def clean(self):
        """Validar que no exista otra reserva aprobada para el mismo espacio, fecha y horario"""
        from django.core.exceptions import ValidationError
        if self.estado == 'aprobada':
            reservas_existentes = ReservaEspacio.objects.filter(
                espacio=self.espacio,
                fecha=self.fecha,
                horario=self.horario,
                estado='aprobada'
            ).exclude(pk=self.pk)
            
            if reservas_existentes.exists():
                raise ValidationError(
                    f'Ya existe una reserva aprobada para {self.espacio.nombre} '
                    f'el {self.fecha} en horario {self.get_horario_display()}'
                )
