from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
import io
import os

# Flask-App initialisieren und templates-Verzeichnis ändern
app = Flask(__name__, template_folder=os.path.dirname(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    input1 = request.form.get('input1')
    input2 = request.form.get('input2')

    # PDF
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(100, 750, f"Eingabe 1: {input1}")
    c.drawString(100, 700, f"Eingabe 2: {input2}")
    c.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='output.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

