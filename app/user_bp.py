from flask import Blueprint, render_template, request, redirect, url_for, flash
# from ..inserir import cad_veiculo 

user_bp = Blueprint('user', __name__, template_folder='templates/user')

@user_bp.route('/user', methods=['POST', 'GET'])
def user():
    return render_template('user.html')

# @user_bp.route('/admin', methods=['POST', 'GET'])
# def admin():
#     if request.method == 'POST':
#         veiculo = cad_veiculo(
#             nome=request.form.get('nome_veiculo'),
#             marca=request.form.get('marca_veiculo'),
#             modelo=request.form.get('modelo_veiculo'),
#             categoria=request.form.get('categoria_veiculo'),
#             cor=request.form.get('cor_veiculo'),
#             ano=request.form.get('ano_veiculo'),
#             preco_dia=request.form.get('preco_veiculo'),
#             disponibilidade=request.form.get('disponibilidade_veiculo'),
#             placa=request.form.get('placa_veiculo')
#         )
#         return 'Veículo criado com sucesso!'
#     return render_template('admin.html')
