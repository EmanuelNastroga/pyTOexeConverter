# Programa criado por Emanuel Nastroga 2021
# converte .py em .exe arquivos que usam GUI

import os

from PySide2.QtCore import QObject, Signal
# pyinstaller myscript.py --onefile --windowed

import threading
# import PyInstaller.__main__
from PySide2.QtCore import QSize
from PySide2.QtGui import QMovie, QIcon

from gui import Ui_MainWindow
from PySide2 import QtWidgets
from PySide2.QtWidgets import QFileDialog, QMessageBox


# classe usada para enviar sinais á GUI
class Sinais(QObject):
    sinal = Signal()

    def __init__(self):
        QObject.__init__(self)




# função exibir animação gif
def movieLoading(play):

    if play:
        ui.label_2.setVisible(True)


    else:
        ui.label_2.setVisible(False)


# função abre janela para procura arquivo .py
def procurar_diretorio():
    diretorio = QFileDialog.getOpenFileName(filter = "python(*.py)")[0]
    ui.label.setText(diretorio)

    if diretorio.__len__()>0:
        ui.pushButton_2.setEnabled(True)

    # with open(diretorio, 'r') as f:
    #     ui.lineEdit.setText(f.read())
#função converte .py em .exe
def converter_py_exe():
    # pyinstaller - -onefile - -windowed myscript.py
    movieLoading(True)
    ui.pushButton_2.setEnabled(False)
    ui.pushButton.setEnabled(False)


    def converte():

        sinal1 = Sinais()
        sinal1.sinal.connect(finalizarConversao)
        # import PyInstaller.__main__
        #
        # PyInstaller.__main__.run([
        #
        #     f'{ui.label.text()}',
        #     '--onefile',
        #     '--windowed'
        # ])
        # while tarefa.is_alive():
        #     pass
        # sinal1.sinal.emit()
        try:
            # import PyInstaller.__main__
            # PyInstaller.__main__.run([
            #
            #     f'{ui.label.text()}',
            #     '--onefile',
            #     '--windowed',
            #     '--console'
            # ])
            os.system('color e')
            print(f'url: {ui.label.text()}')
            os.system(f'pyinstaller "{ui.label.text()}" --onefile --windowed --console ')
            # os.system(f'explorer.exe / e, / n,"{ui.label.text()}"')
            print('aqui na thread')

        except:
            print('erro')
        sinal1.sinal.emit()
        # movieLoading(False)
        # ui.pushButton_2.setEnabled(True)
        # ui.pushButton.setEnabled(True)
        # msgBox = QMessageBox()
        # msgBox.setText("conversão completa!")
        # msgBox.exec_()


    # converte()


    # trhead criada para conversão
    tarefa = threading.Thread(target=converte)  # cia tarefa paralela
    tarefa.daemon = True  # finaliza tarefa com  fim do script
    tarefa.start()  # inicia tarefa



def inicializarWarningMSG(exibir):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Conversão completa")
    # msg.setInformativeText("This is additional information")
    msg.setWindowTitle('completo')
    # msg.setDetailedText("The details are as follows:")

    # msg.setIconPixmap('Oxygen.ico')
    msg.setStyleSheet('background-color: rgb(205, 196, 147); border-top-color: rgb(205, 174, 82);')
    if(exibir):
        msg.exec_()

def finalizarConversao():
    movieLoading(False)
    ui.pushButton_2.setEnabled(True)
    ui.pushButton.setEnabled(True)





def main():
    # print('minha main')


    movie = QMovie('EYE_WALLEroxo.gif')
    ui.label_2.setMovie(movie)
    movie.setSpeed(160)
    rect = ui.label_2.geometry()
    size = QSize(min(rect.width(), rect.height()), min(rect.width(), rect.height()))
    movie.setScaledSize(size)
    movie.start()
    movieLoading(False)
    inicializarWarningMSG(False)


    ui.pushButton_2.setEnabled(False)
    ui.pushButton.clicked.connect(procurar_diretorio)
    ui.pushButton_2.clicked.connect(converter_py_exe)







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    main()
    sys.exit(app.exec_())