# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(0, 0))
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, 0, -1)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, 0, 9)
        self.fallz_icone = QLabel(self.frame)
        self.fallz_icone.setObjectName(u"fallz_icone")
        self.fallz_icone.setMaximumSize(QSize(16728, 16777))

        self.horizontalLayout_3.addWidget(self.fallz_icone)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(65, 65, 65)\n"
"}\n"
"\n"
"\n"
"QToolBox{\n"
"text-align: left;\n"
"	background-color: rgb(70,70,70)\n"
"\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(192,192,192);\n"
"	text-align: left;\n"
"\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(169,169,169);\n"
"	border-top-left-radius: 15px\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(220,220,220)\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 67, 398))
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setFont(font1)
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 106, 398))
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 0, 0)
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.toolBox.addItem(self.page_2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 9, 9)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle.setFocusPolicy(Qt.StrongFocus)
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setStyleSheet(u"background-color: rgba(128,128,128, 128);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.pg_ahome = QWidget()
        self.pg_ahome.setObjectName(u"pg_ahome")
        self.verticalLayout_13 = QVBoxLayout(self.pg_ahome)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.sistema_cadastro = QLabel(self.pg_ahome)
        self.sistema_cadastro.setObjectName(u"sistema_cadastro")

        self.verticalLayout_13.addWidget(self.sistema_cadastro)

        self.Logo = QLabel(self.pg_ahome)
        self.Logo.setObjectName(u"Logo")

        self.verticalLayout_13.addWidget(self.Logo)

        self.criado_por = QLabel(self.pg_ahome)
        self.criado_por.setObjectName(u"criado_por")

        self.verticalLayout_13.addWidget(self.criado_por)

        self.pages.addWidget(self.pg_ahome)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color: rgb(220,220,220);\n"
"	font: 10pt \"MS Shell Dlg 2\";	\n"
"}\n"
"\n"
"QFrame{\n"
"		\n"
"	background-color: rgb(192,192,192)	\n"
"	\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_logradouro = QLineEdit(self.frame_6)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setMinimumSize(QSize(0, 30))
        self.txt_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 2, 0, 1, 4)

        self.txt_complemento = QLineEdit(self.frame_6)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setMinimumSize(QSize(0, 30))
        self.txt_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 3, 1, 1, 2)

        self.txt_bairro = QLineEdit(self.frame_6)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setMinimumSize(QSize(0, 30))
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 3, 3, 1, 1)

        self.txt_nome = QLineEdit(self.frame_6)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(30, 30))
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 1, 1, 3)

        self.txt_cep = QLineEdit(self.frame_6)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setMinimumSize(QSize(0, 30))
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 4, 2, 1, 2)

        self.txt_email = QLineEdit(self.frame_6)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setMinimumSize(QSize(0, 30))
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 5, 1, 1, 3)

        self.lbs_empresas = QLabel(self.frame_6)
        self.lbs_empresas.setObjectName(u"lbs_empresas")
        self.lbs_empresas.setMaximumSize(QSize(16777215, 100))
        self.lbs_empresas.setStyleSheet(u"color: rgb(105,105,105);\n"
"background-color: rgb(249, 249, 249);")

        self.gridLayout.addWidget(self.lbs_empresas, 0, 0, 1, 4)

        self.txt_uf = QLineEdit(self.frame_6)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setMinimumSize(QSize(0, 30))
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 4, 1, 1, 1)

        self.txt_municipio = QLineEdit(self.frame_6)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setMinimumSize(QSize(0, 30))
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 4, 0, 1, 1)

        self.txt_cpnj = QLineEdit(self.frame_6)
        self.txt_cpnj.setObjectName(u"txt_cpnj")
        self.txt_cpnj.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.txt_cpnj.setFont(font2)
        self.txt_cpnj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cpnj, 1, 0, 1, 1)

        self.txt_numero = QLineEdit(self.frame_6)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setMinimumSize(QSize(0, 30))
        self.txt_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_numero, 3, 0, 1, 1)

        self.txt_telefone = QLineEdit(self.frame_6)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setMinimumSize(QSize(0, 30))
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 5, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.botao_cadastro = QPushButton(self.tab)
        self.botao_cadastro.setObjectName(u"botao_cadastro")
        self.botao_cadastro.setMinimumSize(QSize(160, 30))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.botao_cadastro.setFont(font3)
        self.botao_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_cadastro.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(30,144,255);\n"
