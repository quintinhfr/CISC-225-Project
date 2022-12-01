from crypt import methods
from http.client import REQUEST_ENTITY_TOO_LARGE
from flask import Flask, url_for, redirect, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import login_manager
from pip import main
from werkzeug.utils import secure_filename
import os
from werkzeug.exceptions import RequestEntityTooLarge
from PIL import Image
from pydub import AudioSegment
from moviepy.editor import *
from PIL import Image
import stdio
import img2pdf
import shutil
import mysql.connector








# ONLINE TEAM PROJECT

#Database Creation - 


#App Creation -

app = Flask(__name__)
app.config['SECRET_KEY'] = "HUGRADPROJECT"
app.config['MAX_CONTENT_LENGTH'] = 30 * 5000 * 5000 # File Size Limit

AllowedAudioTypes = ['.wav', '.flac', '.alac', '.mp3']

AllowedAtVTypes = ['.mp4', '.MP4']

AllowedPictureTypes = ['.jpg', '.jpeg', '.JPG', '.JPEG']





#--------------------------------------------------------------------
# HOME PAGE
#--------------------------------------------------------------------

@app.route("/")
def Home():
    return render_template("index.html")

#--------------------------------------------------------------------
# Audio Conversion Page
#--------------------------------------------------------------------

@app.route("/audio", methods=['GET', 'POST'])
def audio():
    return render_template("audio.html")

#--------------------------------------------------------------------
# Compression Page
#--------------------------------------------------------------------

@app.route("/compression")
def About():
    return render_template("compression.html")

#--------------------------------------------------------------------
# Extra Page
#--------------------------------------------------------------------

@app.route("/vta")
def Post():
    return render_template("vta.html")

#--------------------------------------------------------------------
# Picture Conversion Page
#--------------------------------------------------------------------

@app.route("/picture")
def picture():
    return render_template("picture.html")

#--------------------------------------------------------------------
# UPLOAD Audio
#--------------------------------------------------------------------

@app.route("/upload_audio", methods=['POST'])
def upload():
    try:
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]

        if file:
            print(extension)
            print(AllowedAudioTypes)

            if extension not in AllowedAudioTypes:
                return 'File is not an accepted audio format'

            file.save(os.path.join(
            'upload_audio/',
            secure_filename(file.filename)
            ))

    except RequestEntityTooLarge:
        return 'File is too large'


    return redirect('/')

#------------------------------------------------------------------------
# MP4 to MP3 Upload
#------------------------------------------------------------------------

@app.route("/upload_video_audio_conversion", methods=['POST'])
def mp4_mp3():
    try:
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]

        if file:
            print(extension)
            print(AllowedAtVTypes)

            if extension not in AllowedAtVTypes:
                return 'File is not an accepted video format'

            file.save(os.path.join(
            'ATVUpload/',
            secure_filename(file.filename)
            ))

   
    except RequestEntityTooLarge:
        return 'File is too large'

    return redirect('/')

#------------------------------------------------------------------------
# Picture Upload
#------------------------------------------------------------------------

@app.route("/upload_picture", methods=['POST'])
def JPG_PDF():
    try:
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]

        if file:

            if extension not in AllowedPictureTypes:
                return 'File is not an accepted video format'

            file.save(os.path.join(
            'upload_picture/',
            secure_filename(file.filename)
            ))

            # Image Storing 
            img_path = (secure_filename(file.filename))

            #PDF Path
            pdf_path = ("New.pdf")

            #open Image
            image= Image.open(img_path)

            #Chunk Conversion
            pdf_bytes = img2pdf.convert(image.filename)

            #open/Creating Pdf
            file = open(pdf_path, "wb")

            #Write PDF with chunks
            file.write(pdf_bytes)

            #Close image file
            image.close()

            #Close PDF File
            file.close()

            shutil.move("/Users/quintinhurrell/Desktop/EZToolz_Project/New.pdf", "/Users/quintinhurrell/Desktop/EZToolz_Project/templates/New.pdf")


   
    except RequestEntityTooLarge:
        return 'File is too large'

    return redirect('/')






#----------------------
# Program Run Operation
#----------------------
if __name__ == "__main__":
    app.run()