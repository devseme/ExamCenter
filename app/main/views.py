from flask import Flask,render_template,request,redirect,url_for
from . import main 
from .. import db
from .forms import UploadForm
import os 


# Views
@main.route('/')
def index():


    return render_template('index.html') 

@main.route('/exams')
def exams():
    
    
    return render_template('exams.html')
@main.route('/moi')
def moi():
    
    
    return render_template('moi.html')
@main.route('/karatina')
def karatina():
    
    return render_template('karatina.html')
    
@main.route('/kpke')
def kpke():
    
    return render_template('kpke.html')

@main.route('/Tuk')
def Tuk():
    
    return render_template('Tuk.html')
@main.route('/uoe')
def uoe():
    
    return render_template('uoe.html')

@main.route('/maseno')
def maseno():
    
    return render_template('maseno.html')

@main.route('/new_upload', methods = ['POST','GET'])
# @login_required 
def new_upload():

    # import pdb; pdb.set_trace();

    form = UploadForm()
    if form.validate_on_submit():

        # image_path = secure_filename(form.image_path.data.filename)
        # image_path = form.image_path.data 

        # import pdb; pdb.set_trace()
        return redirect(url_for('main.index')) 

    # else:
    #     file_url = None
    return render_template('upload.html') 