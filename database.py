import sqlite3


class DataBase:
    def __init__(self, name='system.db'):
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def closeConnection(self):
        try:
            self.connection.close()
        except ConnectionError:
            pass

    def createTableCompany(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Empresas(
            
            CNPJ TEXT,
            NOME TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            UF TEXT,
            CEP TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,

            PRIMARY KEY(CNPJ)
            )       
        """)
    # REGISTRA TODAS AS COMPANHIAS

    def registerCompany(self, fullDataSet):
        cnpj = fullDataSet[0]

        # VERIFICA SE O CNPJ JÁ Existe no banco de dados
        cursor = self.connection.cursor()
        sql = "SELECT * FROM empresas WHERE cnpj = ?"
        result = cursor.execute(sql, (cnpj,))
        if result.fetchone() is not None:
            return

        camposTabela = ('CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO',
                        'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE',
                        'EMAIL')
        qntd = ('?,?,?,?,?,?,?,?,?,?,?')
        cursor = self.connection.cursor()

        try:
            campos = ','.join(camposTabela)
            cursor.execute(f'''INSERT INTO Empresas ({campos}) \
                                VALUES({qntd}) ''', fullDataSet)

            self.connection.commit()
            return ('OK')
        except Exception:
            return 'Erro'

    # SELECIONA TODAS AS COMPANHIAS
    def selectAllCompanies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('SELECT * FROM Empresas ORDER BY NOME')
            empresas = cursor.fetchall()
            return empresas
        except Exception:
            print('tem um erro aqui no banco de dados')
            return
    # DELETA AS INFORMAÇÕES NO BANCO DE DADOS

    def deletCompany(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresas WHERE CNPJ = '{id}'")

            self.connection.commit()

            return 'Cadastro de empresa excluido com sucesso!'

        except Exception:
            return 'Erro ao Excluir registro!'

    # ATUALIZA AS INFORMAÇÕES NO BANCO DE DADOS
    def updateCompany(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Empresas set

        CNPJ = '{fullDataSet[0]}',
        NOME = '{fullDataSet[1]}',
        LOGRADOURO = '{fullDataSet[2]}',
        NUMERO = '{fullDataSet[3]}',
        COMPLEMENTO = '{fullDataSet[4]}',
        BAIRRO = '{fullDataSet[5]}',
        MUNICIPIO = '{fullDataSet[6]}',
        UF = '{fullDataSet[7]}',
        CEP = '{fullDataSet[8]}',
        TELEFONE = '{fullDataSet[9]}',
        EMAIL = '{fullDataSet[10]}'

        WHERE CNPJ = '{fullDataSet[0]}'
    
        """)
        self.connection.commit()
        return
