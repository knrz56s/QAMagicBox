from flask import Flask, Blueprint, render_template, redirect, url_for, request, session, flash
import requests

from fi import fi_bp

app = Flask(
    __name__,
    #template_folder='templates',
    static_folder='static',
    static_url_path='/'
)
app.secret_key='any'

app.register_blueprint(fi_bp, url_prefix='/fi')


@app.route("/")
def index():
    return render_template('PanelUpload.html')


@app.route("/uploadImg", methods=['POST'])
def upload_image():
    if 'imageFile' not in request.files:
        flash('No file part', 'error')

    else:
        file = request.files['imageFile']
        print(file.filename)
        
        if file.filename == '':
            flash('No selected file', 'error')

        # Here you would typically save the uploaded image to your server or process it in some way
        # For simplicity, let's just return a success message
        else:
            flash('Image uploaded successfully!', 'success')
    
    return redirect(url_for('index'))


@app.route("/uploadPdf", methods=['POST'])
def upload_pdf():
    if 'pdfFile' not in request.files:
        flash('No file part', 'error')
    
    else:
        file = request.files['pdfFile']
        print(file.filename)
        
        if file.filename == '':
            flash('No selected file', 'error')
        else:
            flash('Pdf uploaded successfully!', 'success')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8964)
    #app.run(debug=True)


'''
# python upload image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    parent=root,
    # choose type manually on lower right corner
    filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*"))
)
print(file_path)
'''