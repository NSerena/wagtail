
'''
crear películas

ejecutar:

python manage.py shell < datos/crear_peliculas.py
'''

from centros.models import Centro
import json
import os
# borrar centros
for p in Centro.objects.all():
    p.delete()

#lista de centros del json
if os.path.exists("datos/centros/centros.json"):
    pelis = json.load(open("datos/centros/centros.json", encoding='utf-8'))
else:
    pelis = json.load(open("centros.json", encoding='utf-8'))


for p1 in pelis:
    p = Centro()
    p.objectid = p1["objectid"]
    p.nombreCentro = p1["nombre_cen"]
    p.tipoCentro = p1["tipo_centr"]
    p.naturaleza = p1["naturaleza"]
    p.localidad = p1["localidad"]
    p.direccion = p1["direccion"]
    p.codpostal = p1["codpostal"]
    p.long = p1["longitud"]
    p.lat = p1["latitud"]
    p.save()