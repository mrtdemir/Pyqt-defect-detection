# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covision.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

#import process
from PyQt5 import QtCore, QtGui, QtWidgets, uic
#import process
import sys
import time
import qdarkgraystyle
import shutil
class Ui_MainWindow(object):
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.setEnabled(True)
        MainWindow.resize(1370, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1370, 575))
        MainWindow.setMaximumSize(QtCore.QSize(1370, 575))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setWindowIcon(QtGui.QIcon('miniicon.png'))
        MainWindow.setToolTip("")
        MainWindow.setToolTipDuration(-1)
        MainWindow.setStatusTip("")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openFile = QtWidgets.QPushButton(self.centralwidget)
        self.openFile.setGeometry(QtCore.QRect(560, 290, 260, 40))

        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setKerning(True)

        self.openFile.setFont(font)

        self.openFile.setFocusPolicy(QtCore.Qt.TabFocus)
        self.openFile.setAutoDefault(False)

        self.openFile.setObjectName("openFile")
        self.FirstImage = QtWidgets.QLabel(self.centralwidget)
        self.FirstImage.setGeometry(QtCore.QRect(30, 40, 500, 500))

        self.FirstImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FirstImage.setText("")
        self.FirstImage.setObjectName("FirstImage")
        self.buttonProcess = QtWidgets.QPushButton(self.centralwidget)

        self.buttonProcess.setGeometry(QtCore.QRect(560, 330, 260, 60))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.buttonProcess.setFont(font)
        self.buttonProcess.setObjectName("buttonProcess")
        self.LastImage = QtWidgets.QLabel(self.centralwidget)

        self.LastImage.setGeometry(QtCore.QRect(840, 40, 500, 500))

        self.LastImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LastImage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LastImage.setLineWidth(-1)
        self.LastImage.setText("")
        self.LastImage.setObjectName("LastImage")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 540, 1311, 31))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setToolTipDuration(-1)

        self.progressBar.setProperty("value", 0)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setObjectName("progressBar")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 10, 221, 141))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        self.saveAs = QtWidgets.QPushButton(self.centralwidget)
        self.saveAs.setGeometry(QtCore.QRect(560, 390, 260, 40))
        self.saveAs.setObjectName("pushButton")
        self.xmlRatio = QtWidgets.QRadioButton(self.centralwidget)
        self.xmlRatio.setGeometry(QtCore.QRect(570, 220, 51, 20))
        self.xmlRatio.setObjectName("xmlRatio")
        self.jsonRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.jsonRadio.setGeometry(QtCore.QRect(660, 220, 61, 20))
        self.jsonRadio.setObjectName("jsonRadio")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(630, 190, 181, 21))
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plainTextEdit.setMaximumBlockCount(1)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 190, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1030, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.csvRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.csvRadio.setGeometry(QtCore.QRect(760, 220, 51, 20))
        self.csvRadio.setObjectName("csvRadio")
        self.sendToServer = QtWidgets.QPushButton(self.centralwidget)
        self.sendToServer.setGeometry(QtCore.QRect(560, 250, 260, 30))
        self.sendToServer.setObjectName("sendToServer")


        MainWindow.setCentralWidget(self.centralwidget)

        #openfile.button
        self.openFile.clicked.connect(self.getfile)
        #end of openfile

        #process.button
        self.buttonProcess.clicked.connect(self.processPicture)
        #end of process

        #saveAs.button
        self.saveAs.clicked.connect(self.saveImage)
        #end of saveAs

        #diasble button
        self.buttonProcess.setEnabled(False)
        self.saveAs.setEnabled(False)
        self.sendToServer.setEnabled(False)
        self.jsonRadio.setEnabled(False)
        self.xmlRatio.setEnabled(False)
        self.csvRadio.setEnabled(False)
        self.plainTextEdit.setEnabled(False)
        self.label_2.setEnabled(False)
        #end of disable button
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CoVsion"))
        self.openFile.setText(_translate("MainWindow", "Open Image File"))
        self.buttonProcess.setText(_translate("MainWindow", "Process Image"))
        self.saveAs.setText(_translate("MainWindow", "Save Result as..."))
        self.xmlRatio.setText(_translate("MainWindow", "XML"))
        self.jsonRadio.setText(_translate("MainWindow", "JSON"))
        self.label_2.setText(_translate("MainWindow", "SERVER:"))
        self.label_3.setText(_translate("MainWindow", "IMAGE PREVİEW"))
        self.label_5.setText(_translate("MainWindow", "RESULT PREVİEW"))
        self.csvRadio.setText(_translate("MainWindow", "CSV"))
        self.sendToServer.setText(_translate("MainWindow", "Send to Server"))
        
    
    def saveImage(self):
        savefile, _ = QtWidgets.QFileDialog.getSaveFileName(None,"Save File",'..',"Image Files (*.png *.jpg *.bmp)")
        print(savefile)
        shutil.copy2('deneme.png',savefile)
        


    def processPicture(self):

        #process.processStart(self.imagePath)
        self.pixmap = QtGui.QPixmap('deneme.PNG')
        progress = 0
        while progress<81:
            self.progressBar.setValue(progress)
            progress+=10
            time.sleep(1)

        while self.pixmap.isNull():
            self.pixmap = QtGui.QPixmap('deneme.PNG')
            progress+=1
            time.sleep(0.5)
            self.progressBar.setValue(progress)

        self.progressBar.setValue(100)
        self.pixmap2 = self.pixmap.scaled(QtCore.QSize(500,500),QtCore.Qt.KeepAspectRatio)
        self.LastImage.setPixmap(QtGui.QPixmap(self.pixmap2))

        self.saveAs.setEnabled(True)
        self.sendToServer.setEnabled(True)
        self.jsonRadio.setEnabled(True)
        self.xmlRatio.setEnabled(True)
        self.csvRadio.setEnabled(True)
        self.plainTextEdit.setEnabled(True)
        self.label_2.setEnabled(True)


    def getfile(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", '..', "Image Files (*.png *.jpg *.bmp)")
        self.imagePath = self.fname[0]
        pixmap4 = QtGui.QPixmap(self.imagePath)
        pixmap3 = pixmap4.scaled(QtCore.QSize(500,500),QtCore.Qt.KeepAspectRatio)
        self.FirstImage.setPixmap(QtGui.QPixmap(pixmap3))
        self.buttonProcess.setEnabled(True)
    def __init__(self):
        self.fname = None
        self.imagePath = None
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
