from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Vecino, ProyectoVecinal, CertificadoResidencia, Actividad, Noticia, EspacioComunitario, ReservaEspacio
import re
from datetime import date


class VecinoForm(forms.ModelForm):
    """Formulario para registro de vecinos con creación de usuario"""
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=6,
        help_text='Mínimo 6 caracteres'
    )
    password_confirm = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Vecino
        fields = ['rut', 'nombre', 'apellido', 'email', 'telefono', 'direccion']
        labels = {
            'rut': 'RUT',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12.345.678-9'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56912345678'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean_email(self):
        """Validación adicional de formato de email"""
        email = self.cleaned_data.get('email')
        if email:
            # Validación de formato de email
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                raise ValidationError('Por favor ingrese un correo electrónico válido.')
            # Verificar que el email no esté en uso
            if User.objects.filter(email=email).exists():
                raise ValidationError('Este correo electrónico ya está registrado.')
        return email
    
    def clean_rut(self):
        """Validación de RUT único"""
        rut = self.cleaned_data.get('rut')
        if Vecino.objects.filter(rut=rut).exists():
            raise ValidationError('Este RUT ya está registrado.')
        return rut
    
    def clean(self):
        """Validación de contraseñas coincidentes"""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Las contraseñas no coinciden.')
        
        return cleaned_data


class ProyectoForm(forms.ModelForm):
    """Formulario para postulación de proyectos vecinales (sin campo vecino)"""
    
    class Meta:
        model = ProyectoVecinal
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre del Proyecto',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class CertificadoForm(forms.ModelForm):
    """Formulario para solicitud de certificados de residencia (sin campo vecino)"""
    
    class Meta:
        model = CertificadoResidencia
        fields = []  # No hay campos, se usa el vecino del usuario actual


class ActividadForm(forms.ModelForm):
    """Formulario para creación de actividades comunitarias"""
    
    class Meta:
        model = Actividad
        fields = ['nombre', 'descripcion', 'fecha', 'cupos']
        labels = {
            'nombre': 'Nombre de la Actividad',
            'descripcion': 'Descripción',
            'fecha': 'Fecha',
            'cupos': 'Cupos Disponibles',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cupos': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }
    
    def clean_cupos(self):
        """Validación de cupos mayor a cero"""
        cupos = self.cleaned_data.get('cupos')
        if cupos is not None and cupos <= 0:
            raise ValidationError('El número de cupos debe ser mayor a cero.')
        return cupos


class NoticiaForm(forms.ModelForm):
    """Formulario para creación de noticias"""
    
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'autor']
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'autor': 'Autor',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
        }



class ReservaEspacioForm(forms.ModelForm):
    """Formulario para solicitud de reserva de espacios comunitarios"""
    
    class Meta:
        model = ReservaEspacio
        fields = ['espacio', 'fecha', 'horario', 'motivo', 'cantidad_personas']
        labels = {
            'espacio': 'Espacio a Reservar',
            'fecha': 'Fecha de Reserva',
            'horario': 'Horario',
            'motivo': 'Motivo de la Reserva',
            'cantidad_personas': 'Cantidad de Personas',
        }
        widgets = {
            'espacio': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min': date.today().isoformat()}),
            'horario': forms.Select(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describa el motivo de su reserva'}),
            'cantidad_personas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'placeholder': 'Ej: 20'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo espacios activos
        self.fields['espacio'].queryset = EspacioComunitario.objects.filter(activo=True)
    
    def clean_fecha(self):
        """Validar que la fecha sea futura"""
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha < date.today():
            raise ValidationError('La fecha de reserva debe ser igual o posterior a hoy.')
        return fecha
    
    def clean_cantidad_personas(self):
        """Validar cantidad de personas"""
        cantidad = self.cleaned_data.get('cantidad_personas')
        if cantidad is not None and cantidad <= 0:
            raise ValidationError('La cantidad de personas debe ser mayor a cero.')
        return cantidad
    
    def clean(self):
        """Validar que no exista otra reserva aprobada para el mismo espacio, fecha y horario"""
        cleaned_data = super().clean()
        espacio = cleaned_data.get('espacio')
        fecha = cleaned_data.get('fecha')
        horario = cleaned_data.get('horario')
        cantidad_personas = cleaned_data.get('cantidad_personas')
        
        if espacio and fecha and horario:
            # Verificar si ya existe una reserva aprobada
            reservas_existentes = ReservaEspacio.objects.filter(
                espacio=espacio,
                fecha=fecha,
                horario=horario,
                estado='aprobada'
            )
            
            if reservas_existentes.exists():
                raise ValidationError(
                    f'Ya existe una reserva aprobada para {espacio.nombre} '
                    f'el {fecha.strftime("%d/%m/%Y")} en horario {dict(ReservaEspacio.HORARIO_CHOICES)[horario]}. '
                    f'Por favor, seleccione otra fecha u horario.'
                )
        
        # Validar capacidad del espacio
        if espacio and cantidad_personas:
            if cantidad_personas > espacio.capacidad:
                raise ValidationError(
                    f'La cantidad de personas ({cantidad_personas}) excede la capacidad máxima '
                    f'del espacio ({espacio.capacidad} personas).'
                )
        
        return cleaned_data
