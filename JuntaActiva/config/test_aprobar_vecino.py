"""
Script para probar la aprobación de un vecino
"""
from gestion.models import Vecino

# Obtener el vecino pendiente
vecino = Vecino.objects.get(rut='12.345.678-9')
print(f"Vecino antes: {vecino.nombre} {vecino.apellido}")
print(f"Es miembro: {vecino.es_miembro}")

# Cambiar estado
vecino.es_miembro = not vecino.es_miembro
vecino.save()

print(f"\nVecino después:")
print(f"Es miembro: {vecino.es_miembro}")
print("\n✅ Cambio realizado exitosamente")
