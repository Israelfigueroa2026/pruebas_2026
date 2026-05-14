from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000

USUARIOS = {
    'juan': {'contrasena': 'admin', 'rol': 'administrador'},
    'pepe': {'contrasena': 'user',  'rol': 'usuario'},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            nombre = request.form['nombre'].strip()
            edad   = int(request.form['edad'])
            tarros = int(request.form['tarros'])

            if not nombre:
                resultado = {'error': 'Por favor ingresa tu nombre.'}
            elif edad < 1 or edad > 120:
                resultado = {'error': 'Por favor ingresa una edad válida.'}
            elif tarros < 1:
                resultado = {'error': 'La cantidad de tarros debe ser al menos 1.'}
            else:
                total_sin_descuento = tarros * PRECIO_TARRO

                if edad < 18:
                    descuento_pct = 0
                elif 18 <= edad <= 30:
                    descuento_pct = 15
                else:
                    descuento_pct = 25

                total_con_descuento = total_sin_descuento * (1 - descuento_pct / 100)

                resultado = {
                    'nombre': nombre,
                    'edad': edad,
                    'total_sin_descuento': total_sin_descuento,
                    'descuento_pct': descuento_pct,
                    'total_con_descuento': total_con_descuento
                }
        except ValueError:
            resultado = {'error': 'Por favor ingresa valores válidos.'}

    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombre    = request.form['nombre'].strip().lower()
        contrasena = request.form['contrasena'].strip()

        if nombre in USUARIOS and USUARIOS[nombre]['contrasena'] == contrasena:
            rol = USUARIOS[nombre]['rol']
            resultado = {
                'ok': True,
                'mensaje': f'Bienvenido {rol} {nombre}'
            }
        else:
            resultado = {
                'ok': False,
                'mensaje': 'Usuario o contraseña incorrectos.'
            }

    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)