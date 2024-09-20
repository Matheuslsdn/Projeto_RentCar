from app import db 

class veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    marca = db.Column(db.String(20), nullable=False)
    modelo =db.Column(db.String(20), nullable=False)
    categoria = db.Column(db.String(20), nullable=False)
    cor = db.Column(db.String(20), nullable=False)
    ano = db.Column(db.Date, nullable=False)
    preco_dia = db.Column(db.Float, nullable=False)
    disponibilidade = db.Column(db.String(20), nullable=False)
    placa = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<veiculos> {self.nome}'
    
class usuario(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('dados_pessoais.id'))
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(20), unique=True, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f'<usuario> {self.nome}'
    
class manutencao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veiculo =  db.Column(db.String(20), db.ForeignKey('veiculo.id'))
    descricao = db.Column(db.Text, nullable=False)
    dataEntrada = db.Column(db.Date, nullable=False)
    dataSaida = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return f'<manutencao> {self.veiculo}'
    
class reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(50), db.ForeignKey('usuario.id'))
    veiculo = db.Column(db.String(20), db.ForeignKey('veiculo.id'))
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f'<reserva> {self.cliente}'
    
class dados_pessoais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    rg = db.Column(db.String(12), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    telefone = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<dados_pessoais> {self.id_usuario}'
    

    
    
    