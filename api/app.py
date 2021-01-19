import os

from flask import Blueprint, render_template, redirect, url_for, request

admin = Blueprint('admin', __name__)


@admin.route('/')
@admin.route('/index')
def index():
    return "Hello world"
