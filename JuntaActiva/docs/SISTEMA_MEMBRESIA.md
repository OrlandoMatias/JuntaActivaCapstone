# Sistema de Membresía

El sistema permite al administrador gestionar quiénes son miembros de la Junta de Vecinos. Solo los miembros pueden postular proyectos vecinales.

## Características

### Gestión de Miembros por el Administrador

El administrador puede:
- Ver la lista completa de vecinos registrados
- Ver el estado de membresía de cada vecino (Sí/No)
- Hacer miembro a un vecino con un clic
- Quitar la membresía a un vecino con un clic
- El vecino recibe un email automático al cambiar su estado

### Restricción para Postular Proyectos

- Solo los miembros pueden postular proyectos vecinales
- Los no miembros ven un mensaje de error al intentar postular
- Los no miembros son invitados a contactar a la administración

## Flujo de Membresía

### Hacer Miembro a un Vecino

1. Admin va a "Lista de Vecinos"
2. Admin hace clic en "Hacer Miembro"
3. Sistema confirma la acción
4. Sistema actualiza el estado del vecino
5. Sistema envía email de bienvenida al vecino
6. Vecino ahora puede postular proyectos

### Quitar Membresía

1. Admin va a "Lista de Vecinos"
2. Admin hace clic en "Quitar Membresía"
3. Sistema confirma la acción
4. Sistema actualiza el estado del vecino
5. Sistema envía email de notificación al vecino
6. Vecino ya no puede postular proyectos

## Emails Automáticos

### Email de Bienvenida (Nuevo Miembro)

Asunto: "Bienvenido como Miembro de la Junta de Vecinos"

Contenido:
```
Estimado/a [Nombre] [Apellido],

Felicitaciones! Ha sido registrado como MIEMBRO de la Junta de Vecinos.

Como miembro, ahora puede:
- Postular proyectos vecinales
- Participar en actividades exclusivas
- Acceder a beneficios especiales

Puede acceder a su cuenta en el sistema para comenzar a postular proyectos.

Bienvenido a la comunidad!

Saludos cordiales,
Junta de Vecinos
```

### Email de Actualización (Membresía Removida)

Asunto: "Estado de Membresía Actualizado"

Contenido:
```
Estimado/a [Nombre] [Apellido],

Le informamos que su estado de membresía en la Junta de Vecinos ha sido actualizado.

Actualmente NO es miembro activo de la junta.

Si tiene alguna consulta, por favor contacte a la administración.

Saludos cordiales,
Junta de Vecinos
```

## Restricción para No Miembros

Cuando un vecino que NO es miembro intenta postular un proyecto:

Mensaje de Error:
```
Usted no es miembro de la Junta de Vecinos. 
Solo los miembros pueden postular proyectos vecinales. 
Por favor, contacte a la administración para más información.
```

El vecino es redirigido a la página principal y no puede acceder al formulario de postulación.

## Interfaz de Administración

### Lista de Vecinos

La tabla muestra:

| RUT | Nombre | Apellido | Email | Teléfono | Dirección | Es Miembro | Acciones |
|-----|--------|----------|-------|----------|-----------|------------|----------|
| 12345678-9 | Juan | Pérez | juan@email.com | +56912345678 | Calle 123 | Sí | Quitar Membresía |
| 98765432-1 | María | González | maria@email.com | +56987654321 | Av. Principal 456 | No | Hacer Miembro |

### Botones de Acción

Para Miembros:
- Botón amarillo: "Quitar Membresía"
- Confirmación: "¿Está seguro de quitar la membresía a [Nombre]?"

Para No Miembros:
- Botón verde: "Hacer Miembro"
- Confirmación: "¿Está seguro de hacer miembro a [Nombre]?"

## Cómo Probar

### Paso 1: Acceder como Administrador
```
http://localhost:8000/login
Usuario: admin
Contraseña: [tu contraseña]
```

### Paso 2: Ver Lista de Vecinos
```
http://localhost:8000/vecinos/
```

### Paso 3: Hacer Miembro a un Vecino
1. Buscar un vecino con estado "No"
2. Hacer clic en "Hacer Miembro"
3. Confirmar la acción
4. Verificar mensaje: "[Nombre] ahora es miembro de la junta. Email enviado."
5. El vecino recibirá un email de bienvenida

### Paso 4: Probar Restricción
1. Cerrar sesión del admin
2. Iniciar sesión como el vecino que NO es miembro
3. Intentar ir a "Postular Proyecto"
4. Verificar mensaje de error

### Paso 5: Probar Acceso de Miembro
1. Cerrar sesión
2. Iniciar sesión como el vecino que SÍ es miembro
3. Ir a "Postular Proyecto"
4. Verificar acceso al formulario

## Base de Datos

### Campo en Modelo Vecino

```python
es_miembro = models.BooleanField(default=False)
```

Valores:
- True = Es miembro (puede postular proyectos)
- False = No es miembro (no puede postular proyectos)

Por defecto: Todos los vecinos nuevos NO son miembros hasta que el admin los active.

## Seguridad

### Validaciones Implementadas

1. Solo administradores pueden cambiar el estado de miembro
2. Confirmación antes de cambiar el estado
3. Validación en el backend (no solo frontend)
4. Redirección automática si no es miembro
5. Mensajes claros de error

### Permisos

| Acción | Vecino | Vecino Miembro | Admin |
|--------|--------|----------------|-------|
| Ver lista de vecinos | No | No | Sí |
| Cambiar estado de miembro | No | No | Sí |
| Postular proyecto | No | Sí | Sí |
| Ver sus propios proyectos | Sí | Sí | Sí |

## Archivos Modificados

### Backend
- `config/gestion/models.py` - Campo `es_miembro`
- `config/gestion/views.py` - Función `cambiar_estado_miembro()`
- `config/gestion/views.py` - Modificada función `postular_proyecto()`
- `config/gestion/urls.py` - Ruta `/vecinos/cambiar-miembro/<id>/`

### Frontend
- `config/gestion/templates/gestion/vecinos/lista.html` - Columna de acciones

## Beneficios

### Para Administradores
- Control total sobre quién puede postular proyectos
- Gestión simple con un clic
- Notificación automática a los vecinos
- Interfaz clara y fácil de usar

### Para Vecinos
- Reciben notificación cuando son hechos miembros
- Saben exactamente por qué no pueden postular
- Instrucciones claras para contactar a la administración
- Transparencia en el proceso

### Para la Junta de Vecinos
- Mejor control de membresía
- Proceso formal de postulación de proyectos
- Registro claro de quiénes son miembros
- Comunicación automática con los vecinos
