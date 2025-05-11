from flask import Blueprint, render_template, request, redirect, url_for
from app.models.user import User
from flask_login import login_required, current_user
from app import db

bp = Blueprint('user', __name__)

@bp.route('/listar')
@login_required
def listar_usuarios():
    usuarios = User.query.all()
    return render_template('listar.html', usuarios=usuarios)

@bp.route('/user/novo')
@login_required
def novo_usuario():
    return render_template('user/novo.html')

@bp.route('/user/criar', methods=['POST'])
@login_required
def criar_usuario():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    novo = User(username=username, password=password, role=role)
    db.session.add(novo)
    db.session.commit()
    return redirect(url_for('user.listar_usuarios'))

@bp.route('/user/deletar/<int:id>', methods=['POST'])
@login_required
def deletar_usuario(id):
    usuario = User.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('user.listar_usuarios'))
