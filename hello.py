from flask import Flask, render_template, request, flash, redirect, url_for
from flask_dropzone import Dropzone
import os
app = Flask(__name__)
dropzone = Dropzone(app)

app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '.txt, .clu'

# get the current folder
app.config['UPLOADED_PATH'] = os.getcwd()

# essa variável serve pra gente não ter que ficar rodando
# o servidor de novo toda hora
# por via das dúvidas dá um export nela tbm
DEBUG = True

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload():
    arqs = []
    if request.method == 'POST':
        data = request.data
         # loop over files since we allow multiple files
        for f in request.files.getlist('file'):
            print(request.files)
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
            arqs.append(f)
        # chamar algoritmos aqui
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
