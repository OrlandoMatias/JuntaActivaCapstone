# 📅 Sistema de Reservas de Espacios Comunitarios

## ✅ Funcionalidad Implementada

Sistema completo para gestionar reservas de canchas, salas y plazas comunitarias con calendario, validaciones y notificaciones por email.

---

## 🎯 Características Principales

### 1. Gestión de Espacios Comunitarios

**Tipos de Espacios:**
- 🏀 Canchas
- 🏢 Salas
- 🌳 Plazas

**Información de cada espacio:**
- Nombre
- Tipo
- Descripción
- Capacidad máxima
- Estado (activo/inactivo)

### 2. Sistema de Reservas

**Horarios Disponibles:**
- 🌅 Mañana (08:00 - 13:00)
- ☀️ Tarde (13:00 - 18:00)
- 🌙 Noche (18:00 - 22:00)
- 📅 Día Completo (08:00 - 22:00)

**Estados de Reserva:**
- ⏳ Pendiente - Esperando aprobación del admin
- ✅ Aprobada - Confirmada por el admin
- ❌ Rechazada - No aprobada por el admin
- 🚫 Cancelada - Cancelada por el vecino

### 3. Validaciones Automáticas

✅ **No se pueden hacer reservas duplicadas** - Un espacio solo puede tener una reserva aprobada por fecha y horario
✅ **Fechas futuras** - Solo se pueden reservar fechas iguales o posteriores a hoy
✅ **Capacidad del espacio** - La cantidad de personas no puede exceder la capacidad máxima
✅ **Espacios activos** - Solo se muestran espacios activos para reservar

---

## 📧 Emails Automáticos

### Email de Aprobación ✅

**Asunto:** "✅ Reserva de Espacio Aprobada"

**Contenido:**
```
Estimado/a [Nombre] [Apellido],

¡Excelentes noticias! Su solicitud de reserva ha sido APROBADA.

📋 Detalles de la Reserva:
- Espacio: Cancha de Fútbol (Cancha)
- Fecha: 20 de noviembre de 2024
- Horario: Tarde (13:00 - 18:00)
- Motivo: Partido amistoso
- Cantidad de personas: 22

Por favor, recuerde:
✅ Llegar puntualmente
✅ Respetar el horario asignado
✅ Dejar el espacio limpio y ordenado
✅ Cumplir con las normas de uso del espacio

¡Que disfrute del espacio!

Saludos cordiales,
Junta de Vecinos
```

### Email de Rechazo ❌

**Asunto:** "❌ Reserva de Espacio Rechazada"

**Contenido:**
```
Estimado/a [Nombre] [Apellido],

Lamentamos informarle que su solicitud de reserva ha sido RECHAZADA.

📋 Detalles de la Solicitud:
- Espacio: Sala Multiuso (Sala)
- Fecha: 20 de noviembre de 2024
- Horario: Noche (18:00 - 22:00)
- Motivo: Reunión comunitaria

Para más información sobre los motivos del rechazo o para realizar una nueva solicitud,
por favor contacte a la junta de vecinos.

Saludos cordiales,
Junta de Vecinos
```

---

## 🔄 Flujo de Reserva

### Para Vecinos:

```
1. Vecino ve calendario de disponibilidad
   ↓
2. Vecino selecciona espacio, fecha y horario
   ↓
3. Vecino llena formulario de solicitud
   ↓
4. Sistema valida disponibilidad
   ↓
5. Solicitud queda en estado "Pendiente"
   ↓
6. Admin revisa y aprueba/rechaza
   ↓
7. Vecino recibe email con resultado
   ↓
8. Vecino puede ver sus reservas
```

### Para Administradores:

```
1. Admin ve todas las solicitudes pendientes
   ↓
2. Admin revisa detalles de cada solicitud
   ↓
3. Admin aprueba o rechaza
   ↓
4. Sistema envía email automático al vecino
   ↓
5. Sistema actualiza calendario
```

---

## 🖥️ Vistas Disponibles

### Para Vecinos:

1. **Listar Espacios** (`/reservas/espacios/`)
   - Ver todos los espacios disponibles
   - Información de cada espacio

2. **Calendario de Reservas** (`/reservas/calendario/`)
   - Ver disponibilidad por fecha
   - Ver qué espacios están ocupados
   - Seleccionar fecha para ver disponibilidad

3. **Solicitar Reserva** (`/reservas/solicitar/`)
   - Formulario para solicitar reserva
   - Validación en tiempo real
   - Selección de espacio, fecha, horario

