from flask import Blueprint, render_template, redirect, request, flash, url_for
from app.models.user import User
from app import db, login_manager
from flask_login import login_user, logout_user

bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/')
def root():

    # Redireciona automaticamente para a rota /login

    return redirect(url_for('auth.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # Verifica se a tabela de usuários está vazia

    if User.query.count() == 0:
        
        # Se estiver vazia, cria o usuário admin
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            new_admin = User(username='admin', password='admin123', role='admin')
            db.session.add(new_admin)
            db.session.commit()
            flash('Usuário admin criado automaticamente')

    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect('/dashboard')
        flash('Usuário ou senha inválidos')

    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect('/login')
