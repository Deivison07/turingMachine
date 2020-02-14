# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maquinaTurin.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(747, 452)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.campoFita = QtWidgets.QListWidget(Frame)
        self.campoFita.setMaximumSize(QtCore.QSize(16777215, 41))
        self.campoFita.setProperty("isWrapping", False)
        self.campoFita.setViewMode(QtWidgets.QListView.IconMode)
        self.campoFita.setObjectName("campoFita")
        self.verticalLayout_5.addWidget(self.campoFita)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.linhaComando = QtWidgets.QLineEdit(Frame)
        self.linhaComando.setObjectName("linhaComando")
        self.horizontalLayout.addWidget(self.linhaComando)
        self.addComando = QtWidgets.QPushButton(Frame)
        self.addComando.setObjectName("addComando")
        self.horizontalLayout.addWidget(self.addComando)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listaComando = QtWidgets.QListWidget(Frame)
        self.listaComando.setObjectName("listaComando")
        self.verticalLayout.addWidget(self.listaComando)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.limparLista = QtWidgets.QPushButton(Frame)
        self.limparLista.setObjectName("limparLista")
        self.horizontalLayout_2.addWidget(self.limparLista)
        self.removerComando = QtWidgets.QPushButton(Frame)
        self.removerComando.setObjectName("removerComando")
        self.horizontalLayout_2.addWidget(self.removerComando)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setMinimumSize(QtCore.QSize(91, 91))
        self.label_3.setMaximumSize(QtCore.QSize(91, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("turing_type_b-512.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setMinimumSize(QtCore.QSize(91, 61))
        self.label_2.setMaximumSize(QtCore.QSize(91, 61))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.boxPassoaPasso = QtWidgets.QGroupBox(Frame)
        self.boxPassoaPasso.setMinimumSize(QtCore.QSize(95, 56))
        self.boxPassoaPasso.setFlat(False)
        self.boxPassoaPasso.setCheckable(False)
        self.boxPassoaPasso.setObjectName("boxPassoaPasso")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.boxPassoaPasso)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.playPassoaPasso = QtWidgets.QPushButton(self.boxPassoaPasso)
        self.playPassoaPasso.setObjectName("playPassoaPasso")
        self.verticalLayout_2.addWidget(self.playPassoaPasso)
        self.verticalLayout_3.addWidget(self.boxPassoaPasso)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.campoEditarFita = QtWidgets.QPlainTextEdit(Frame)
        self.campoEditarFita.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.campoEditarFita.setPlainText("")
        self.campoEditarFita.setBackgroundVisible(False)
        self.campoEditarFita.setCenterOnScroll(False)
        self.campoEditarFita.setObjectName("campoEditarFita")
        self.verticalLayout_4.addWidget(self.campoEditarFita)
        self.botaoUpload = QtWidgets.QPushButton(Frame)
        self.botaoUpload.setObjectName("botaoUpload")
        self.verticalLayout_4.addWidget(self.botaoUpload)
        self.botaoPlay = QtWidgets.QPushButton(Frame)
        self.botaoPlay.setObjectName("botaoPlay")
        self.verticalLayout_4.addWidget(self.botaoPlay)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.logConsole = QtWidgets.QLabel(Frame)
        self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 5, 5);")
        self.logConsole.setObjectName("logConsole")
        self.verticalLayout_5.addWidget(self.logConsole)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Simulador (Maquina de Turing)"))
        self.campoFita.setSortingEnabled(False)
        self.linhaComando.setToolTip(_translate("Frame", "<html><head/><body><p align=\"center\">Digite aqui ex: Q0,1=Q1,1,D</p><p align=\"center\">pode ser minusculas ou maiusculas não coloque (parenteses)</p></body></html>"))
        self.linhaComando.setWhatsThis(_translate("Frame", "<html><head/><body><p><br/></p></body></html>"))
        self.linhaComando.setPlaceholderText(_translate("Frame", "Digite aqui ex: Q0,1=Q1,1,D"))
        self.addComando.setText(_translate("Frame", "ADD"))
        self.limparLista.setText(_translate("Frame", "Limpar Lista"))
        self.removerComando.setText(_translate("Frame", "Remover "))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#da2805;\">Máquina </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#da2805;\">de Turing</span></p></body></html>"))
        self.boxPassoaPasso.setTitle(_translate("Frame", "Passo a Passo"))
        self.playPassoaPasso.setText(_translate("Frame", "Play>>"))
        self.label.setText(_translate("Frame", "Digite a fita aqui:"))
        self.campoEditarFita.setToolTip(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">A primeira letra (ou numero) indica onde a fita começa,<br/>a letra &quot;B&quot;(Maiusculo) indica o final do programa.</span></p></body></html>"))
        self.campoEditarFita.setPlaceholderText(_translate("Frame", "ex:10000000000B"))
        self.botaoUpload.setText(_translate("Frame", "UPLOADING -- (Reiniciar)"))
        self.botaoPlay.setText(_translate("Frame", "Play (Passo único)"))
        self.logConsole.setToolTip(_translate("Frame", "<html><head/><body><p><br/></p></body></html>"))
        self.logConsole.setWhatsThis(_translate("Frame", "<html><head/><body><p><br/></p></body></html>"))
        self.logConsole.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Erro!</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
