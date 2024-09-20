from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from app.models import dados_pessoais

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == 'user@example.com' and password == 'senha123':
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais inválidas, tente novamente.', 'danger')
    
    return render_template('login.html')

@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        email = request.form.get('email') 
        endereco = request.form.get('endereco')
        data_nascimento = request.form.get('data_nascimento')
        rg = request.form.get('rg')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')

        # Validações e processamento dos dados
        if len(nome) < 3:
            flash('O nome de usuário deve ter pelo menos 3 caracteres.', 'danger')
        elif len(senha) < 6:
            flash('A senha deve ter pelo menos 6 caracteres.', 'danger')
        else:
            dados_pessoais = dados_pessoais(nome=nome, senha=senha, cpf=cpf, rg=rg, data_nascimento=data_nascimento, email=email, endereco=endereco, telefone=telefone)
            db.session.add(dados_pessoais)
            db.session.commit()
            flash('Usuário registrado com sucesso!', 'success')
            return redirect(url_for('login'))

    return render_template('registro.html')