4. **Mis Reservas** (`/reservas/mis-reservas/`)
   - Ver todas sus reservas
   - Estados: Pendiente, Aprobada, Rechazada, Cancelada
   - Opción de cancelar reservas

### Para Administradores:

5. **Gestionar Reservas** (`/reservas/gestionar/`)
   - Ver todas las solicitudes
   - Filtrar por estado
   - Aprobar o rechazar solicitudes

---

## 📋 Formulario de Solicitud

**Campos requeridos:**
- **Espacio:** Selección de espacio disponible
- **Fecha:** Calendario (solo fechas futuras)
- **Horario:** Mañana, Tarde, Noche o Día Completo
- **Motivo:** Descripción del uso del espacio
- **Cantidad de Personas:** Número estimado

**Validaciones:**
- ✅ Fecha no puede ser en el pasado
- ✅ Cantidad de personas > 0
- ✅ Cantidad no excede capacidad del espacio
- ✅ No existe otra reserva aprobada para mismo espacio/fecha/horario

---

## 🗓️ Calendario de Disponibilidad

**Características:**
- Ver disponibilidad por fecha
- Selector de fecha
- Tabla con todos los espacios
- Indicador visual de disponibilidad:
  - 🟢 Verde = Disponible
  - 🔴 Rojo = Ocupado (muestra quién reservó)

**Ejemplo de Vista:**

| Espacio | Mañana | Tarde | Noche | Día Completo |
|---------|--------|-------|-------|--------------|
| Cancha Fútbol | 🟢 Disponible | 🔴 Reservado por Juan Pérez | 🟢 Disponible | 🔴 No disponible |
| Sala Multiuso | 🟢 Disponible | 🟢 Disponible | 🟢 Disponible | 🟢 Disponible |
| Plaza Central | 🔴 Reservado por María González | 🟢 Disponible | 🟢 Disponible | 🔴 No disponible |

---

## 🔒 Seguridad y Permisos

### Validaciones de Seguridad:

1. ✅ Solo usuarios autenticados pueden reservar
2. ✅ Solo el vecino dueño puede ver sus reservas
3. ✅ Solo el vecino dueño puede cancelar sus reservas
4. ✅ Solo administradores pueden aprobar/rechazar
5. ✅ Validación de duplicados en base de datos
6. ✅ Constraint único en BD (espacio + fecha + horario + estado)

### Permisos por Rol:

| Acción | Vecino | Admin |
|--------|--------|-------|
| Ver espacios | ✅ | ✅ |
| Ver calendario | ✅ | ✅ |
| Solicitar reserva | ✅ | ✅ |
| Ver mis reservas | ✅ | ✅ |
| Cancelar mi reserva | ✅ | ✅ |
| Ver todas las reservas | ❌ | ✅ |
| Aprobar/Rechazar | ❌ | ✅ |

---

## 🗄️ Modelos de Base de Datos

### EspacioComunitario

```python
- nombre: CharField
- tipo: CharField (cancha/sala/plaza)
- descripcion: TextField
- capacidad: IntegerField
- activo: BooleanField
```

### ReservaEspacio

```python
- vecino: ForeignKey(Vecino)
- espacio: ForeignKey(EspacioComunitario)
- fecha: DateField
- horario: CharField (manana/tarde/noche/dia_completo)
- motivo: TextField
- cantidad_personas: IntegerField
- estado: CharField (pendiente/aprobada/rechazada/cancelada)
- fecha_solicitud: DateTimeField
- fecha_respuesta: DateTimeField
- observaciones_admin: TextField
```

**Constraint Único:**
- Un espacio solo puede tener UNA reserva aprobada por fecha y horario

---

## 🧪 Cómo Probar

### Paso 1: Crear Espacios (Admin)

Primero necesitas crear espacios en el admin de Django:

```bash
http://localhost:8000/admin/gestion/espaciocomunitario/
```

**Ejemplos de espacios:**
1. Cancha de Fútbol - Tipo: Cancha - Capacidad: 30
2. Sala Multiuso - Tipo: Sala - Capacidad: 50
3. Plaza Central - Tipo: Plaza - Capacidad: 100

### Paso 2: Ver Calendario (Vecino)

```
http://localhost:8000/reservas/calendario/
```

- Selecciona una fecha
- Ve la disponibilidad de cada espacio

### Paso 3: Solicitar Reserva (Vecino)

```
http://localhost:8000/reservas/solicitar/
```

- Selecciona espacio
- Selecciona fecha y horario
- Describe el motivo
- Indica cantidad de personas
- Envía solicitud

### Paso 4: Gestionar Reservas (Admin)

```
http://localhost:8000/reservas/gestionar/
```

