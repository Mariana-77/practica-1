from flask import Flask, render_template, request

app = Flask(__name__)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página Quiénes Somos
@app.route('/about')
def about():
    return render_template('about.html')

# Página Servicios
@app.route('/services')
def services():
    return render_template('services.html')

# Página Noticias
@app.route('/news')
def news():
    return render_template('news.html')

# Página de Contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Recoge los datos del formulario
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"Gracias por contactarnos, {name}! Te responderemos pronto."
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
