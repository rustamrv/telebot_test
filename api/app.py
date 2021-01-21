from flask import Blueprint, render_template, redirect, url_for, request
from flask_restful import Api

admin = Blueprint('admin', __name__)


@admin.route('/')
@admin.route('/index')
def index():
    return "Hello world"
