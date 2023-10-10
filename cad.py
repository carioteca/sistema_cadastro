# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cad.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import locale
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QVBoxLayout,QApplication
from PyQt5.QtGui import QDoubleValidator
from bd import conection_bd,register_table
from lista import Listagem 

class Cadastrar(object):
    def show_list(self):
        import sys
        self.cadlist = QtWidgets.QMainWindow() 
        self.ui = Listagem()
        self.ui.setupUi(self.cadlist)
        self.cadlist.show()
        
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.setFixedSize(929, 520)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("background-color:#101010;")
        self.QLineNome = QtWidgets.QLineEdit(Form)
        self.QLineNome.setGeometry(QtCore.QRect(60, 110, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QLineNome.setFont(font)
        self.QLineNome.setStyleSheet("background-color:white;")
        self.QLineNome.setObjectName("QLineNome")
        self.QLineNome.setMaxLength(255)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 50, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setText("Nome")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setText("Descrição ")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.plainDescricao = QtWidgets.QPlainTextEdit(Form)
        self.plainDescricao.setGeometry(QtCore.QRect(60, 260, 461, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.plainDescricao.setFont(font)
        self.plainDescricao.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainDescricao.setStyleSheet("background-color:\"white\";")
        self.plainDescricao.setObjectName("plainDescricao")
        self.plainDescricao.textChanged.connect(self.verify_carac_desc)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(610, 50, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setText("Valor")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(610, 210, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setText("Disponível")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.radioSim = QtWidgets.QRadioButton(Form)
        self.radioSim.setGeometry(QtCore.QRect(610, 280, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        self.radioSim.setFont(font)
        self.radioSim.setStyleSheet("color:\"white\";")
        self.radioSim.setObjectName("radioButton")
        self.radioNao = QtWidgets.QRadioButton(Form)
        self.radioNao.setGeometry(QtCore.QRect(690, 280, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        self.radioNao.setFont(font)
        self.radioNao.setStyleSheet("color:\"white\";")
        self.radioNao.setObjectName("radioNao")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 440, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color:#242121;\n"
"color:\"white\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.verify_field_condition)
        self.QLineValor = QtWidgets.QLineEdit(Form)
        self.QLineValor.setGeometry(QtCore.QRect(610, 110, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.QLineValor.setFont(font)
        self.QLineValor.setStyleSheet("background-color:white;")
        self.QLineValor.setObjectName("QLineValor")
        self.QLineValor.editingFinished.connect(self.verify_type)
        self.double_validator = QDoubleValidator()
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 380, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;\n"
"font-size:18;")
        self.label_5.setObjectName("label_5")        
        self.QLineValor.setValidator(self.double_validator)    
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
     
                     
              

    def input_mask(self, numero):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor_formatado = locale.currency(numero, grouping=True, symbol="R$")
        self.QLineValor.setText(str(valor_formatado))
        
    def show_alert_empty(self):
        alert = QMessageBox()
        alert.setWindowTitle('Aviso')
        alert.setText('Campo vázio, por favor, verifique!')
        alert.setIcon(QMessageBox.Warning)  # Você pode alterar o ícone (Information, Warning, Critical)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()
        
    def show_alert_limity(self):
        alert = QMessageBox()
        alert.setWindowTitle('Aviso')
        alert.setText('Você atingiu o limite de caracteres no campo de descrição.\n Por favor, reduza o tamanho do texto!')
        alert.setIcon(QMessageBox.Warning)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()
        
    def show_alert_success(self):
        alert = QMessageBox()
        alert.setWindowTitle('Aviso')
        alert.setText('Dados Inseridos com Sucesso!')
        alert.setIcon(QMessageBox.Information)  # Você pode alterar o ícone (Information, Warning, Critical)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()
        
    
    def obtain_radio_option(self):
        if self.radioSim.isChecked() == True:
            option=1
        else:
            option=0
        return option
        
    def clean_value(self):
        valor = self.QLineValor.text()
        valor = valor.replace('R$', '')
        valor = valor.replace(',00', '')
        return valor
        
    def insert_data(self):
        disponivel = self.obtain_radio_option()
        valor = self.clean_value()
        register_table(self.QLineNome.text(),self.plainDescricao.toPlainText(),valor,disponivel)
        self.show_alert_success() 
        
    def verify_carac_desc(self):
        descricao = self.plainDescricao.toPlainText()
        tam = int(len(descricao)) - 1
        self.label_5.setText("Caracteres: "+str(tam))
        
        
    def verify_limit_desc(self):
        descricao = self.plainDescricao.toPlainText()
        tam = int(len(descricao)) - 1
        cond = True
        if tam > 255:
            cond = False
        return cond
        
    def verify_type(self):
        numero = self.QLineValor.text()
        try:
            numero_float = float(numero.replace(",", "."))
            self.input_mask(numero_float)
        except ValueError:
            pass
            
    def verify_field_condition(self):
       cond = self.verify_limit_desc()
       if self.QLineNome.text() == "":
            self.show_alert_empty()
            
       elif self.plainDescricao.toPlainText() == "":
            self.show_alert_empty() 
            
       elif self.QLineValor.text() == "":
            self.show_alert_empty()
            
       elif self.radioSim.isChecked() == False and self.radioNao.isChecked() == False:
            self.show_alert_empty()
       elif cond == False:
            self.show_alert_limity()
       else:
        self.insert_data()
        self.show_list()
        self.Form.close()
        
    
 
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cadastrar"))
        self.radioSim.setText(_translate("Form", "Sim"))
        self.radioNao.setText(_translate("Form", "Não"))
        self.label_5.setText(_translate("Form", "Caracteres:"))
        self.pushButton.setText(_translate("Form", "CADASTRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    app.setWindowIcon(QtGui.QIcon("img/logo.png"))
    ui = Cadastrar()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
