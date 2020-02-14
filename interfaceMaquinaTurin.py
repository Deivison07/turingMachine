from PyQt5 import QtCore, QtGui, QtWidgets
from maquinaTurin import Ui_Frame
import fix_qt_import_error
import sys

class main (QtWidgets.QWidget,Ui_Frame):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.botaoUpload.clicked.connect(self.fita)
        self.playPassoaPasso.clicked.connect(self.passos)
        self.addComando.clicked.connect(self.comandos)
        self.limparLista.clicked.connect(self.limpar)
        self.removerComando.clicked.connect(self.removerItem)
        self.listaComando.itemClicked.connect(self.itemClicado)
        self.botaoPlay.clicked.connect(self.playPassoUnico)
        self.linhaComando.returnPressed.connect(self.comandos)
        
        self.lista = []
        self.ponteiro = 0 
        self.anterior = 0
        self.dicionario = {}
        self.itemParaRemover = 0
        self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.logConsole.setText('')
        
        
    def fita(self):
        self.lista = []
        self.campoFita.clear()
        
        letra = self.campoEditarFita.toPlainText()
        self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.logConsole.setText('')
        try:
            for itens in letra:
                itens = itens.upper()
                if itens != ' ' and itens != '\n':
                    
                    self.lista.append(itens)
                    
                    item = QtWidgets.QListWidgetItem()
                    font = QtGui.QFont()
                    font.setPointSize(11)
                    item.setFont(font)
                    item.setText(itens)
                    self.campoFita.addItem(item)
                    
            self.lista.append('fim')
            
            self.indexPasso = 0
            self.ponteiroPasso = 'Q0,'+ self.lista[0]
            
            brush = QtGui.QBrush(QtGui.QColor(225, 41, 4))
            brush.setStyle(QtCore.Qt.SolidPattern)
            self.campoFita.item(self.indexPasso).setBackground(brush)
            self.logConsole.setText(self.ponteiroPasso)
            
        except:
            self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 5, 5);")
            self.logConsole.setText('Erro!')
            
                
    def play(self):
        
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        self.campoFita.item(self.anterior).setBackground(brush)
        
        brush = QtGui.QBrush(QtGui.QColor(225, 41, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.campoFita.item(self.ponteiro).setBackground(brush)
        
        self.ponteiro+=1
        self.anterior = self.ponteiro-1
        
    def comandos(self):
        
        if self.linhaComando.text().count('=')==1 and self.linhaComando.text().count(',')==3 and '(' not in self.linhaComando.text() and ')' not in self.linhaComando.text():
            
            palavra = self.linhaComando.text()
            palavra = palavra.upper()
            chave = palavra.split('=')
            valor = chave[1].split(',')
            
            if chave[0] not in self.dicionario.keys():
                self.dicionario[chave[0]] = valor[0],valor[1],valor[2]
                self.listaComando.addItem('{} = {},{},{}'.format(chave[0],valor[0],valor[1],valor[2]))
                print(self.dicionario)
                self.linhaComando.clear()
                self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(15, 255, 63);")
                self.logConsole.setText('Comando Adicionado!!')
        else:
            self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 5, 5);")
            self.logConsole.setText('Erro de Formatação ou a Chave já existe!')
            self.linhaComando.clear()
    
    def limpar(self):
        self.listaComando.clear()
        self.dicionario.clear()
        self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(15, 255, 63);")
        self.logConsole.setText('Lista de comandos limpa!')
        
    def removerItem(self):
        try:
            remover = self.listaComando.row(self.itemParaRemover)
            
            self.listaComando.takeItem(remover)
            
            remover = self.itemParaRemover.text().split(' = ')
            
            if remover[0] in self.dicionario.keys():
                del(self.dicionario[remover[0]])
                self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(15, 255, 63);")
                self.logConsole.setText('Item Removido')
            
                print(self.dicionario)
        except:
            print('aqui')
        
    def itemClicado(self,item):
        self.itemParaRemover = item
        
    def playPassoUnico(self):
        try:
            index = 0
            ponteiro = 'Q0,'+ self.lista[0]
            while(1):
                
                #letra = self.lista[index]
                    
                if  ponteiro.split(',')[0] == 'QF':
                    self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(15, 255, 63);")
                    self.logConsole.setText('Programa Finalisou com sucesso ')
                    
                    break
                else:
                    if ponteiro in self.dicionario.keys():
                        if self.dicionario[ponteiro][2] == 'D':
                            
                            self.lista[index] = self.dicionario[ponteiro][1]
                            self.campoFita.item(index).setText(self.dicionario[ponteiro][1])
                            index = index + 1 
                            self.campoFita.scrollToItem(self.campoFita.item(index))
                            try:
                                ponteiro = str(self.dicionario[ponteiro][0]+','+self.lista[index])
                            except:
                                self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(255, 5, 5);")
                                self.logConsole.setText('Ponteiro Fora Da Fita Erro Fatal!')
                                
                                break
                            
                        else: 
                            
                            if self.dicionario[ponteiro][2] == 'E' and index > 0:
                                self.lista[index] = self.dicionario[ponteiro][1]
                                self.campoFita.item(index).setText(self.dicionario[ponteiro][1])
                                index = index - 1 
                                self.campoFita.scrollToItem(self.campoFita.item(index))
                                self.ponteiro = str(self.dicionario[ponteiro][0]+','+self.lista[index])
                            else:
                                self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(255, 5, 5);")
                                self.logConsole.setText('ponteiro fora da Fita Erro Fatal!')
                                
                                break
                    
                        print(ponteiro)
                        print(self.lista)
                    else:
                        self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(255, 5, 5);")
                        self.logConsole.setText("Este ponteiro nao existe! Fim de programa!")
                        break
                    
        except:
            pass
              
    def passos(self):  
        
        try:
        
            try:
                brush = QtGui.QBrush(QtGui.QColor(225, 255, 255))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.campoFita.item(self.indexPasso).setBackground(brush)
            except:
                pass
                    
            if  self.ponteiroPasso.split(',')[0] == 'QF':
                self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(15, 255, 63);")
                self.logConsole.setText("Programa Finalisou com sucesso ")
            
            else:
                if self.ponteiroPasso in self.dicionario.keys():
                    if self.dicionario[self.ponteiroPasso][2] == 'D':
                        
                        self.lista[self.indexPasso] = self.dicionario[self.ponteiroPasso][1]
                        self.campoFita.item(self.indexPasso).setText(self.dicionario[self.ponteiroPasso][1])
                        self.indexPasso = self.indexPasso + 1 
                        self.campoFita.scrollToItem(self.campoFita.item(self.indexPasso))
                        try:
                            self.ponteiroPasso = str(self.dicionario[self.ponteiroPasso][0]+','+self.lista[self.indexPasso])
                        except:
                            self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(255, 5, 5);")
                            self.logConsole.setText('Ponteiro Fora Da Fita Erro Fatal!')
                        
                    else: 
                        
                        if self.dicionario[self.ponteiroPasso][2] == 'E' and self.indexPasso > 0:
                            self.lista[self.indexPasso] = self.dicionario[self.ponteiroPasso][1]
                            self.campoFita.item(self.indexPasso).setText(self.dicionario[self.ponteiroPasso][1])
                            self.indexPasso = self.indexPasso - 1 
                            self.campoFita.scrollToItem(self.campoFita.item(self.indexPasso))
                            self.ponteiroPasso = str(self.dicionario[self.ponteiroPasso][0]+','+self.lista[self.indexPasso])
                        else:
                            self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(255, 5, 5);")
                            self.logConsole.setText('Ponteiro fora da Fita Erro Fatal!')
                
                    print(self.ponteiroPasso)
                    
                    self.logConsole.setText(self.ponteiroPasso)

                    print(self.lista)
                else:
                    self.logConsole.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";\n"
    "background-color: rgb(255, 5, 5);")
                    self.logConsole.setText("Este ponteiro nao existe! Fim de programa!")
            try:       
                brush = QtGui.QBrush(QtGui.QColor(225, 2, 5))
                brush.setStyle(QtCore.Qt.SolidPattern)
                self.campoFita.item(self.indexPasso).setBackground(brush)
            except:
                pass
        except:
            print('Deu errado')
            pass
    

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = main()
    ui.show()
    sys.exit(app.exec_())
    
    