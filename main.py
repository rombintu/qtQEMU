import sys
import form
import os

from functions import createDisk, deleteDisk, startVM, bootCar, converToRaw
from PyQt5 import QtWidgets


class App(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.chooseCar)
        self.pushButton.clicked.connect(self.startCar)
        self.action.triggered.connect(self.createNewDisk)
        self.action_2.triggered.connect(self.bootNewCar)
        self.action_3.triggered.connect(self.deleteCar)
        self.action_4.triggered.connect(self.converting)
        self.action_iso.triggered.connect(self.bootIso)

    def createNewDisk(self):
        pathDir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбери папку для диска")
        newDisk, yes = QtWidgets.QInputDialog.getText(self, 'Новый диск', 'Название нового диска:')
        sizeDisk, yes2 = QtWidgets.QInputDialog.getText(self, 'Новый диск', 'Размер нового диска (GB):')
        if yes and yes2:
            try:
                createDisk(pathDir, newDisk, sizeDisk)
            except Exception as e:
                errorWin = QtWidgets.QErrorMessage(self)
                errorWin.showMessage(str(e))
                return False

    def bootNewCar(self):
        isoFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбери файл "iso"', os.path.abspath(os.curdir), '*.iso')[0]
        pathToDisk = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбери диск', os.path.abspath(os.curdir), '*.qcow *.raw')[0]
        countMem, yes = QtWidgets.QInputDialog.getText(self, 'Новая машина', 'Сколько ОЗУ выделить (MB):')
        if yes:
            try:
                bootCar(pathToDisk, isoFile, countMem)
            except Exception as e:
                errorWin = QtWidgets.QErrorMessage(self)
                errorWin.showMessage(str(e))
                return False

    def deleteCar(self):
        pathToDisk = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбери диск для удаления', os.path.abspath(os.curdir), '*.qcow *.raw')[0]
        try:
            deleteDisk(pathToDisk)
        except Exception as e:
            errorWin = QtWidgets.QErrorMessage(self)
            errorWin.showMessage(str(e))
            return False

    def chooseCar(self):
        pathToCar = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбери файл', os.path.abspath(os.curdir), '*.qcow *.img *.raw')[0]
        self.lineEdit.setText(pathToCar)

    def startCar(self):
        memCount = self.comboBox.currentText()
        nameCar = self.lineEdit.text()
        kvmStatus = self.checkBox.checkState()
        try:
            startVM(nameCar, memCount, kvmStatus)
        except Exception as e:
            errorWin = QtWidgets.QErrorMessage(self)
            errorWin.showMessage(str(e))
            return False

    def converting(self):
        pathToDisk = \
        QtWidgets.QFileDialog.getOpenFileName(self, 'Выбери диск', os.path.abspath(os.curdir), '*.qcow')[0]
        try:
            converToRaw(pathToDisk)
        except Exception as e:
            errorWin = QtWidgets.QErrorMessage(self)
            errorWin.showMessage(str(e))
            return False

    def bootIso(self):
        isoFile = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбери файл "iso"', os.path.abspath(os.curdir), '*.iso')[0]
        countMem, yes = QtWidgets.QInputDialog.getText(self, 'Новая машина', 'Сколько ОЗУ выделить (MB):')
        if yes:
            try:
                bootCar(False, isoFile, countMem)
            except Exception as e:
                errorWin = QtWidgets.QErrorMessage(self)
                errorWin.showMessage(str(e))
                return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    app.exec_()
