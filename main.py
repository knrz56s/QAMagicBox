from flask import Flask, Blueprint, render_template, redirect, url_for, request, session, flash
import requests, os
from werkzeug.utils import secure_filename

from FileProcess import pdfExtract
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
        
        pdfExtract(file)
    except Exception as e:
        # Log the exception or handle it in a way that's appropriate for your application
        flash('An error occurred: {}'.format(str(e)), 'error')

    return redirect(url_for('index'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pdfextract(file):
    import fitz
    import re
    import os
    from pypdf import PdfReader
    import matplotlib.pyplot as plt
    import matplotlib.image as img

    #file_path = 'sample.pdf' # PDF 文件路径
    #dir_path = './' # 存放图片的文件夹

    reader = file
    length = len(reader.pages)
    for i in range(0,length) :
        page = reader.pages[i]
        print(page.extract_text())

    '''def pdf2image1(path, pic_path):
        checkIM = r"/Subtype(?= */Image)"
        pdf = fitz.open(path)
        lenXREF = pdf.xref_length()
        count = 1
        for i in range(1, lenXREF):
            text = pdf.xref_object(i)
            isImage = re.search(checkIM, text)
            if not isImage:
                continue
            pix = fitz.Pixmap(pdf, i)
            new_name = f"img_{count}.png"
            pix.save(os.path.join(pic_path, new_name))
            #image = img.imread(new_name)
            #plt.imshow(image)
            #plt.show()
            count += 1
            pix = None

    pdf2image1(file_path, dir_path)'''

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