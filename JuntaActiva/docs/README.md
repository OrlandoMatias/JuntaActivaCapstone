# Documentación del Sistema

Esta carpeta contiene toda la documentación técnica y guías del Sistema de Gestión Vecinal.

## Índice de Documentos

### Configuración e Instalación

- **BASE_DE_DATOS.md** - Configuración de MySQL/SQLite, instalación de XAMPP, backup y restauración
- **CONFIGURAR_EMAIL.md** - Configuración de envío de emails con Gmail/Outlook

### Desarrollo

- **DESARROLLO.md** - Guía completa para desarrolladores, estructura del proyecto, modelos, vistas, testing

### Funcionalidades del Sistema

- **SISTEMA_MEMBRESIA.md** - Sistema de membresía, gestión de miembros, restricciones
- **SISTEMA_RESERVAS.md** - Sistema de reservas de espacios comunitarios, calendario, validaciones

## Guía Rápida

### Para Usuarios Nuevos

1. Leer `../README.md` (documento principal)
2. Seguir pasos de instalación
3. Configurar base de datos (ver `BASE_DE_DATOS.md`)
4. Configurar email (ver `CONFIGURAR_EMAIL.md`)

### Para Desarrolladores

1. Leer `DESARROLLO.md` para entender la estructura
2. Configurar entorno de desarrollo
3. Revisar modelos y vistas existentes
4. Seguir buenas prácticas de código

### Para Administradores

1. Leer `SISTEMA_MEMBRESIA.md` para gestión de miembros
2. Leer `SISTEMA_RESERVAS.md` para gestión de espacios
3. Configurar espacios comunitarios en el admin
4. Gestionar solicitudes de vecinos

## Estructura de Documentación

```
docs/
├── README.md                  # Este archivo (índice)
├── BASE_DE_DATOS.md          # Configuración de BD
├── CONFIGURAR_EMAIL.md       # Configuración de emails
├── DESARROLLO.md             # Guía de desarrollo
├── SISTEMA_MEMBRESIA.md      # Sistema de membresía
└── SISTEMA_RESERVAS.md       # Sistema de reservas
```

## Documentos Adicionales

Algunos documentos específicos pueden encontrarse en:
- `config/` - Scripts de configuración y verificación
- `../README.md` - Documentación principal del proyecto

## Contribuir a la Documentación

Al agregar nuevas funcionalidades:

1. Actualizar el documento correspondiente en `docs/`
2. Actualizar este índice si se crea un nuevo documento
3. Mantener formato consistente
4. Incluir ejemplos de código cuando sea relevante
5. Documentar solución de problemas comunes

## Convenciones

- Usar Markdown para todos los documentos
- Incluir ejemplos de código con sintaxis resaltada
- Organizar contenido con encabezados claros
- Incluir tabla de contenidos en documentos largos
- Mantener lenguaje claro y conciso
