import sqlite3
import sys
from builtins import str

import pandas as pd
from database import DataBase
from PySide6.QtCore import QCoreApplication, QEasingCurve, QPropertyAnimation
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                               QTableWidget, QTableWidgetItem)
from ui_functions import consultaCnpj, tirarPontos
from ui_main import Ui_MainWindow
from variables import WINDOW_ICON_PATH


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Fallz - Sistema de cadastro de empresas')
        self.buscar_empresas()
        self.contador = 0

        #########################################
        # TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.leftMenu)
        #########################################
#


#       #########################################
        # Páginas do Sistema
        self.btn_home.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.pg_ahome))

        self.btn_cadastrar.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.pg_cadastrar))

        self.btn_contatos.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.pg_contatos))

        self.btn_sobre.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.pg_sobre))
        #########################################
#

        #########################################
        # Preencher automaticamente os dados do cnpj
        self.txt_cpnj.editingFinished.connect(self.consultApi)

        #########################################
        # Botão de cadastrar empresas
        self.botao_cadastro.clicked.connect(self.cadastrar_empresas)

        #########################################
        # Botão de atualizar cadastro
        self.btn_alterar.clicked.connect(self.update_company)
#        #########################################

        #########################################
        # Botão de gerar tabela em excel
        self.btn_excel.clicked.connect(self.gerar_excel_2)
#        #########################################

        #########################################
        # Botão de Deletar empresas
        self.btn_excluir.clicked.connect(self.deletar_empresa)
#        #########################################

    # Função que desliza o menu ao clicar no botão

    def leftMenu(self):

        width = self.left_menu.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QPropertyAnimation(self.left_menu, b'maximumWidth')
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        self.animation.start()  # Inicia a animação
    #################################################################

