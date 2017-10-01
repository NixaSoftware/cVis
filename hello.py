from flask import Flask, render_template, request, flash, redirect, url_for
from flask_dropzone import Dropzone
import os
app = Flask(__name__)
dropzone = Dropzone(app)

app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '.txt, .clu'
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True

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
    # arqs = []
    if request.method == 'POST':

        # se arquivos vem do dataset
        if(request.form['name'] == 'dataset'):
            print("Oi! Você fez upload do dataset!")
            # cria diretorio uploaded na pasta atual, se já não existir
            if not os.path.exists(app.config['UPLOADED_PATH'] + '/dataset-uploaded'):
                os.makedirs(app.config['UPLOADED_PATH'] + '/dataset-uploaded')
            # loop over files since we allow multiple files
            for f in request.files.getlist('file'):
                # print para verificar erros no server
                print(request.files)
                #salva arquivos na pasta atual + /uploaded
                f.save(os.path.join(app.config['UPLOADED_PATH'] + '/dataset-uploaded', f.filename))

            # chamar algoritmos aqui

        # se arquivos vem do partition
        if(request.form['name'] == 'partition'):
            print("Oi! Você fez upload do partitions!")
            # cria diretorio uploaded na pasta atual, se já não existir
            if not os.path.exists(app.config['UPLOADED_PATH'] + '/partitions-uploaded'):
                os.makedirs(app.config['UPLOADED_PATH'] + '/partitions-uploaded')
            # loop over files since we allow multiple files
            for f in request.files.getlist('file'):
                # print para verificar erros no server
                print(request.files)
                #salva arquivos na pasta atual + /uploaded
                f.save(os.path.join(app.config['UPLOADED_PATH'] + '/partitions-uploaded', f.filename))

            # chama o loadClusters.py aqui

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
