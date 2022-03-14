
'''
crear películas

ejecutar:

python manage.py shell < datos/crear_peliculas.py
'''

from centros.models import Centro
import json
import os
# borrar centros
for c in Centro.objects.all():
    c.delete()

#lista de centros del json
if os.path.exists("datos/centros/centros.json"):
    centros = json.load(open("datos/centros/centros.json", encoding='utf-8'))
else:
    centros = json.load(open("centros.json", encoding='utf-8'))


for c1 in centros:
    c = Centro()
    c.objectid = c1["objectid"]
    c.nombreCentro = c1["nombre_cen"]
    c.tipoCentro = c1["tipo_centr"]
    c.naturaleza = c1["naturaleza"]
    c.localidad = c1["localidad"]
    c.direccion = c1["direccion"]
    c.codpostal = c1["codpostal"]
    c.long = c1["longitud"]
    c.lat = c1["latitud"]
    c.save()