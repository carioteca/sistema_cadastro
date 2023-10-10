# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listagem.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView,QVBoxLayout, QWidget,QHeaderView,QTableWidgetItem
from PyQt5.QtCore import Qt
from bd import conection_bd, show_list_product

class Listagem(object):
    def show_cad(self):
        from cad import Cadastrar
        self.cadform = QtWidgets.QMainWindow() 
        self.ui = Cadastrar()
        self.ui.setupUi(self.cadform)
        self.cadform.show()
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(955, 532)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("background-color:#101010;")
        Form.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 460, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:\"white\";\n"
"background-color:#242121;")
        self.pushButton.clicked.connect(self.show_cad)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 911, 411))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color:#101010;font-size:20px;color:white;")
        self.tableWidget.setLineWidth(10)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.table_list_product()
        # self.tableWidget.horizontalHeader.resizeSection(0, 100)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Listagem"))
        self.pushButton.setText(_translate("Form", "CADASTRAR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Valor"))
     
        
    def input_symbol_number(self, numero):
        valor_formatado = "R$ "+ str(numero)
        return valor_formatado
        
    def table_list_product(self):
        row_pos=0
        resultado = show_list_product()
        for linha in resultado:
            numero = linha[1]
            valor_formatado = self.input_symbol_number(numero)
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)  
            self.tableWidget.setItem(row_pos,0,QTableWidgetItem(str(linha[0])))
            self.tableWidget.setItem(row_pos,1,QTableWidgetItem(valor_formatado))
            row_pos+=1
            
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("img/logo.png"))
    app.setStyleSheet("QHeaderView::section{background-color: #2a2a2a; border:1px solid #2a2a2a;}")
    
if __name__ == "__main__":
    Form = QtWidgets.QWidget()
    ui = Listagem()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


