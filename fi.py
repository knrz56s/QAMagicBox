from flask import Flask, Blueprint, render_template, redirect, url_for, request, session
import requests

fi_bp = Blueprint('fi', __name__)

@fi_bp.route('/')
def index():
    return render_template('GPTUpload.html')

@fi_bp.route('/sayHi')
def say():
    print('Here is f.')