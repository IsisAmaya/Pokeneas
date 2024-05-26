from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)
port =  8000

# Arreglo de Pokeneas
pokeneas = [
    {'id': 1, 'nombre': 'Spectrox', 'altura': 150, 'habilidad': 'Camuflaje nocturno', 'imagen': 'https://storage.googleapis.com/pokeneea/1.webp', 'frase': 'En la oscuridad, encuentra tu luz.'},
    {'id': 2, 'nombre': 'Florantus', 'altura': 140, 'habilidad': 'Regeneración solar', 'imagen': 'https://storage.googleapis.com/pokeneea/2.webp', 'frase': 'Crecer es cambiar, y cambiar es desafiante pero hermoso.'},
    {'id': 3, 'nombre': 'Stegon', 'altura': 160, 'habilidad': 'Armadura de espinas', 'imagen': 'https://storage.googleapis.com/pokeneea/3.webp', 'frase': 'La protección es más fuerte en las raíces de nuestra existencia.'},
    {'id': 4, 'nombre': 'Aquariunix', 'altura': 120, 'habilidad': 'Manipulación de agua', 'imagen': 'https://storage.googleapis.com/pokeneea/4.webp', 'frase': 'Fluye como el agua, inquebrantable y libre.'},
    {'id': 5, 'nombre': 'Mysticat', 'altura': 110, 'habilidad': 'Visión nocturna', 'imagen': 'https://storage.googleapis.com/pokeneea/5.webp', 'frase': 'Mira más allá de lo visible para encontrar la verdad.'},
    {'id': 6, 'nombre': 'Shadowrend', 'altura': 140, 'habilidad': 'Velocidad sombría', 'imagen': 'https://storage.googleapis.com/pokeneea/6.webp', 'frase': 'El miedo es sólo una sombra que pasa.'},
    {'id': 7, 'nombre': 'Chromadillo', 'altura': 120, 'habilidad': 'Cambio de color', 'imagen': 'https://storage.googleapis.com/pokeneea/7.webp', 'frase': 'El cambio no es solo necesario; es bello.'},
    {'id': 8, 'nombre': 'Lunispike', 'altura': 145, 'habilidad': 'Reflexión lunar', 'imagen': 'https://storage.googleapis.com/pokeneea/8.webp', 'frase': 'Refleja lo que deseas ser, no lo que temes.'},
    {'id': 9, 'nombre': 'Gaiaston', 'altura': 150, 'habilidad': 'Clonación', 'imagen': 'https://storage.googleapis.com/pokeneea/9.webp', 'frase': 'Firme como una roca, libre como la tierra.'},
    {'id': 10, 'nombre': 'Prismalux', 'altura': 130, 'habilidad': 'Prisma de luz', 'imagen': 'https://storage.googleapis.com/pokeneea/10.webp', 'frase': 'La luz se encuentra en todas las perspectivas.'},
]

# Ruta que devuelve un JSON con información de un Pokenea aleatorio
@app.route('/pokenea/json')
def pokenea_json():
    pokenea = random.choice(pokeneas)
    return jsonify({
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        'contenedor_id': 'ID_DEL_CONTENEDOR'  # Suponiendo que se obtenga de otra manera
    })

# Ruta que muestra por pantalla la imagen y frase de un Pokenea aleatorio
@app.route('/pokenea/display')
def pokenea_display():
    pokenea = random.choice(pokeneas)
    return render_template('display.html', pokenea=pokenea, contenedor_id='ID_DEL_CONTENEDOR')

if __name__ == '__main__':
    app.run(debug=True,
            host="0.0.0.0", port=port
            )
    