- Ve todas las solicitudes pendientes
- Aprueba o rechaza
- El vecino recibe email automático

### Paso 5: Ver Mis Reservas (Vecino)

```
http://localhost:8000/reservas/mis-reservas/
```

- Ve todas tus reservas
- Estados y detalles
- Opción de cancelar

---

## 📊 Estados de Reserva

### Pendiente ⏳
- Solicitud recién creada
- Esperando revisión del admin
- Vecino puede cancelar

### Aprobada ✅
- Admin aprobó la solicitud
- Espacio reservado
- Vecino recibe email de confirmación
- Vecino puede cancelar (libera el espacio)

### Rechazada ❌
- Admin rechazó la solicitud
- Espacio no reservado
- Vecino recibe email con notificación
- No se puede modificar

### Cancelada 🚫
- Vecino canceló su reserva
- Espacio liberado
- No se puede reactivar

---

## 🔍 Monitoreo

### En la Consola del Servidor:

**Reserva Aprobada:**
```
✓ Email de aprobación enviado a vecino@email.com
```

**Reserva Rechazada:**
```
✓ Email de rechazo enviado a vecino@email.com
```

**Intento de Reserva Duplicada:**
```
ValidationError: Ya existe una reserva aprobada para Cancha de Fútbol el 20/11/2024 en horario Tarde
```

### En el Navegador:

**Solicitud Enviada:**
```
✓ Solicitud de reserva enviada exitosamente. Será revisada por un administrador.
```

**Reserva Aprobada:**
```
✓ Reserva aprobada exitosamente. Email enviado al vecino.
```

**Reserva Rechazada:**
```
✓ Reserva rechazada. Se ha notificado al vecino.
```

**Reserva Cancelada:**
```
✓ Reserva cancelada exitosamente.
```

---

## ✨ Beneficios del Sistema

### Para Vecinos:
- ✅ Pueden ver disponibilidad en tiempo real
- ✅ Proceso simple de solicitud
- ✅ Reciben notificaciones por email
- ✅ Pueden gestionar sus propias reservas
- ✅ Transparencia en el proceso

### Para Administradores:
- ✅ Control centralizado de reservas
- ✅ Evita conflictos de horarios
- ✅ Notificaciones automáticas
- ✅ Historial completo de reservas
- ✅ Validaciones automáticas

### Para la Junta de Vecinos:
- ✅ Mejor uso de espacios comunitarios
- ✅ Registro formal de reservas
- ✅ Reducción de conflictos
- ✅ Comunicación efectiva
- ✅ Sistema profesional

---

## 📝 Archivos Creados/Modificados

### Backend:
- ✅ `config/gestion/models.py` - Modelos EspacioComunitario y ReservaEspacio
- ✅ `config/gestion/forms.py` - Formulario ReservaEspacioForm
- ✅ `config/gestion/views.py` - 8 nuevas vistas para reservas
- ✅ `config/gestion/urls.py` - 8 nuevas rutas
- ✅ `config/gestion/migrations/0003_*.py` - Migración de BD

### Frontend (Pendiente):
- ⏳ `templates/gestion/reservas/espacios.html`
- ⏳ `templates/gestion/reservas/solicitar.html`
- ⏳ `templates/gestion/reservas/mis_reservas.html`
- ⏳ `templates/gestion/reservas/gestionar.html`
- ⏳ `templates/gestion/reservas/calendario.html`

---

## 🚀 Próximos Pasos

### 1. Crear Plantillas HTML
Necesitas crear las plantillas en la carpeta `templates/gestion/reservas/`

### 2. Crear Espacios Iniciales
Usa el admin de Django para crear los espacios comunitarios

### 3. Probar el Sistema
- Solicitar reservas como vecino
- Aprobar/rechazar como admin
- Verificar emails

---

## 🎉 Estado Actual

### ✅ Backend Completo

- ✅ Modelos creados y migrados
- ✅ Formularios con validaciones
- ✅ Vistas implementadas
- ✅ Rutas configuradas
- ✅ Emails automáticos
- ✅ Validaciones de seguridad

### ⏳ Pendiente

- ⏳ Crear plantillas HTML
- ⏳ Agregar estilos CSS
- ⏳ Crear espacios iniciales

---

## 📚 Documentación Adicional

Para más información sobre:
- Configuración de emails: Ver `CONFIGURAR_EMAIL.md`
- Sistema de membresía: Ver `SISTEMA_MEMBRESIA.md`
- Emails de proyectos: Ver `EMAILS_PROYECTOS.md`

---

¡El sistema de reservas está listo para usar una vez que se creen las plantillas HTML!
