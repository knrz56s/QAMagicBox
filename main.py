from flask import Flask, Blueprint, render_template, redirect, url_for, request, session, flash
import requests, os
from werkzeug.utils import secure_filename

from PDF import PDF
from Secrets import UPLOAD_FOLDER

app = Flask(
    __name__,
    #template_folder='templates',
    static_folder='static',
    static_url_path='/'
)
app.secret_key='any'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template('PanelUpload.html')


from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/uploadImg", methods=['POST'])
def upload_image():
    try:
        if 'imageFile' not in request.files:
            flash('No file part', 'error')
        
        file = request.files['imageFile']
        print("File name is : ", file.filename)
        
        if file.filename == '':
            flash('No selected file', 'error')
        
        # Here you would typically save the uploaded image to your server or process it in some way
        # For simplicity, let's just return a success message
        else:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # zh-TW not allowed
                flash('Image uploaded successfully!', 'success')
                return redirect(url_for('uploaded_file', filename=filename))
    except Exception as e:
        # Log the exception or handle it in a way that's appropriate for your application
        flash('An error occurred: {}'.format(str(e)), 'error')
    
    return redirect(url_for('index'))


@app.route("/uploadPdf", methods=['POST'])
def upload_pdf():
    
    try:
        if 'pdfFile' not in request.files:
            flash('No file part', 'error')
        
        else:
            file = request.files['pdfFile']
            print("File name is : ", file.filename)
            
            if file.filename == '':
                flash('No selected file', 'error')
            else:
                flash('Pdf uploaded successfully!', 'success')
        
        uploadPdf = PDF(pdf=file)
        response = uploadPdf.run() # HOW TO DO IT ASYNCHRONOUSLY D:

    except Exception as e:
        # Log the exception or handle it in a way that's appropriate for your application
        flash('An error occurred: {}'.format(str(e)), 'error')

    return redirect(url_for('index'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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