from datetime import datetime, timedelta
from flask import Blueprint, jsonify, url_for, render_template
from cli import db
from cli.models import User


home = Blueprint('home', __name__)


@home.before_app_first_request
def init_db():
    db.create_all()


@home.route('/', methods=['GET'])
def index():
    task = 5
    return render_template(
        'index.html',
        task=task
    )


@home.route('/users')
def users():
    users = db.session.query(User).all()
    return jsonify([user.username for user in users])
