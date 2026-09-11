#Se importan las librerias que se utilizaran.
import requests
import json
import os
#Pedimos al usuario que ingrese el nombre o numero de pokemon
solicitud_pokemon = input ('Ingresa Nombre O Numero de Pokemon: ').strip().lower()
#Declaramos el url de pokeapi de donde saldra la informacion de los pokemon.
url = f"https://pokeapi.co/api/v2/pokemon/{solicitud_pokemon}"
#Declaramos la variable "resultados" donde se guardara la informacion solicitada a pokeapi.
resultado = requests.get(url)

if resultado.status_code == 200:
#el resultado se manda a la variable "datos"
    datos =  resultado.json()
#se guarda la informacion del pokemon en la variable "datos" para despues hacer una impresion de la informacion.
    nombre = datos ['name'].capitalize()
    peso = datos['weight']
    tamaño = datos ['height']
    imagen = datos['sprites']['front_default']
    tipo = [t['type']['name'] for t in datos['types']]
    habilidades = [a['ability']['name'] for a in datos ['abilities']]
    movimientos = [m['move']['name'] for m in datos ['moves']]
    print (f"\n ¡Tu Pokemon es '{nombre}'!")
    print(f"Apariencia: {imagen}")
    print (f"Peso: {peso}")
    print (f"Tamaño: {tamaño}")
    print (f"Tipo: {', '.join(tipo)}")
    print (f"Habilidades: {', '.join(habilidades)}")
    print(f"Movimientos ({len(movimientos)} en total): {', '.join(movimientos[:5])}...")
#se guardan la informacion del pokemon en un archivo .json.
    informacion = {
            "Imagen": imagen,
            "Nombre": nombre,
            "Peso": peso,
            "Tipo": tipo,
            "Habilidades": habilidades,
            "Movimientos": movimientos
    }
    #Se asegura de que la carpeta "pokedex" exista.
    os.makedirs("pokedex", exist_ok=True)
    archivo_nombre= f"pokedex/{datos['name'].lower()}.json"
    with open (archivo_nombre, "w",encoding="utf-8") as archivo:
            json.dump(informacion,archivo, indent=4, ensure_ascii=False)
            print(f"\n Guardado correctamente en '{archivo_nombre}'")
            ruta_absoluta = os.path.abspath(archivo_nombre)
            print(f"Ubicación exacta del archivo: {ruta_absoluta}")
#se valuan los errores y se imprime un mensaje en caso de surgir.
elif resultado.status_code == 404:
    print(f"\nError: Tu Pokemon '{solicitud_pokemon}' no existe. Revisa el nombre.")
else:
    print(f"\nOcurrió un error: {resultado.status_code}")