"	border-radius:15px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius:15px;\n"
"	background-color: rgb(105,105,105);\n"
"}")

        self.verticalLayout_11.addWidget(self.botao_cadastro, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget {\n"
"	background-color: rgb(249, 249, 249);\n"
"\n"
"}")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setRowCount(0)

        self.horizontalLayout_6.addWidget(self.tableWidget)

        self.frame_5 = QFrame(self.tab_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton {\n"
"	border-radius: 15px;\n"
"	background-color: rgb(192,192,192);\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"	color: rgb(0, 24, 48);\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: rgb(249, 249, 249)\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_excel = QPushButton(self.frame_5)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0,100,0);\n"
"	border-radius:15px;\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_5)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255, 215, 0);\n"
"	border-radius:15px;\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_5)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(255,99,71);\n"
"	border-radius:15px;\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.gridLayout_2 = QGridLayout(self.pg_contatos)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.pg_contatos)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.whatsapp = QLabel(self.pg_contatos)
        self.whatsapp.setObjectName(u"whatsapp")

        self.gridLayout_2.addWidget(self.whatsapp, 1, 0, 1, 1)

        self.label_6 = QLabel(self.pg_contatos)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_9 = QLabel(self.pg_contatos)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        self.pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.pg_sobre)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_8)

        self.pages.addWidget(self.pg_sobre)

        self.verticalLayout_6.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer = QFrame(self.main_container)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 3, 0, 0)
        self.footer_frame = QLabel(self.footer)
        self.footer_frame.setObjectName(u"footer_frame")

        self.verticalLayout_2.addWidget(self.footer_frame)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fallz_icone.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/fav.png\"/><span style=\" font-size:22pt; font-weight:700; vertical-align:super;\">FALLZ</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Usu\u00e1rio</span>: Pedro</p><p align=\"center\"><span style=\" font-weight:700;\">Sistema</span>: Cadastro</p><p align=\"center\"><span style=\" font-weight:700;\">Status</span>: Ativo</p><p align=\"center\"><span style=\" font-weight:700;\">Venc</span>: 12/12/2023</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">JO\u00c3O PEDRO DEV</span></p></body></html>", None))
        self.sistema_cadastro.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">SISTEMA DE CADASTRO</span></p></body></html>", None))
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/logo4.png\"/></p></body></html>", None))
        self.criado_por.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; font-style:italic;\">Desenvolvido por Jo\u00e3o Pedro Gon\u00e7alves</span></p></body></html>", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome empresarial", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lbs_empresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">EMPRESAS</span></p></body></html>", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.txt_cpnj.setText("")
        self.txt_cpnj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_numero.setText("")
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.botao_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">Empresas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGADOURO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">Empresas</span></p></body></html>", None))
        self.whatsapp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/whatsApp.png\"/><span style=\" font-size:18pt; vertical-align:super;\">(62) 9 8527-7528</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/email.png\"/><span style=\" font-size:16pt; vertical-align:super;\">www.pedrobitencourtdev@hotmail.com</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/instagram.png\"/><span style=\" font-size:16pt; vertical-align:super;\">Fallzoficial</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Sobre</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">Este sistema faz consulta do CNPJ ultilizando API da receita federal e faz o cadastro em um banco de dados SQLITE3.</span></p><p><span style=\" font-size:14pt; font-style:italic;\">Objetivo do sistema \u00e9 praticar Python para desenvolver aplica\u00e7oes mais modernas e funcionais.</span></p></body></html>", None))
        self.footer_frame.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Nunito Sans','sans-serif'; font-size:10pt; color:#ffffff;\">\u00a9 Jo\u00e3o Pedro Gon\u00e7alves 2023</span></p></body></html>", None))
    # retranslateUi