#

    #################################################################
    # Chama a API e seta o retorno da função nas line text da interface

    def consultApi(self):
        try:
            # VERIFICA SE O CNPJ É DÍGITO ANTES DE SETAR O RETORNO DA API
            # NOS CAMPOS DO FORMULÁRIO

            cnpj = self.txt_cpnj.text().replace('.', '').replace(
                '/', '').replace('-', '').strip()

            # VERIFICA SE O CAMPO ESTÁ VAZIO E NÃO RETORNA NADA
            if cnpj == '':
                return

            if not cnpj.isdigit():
                msgBox = "Impossível cadastrar (CNPJ INVÁLIDO)'"
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setWindowTitle("Atenção")
                msg.setText(msgBox)
                msg.exec()
                self.limpar_formulario()
                return

        # VERIFICA SE O CAMPO DO CNPJ TEM 14

            if len(cnpj) < 14:
                msgBox = "Impossível cadastrar (CNPJ INVÁLIDO)'"
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Information)
                msg.setWindowTitle("Atenção")
                msg.setText(msgBox)
                msg.exec()
                self.limpar_formulario()
                return

            # SETA OS DADOS RETORNADOS PELA API NOS CAMPOS DO FORMULÁRIO
            campos = consultaCnpj(self.txt_cpnj.text())

            if campos is not None:
                self.txt_nome.setText(campos[0])
                self.txt_logradouro.setText(campos[1])
                self.txt_numero.setText(campos[2])
                self.txt_complemento.setText(campos[3])
                self.txt_bairro.setText(campos[4])
                self.txt_municipio.setText(campos[5])
                self.txt_uf.setText(campos[6])
                if campos[7] is not None:
                    self.txt_cep.setText(campos[7])
                if campos[8] is not None:
                    self.txt_telefone.setText(campos[8])
                self.txt_email.setText(campos[9])
        except Exception as e:
            error_message = "Erro inesperado: " + str(e)
            QMessageBox.warning(self, "Erro", error_message)

    ##################################################################

    #################################################################
    # Para cadastrar empresas

    def cadastrar_empresas(self):

        # VERIFICA SE TEM ALGO NOS CAMPOS ANTES DE FAZER O REGISTRO NO BD
        if not self.txt_cpnj.text() or not self.txt_nome.text():
            msgBox = "Impossível cadastrar (CNPJ INVÁLIDO)'"
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Atenção")
            msg.setText(msgBox)
            msg.exec()
            self.limpar_formulario()
            return

        db = DataBase()
        db.connect()
        fullDataSet = (
            self.txt_cpnj.text(),
            self.txt_nome.text(),
            self.txt_logradouro.text(),
            self.txt_numero.text(),
            self.txt_complemento.text(),
            self.txt_bairro.text(),
            self.txt_municipio.text(),
            self.txt_uf.text(),
            self.txt_cep.text(),
            self.txt_telefone.text().strip(),
            self.txt_email.text(),
        )

        # CADASTRAR NO BANCO DE DADOS
        resp = db.registerCompany(fullDataSet)

        if resp == "OK":
            msgBox = "Cadastro Realizado"
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("Sucesso")
            msg.setText(msgBox)
            msg.exec()
            db.closeConnection()
            self.limpar_formulario()
            self.buscar_empresas()
            return
        else:
            msg_error = "CNPJ já existe no banco de dados"
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(msg_error)
            msg.exec()
            db.closeConnection()
            self.buscar_empresas()
            return

    #################################################################
    # Para limpar os campos do formulário

    def limpar_formulario(self):
        campos = (
            self.txt_cpnj.clear(),
            self.txt_nome.clear(),
            self.txt_logradouro.clear(),
            self.txt_numero.clear(),
            self.txt_complemento.clear(),
            self.txt_bairro.clear(),
            self.txt_municipio.clear(),
            self.txt_uf.clear(),
            self.txt_cep.clear(),
            self.txt_telefone.clear(),
            self.txt_email.clear(),
        )
        return campos

    #################################################################
    # Buscar Empresas

    def buscar_empresas(self):
        db = DataBase()
        db.connect()
        result = db.selectAllCompanies()

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(result))

        for row, text in enumerate(result):
            for colum, data in enumerate(text):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row, colum, item)
        db.closeConnection()
    #################################################################
    # update Empresas

    def update_company(self):
        dados = []
        update_dados = []

        for row in range(self.tableWidget.rowCount()):
            for colum in range(self.tableWidget.columnCount()):
                dados.append(self.tableWidget.item(row, colum).text())

            update_dados.append(dados)
            dados = []

        # ATUALIZAR DADOS NO BANCO
        db = DataBase()
        db.connect()

        for emp in update_dados:
            db.updateCompany(tuple(emp))

        db.closeConnection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Erro")
        msg.setText('Dados atualizados com sucesso!')
        msg.exec()
        db.closeConnection()

        self.tableWidget.reset()

    def deletar_empresa(self):

        db = DataBase()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registor será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        resp = msg.exec()

        if resp == QMessageBox.StandardButton.Yes:
            cnpj = self.tableWidget.selectionModel().currentIndex().\
                siblingAtColumn(0).data()
            result = db.deletCompany(cnpj)
            self.buscar_empresas()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle("EMPRESAS")
            msg.setText(result)
            msg.exec()

        db.closeConnection()

    def gerar_excel(self):

        dados = []
        all_dados = []

        for row in range(self.tableWidget.rowCount()):
            for colun in range(self.tableWidget.columnCount()):
                dados.append(self.tableWidget.item(row, colun).text())

        all_dados.append(dados)
        dados = []

        columns = ['CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO',
                   'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE',
                   'EMAIL']

        empresas = pd.DataFrame(all_dados, columns)
        empresas.to_excel("Empresas.xlsx", sheet_name='empresas', index=False)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle('Excel')
        msg.setText('Relatório Excel gerado com sucesso!')
        msg.exec()

    def gerar_excel_2(self):

        cnx = sqlite3.connect("system.db")

        empresas = pd.read_sql_query("""SELECT * FROM Empresas """, cnx)

        empresas.to_excel("Empresas.xlsx", sheet_name='empresas', index=False)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle('Excel')
        msg.setText('Relatório Excel gerado com sucesso!')
        msg.exec()

        # VERIFICAÇÃO NO TEMPO DE RESPOSTA DA API


if __name__ == '__main__':
    db = DataBase()
    db.connect()
    db.createTableCompany()
    db.closeConnection()

    app = QApplication(sys.argv)
    window = MainWindow()

    #########################################
    # DEFINE ÍCONE
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    #########################################

    window.show()
    # app.exec()
    sys.exit(app.exec())
