# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_exp.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDir
from PyQt4.QtGui import * 
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
#window to make the theming dynamic
#th = "w.jpg"
#class theme(QWidget):
#    def __init__(self):
 #       palette	= QPalette()
  # 	palette.setBrush(QPalette.Background,QBrush(QPixmap(th)))
#	Window.setPalette(palette)
#
 #       QWidget.__init__(self)
  #      w1 = QtGui.QPushButton("w1",self)
   #     w1.move(170,220)
    #    w1.resize(35,65)
     #   w1.clicked.connect(self.w1)
   # def w1(self):
    #    th="w1.jpg"    
     
	
	
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(775, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 150, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect( self.btn_click )
        self.treeView = QtGui.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 41, 291, 511))
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.treeView.clicked.connect( self.file_choose )
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(00, 10, 18,27))
        self.pushButton.setObjectName(_fromUtf8("thm"))
        self.pushButton.clicked.connect( self.th1 )
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 18, 27))
        self.pushButton.setObjectName(_fromUtf8("thm2"))
        self.pushButton.clicked.connect( self.th2 )
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 10, 18, 27))
        self.pushButton.setObjectName(_fromUtf8("thm2"))
        self.pushButton.clicked.connect( self.th3 )
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 10, 18, 27))
        self.pushButton.setObjectName(_fromUtf8("thm2"))
        self.pushButton.clicked.connect( self.th4 )
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 10, 18, 27))
        self.pushButton.setObjectName(_fromUtf8("thm2"))
        self.pushButton.clicked.connect( self.th5 )
        self.w = None
        palette	= QPalette()
   	palette.setBrush(QPalette.Background,QBrush(QPixmap("w1.jpg")))
	Window.setPalette(palette)


    def th1(self):
       
        palette	= QPalette()
   	palette.setBrush(QPalette.Background,QBrush(QPixmap("w.jpg")))
	Window.setPalette(palette)
        
    def th2(self):
        #self.w = theme()
        #self.w.show()
        palette	= QPalette()
   	palette.setBrush(QPalette.Background,QBrush(QPixmap("w1.jpg")))
	Window.setPalette(palette)
		

    def th3(self):
       
        palette	= QPalette()
   	palette.setBrush(QPalette.Background,QBrush(QPixmap("w2.jpg")))
	Window.setPalette(palette)
    def th4(self):
       
        palette	= QPalette()
   	palette.setBrush(QPalette.Background,QBrush(QPixmap("w3.jpg")))
	Window.setPalette(palette)
    
    def th5(self):
       
        palette	= QPalette()
   	palette.setBrush(QPalette.Background,QBrush(QPixmap("w4.jpg")))
	Window.setPalette(palette)
    def btn_click(self):
        file_dialog = QtGui.QFileDialog()
        folder = file_dialog.getExistingDirectory(None, "Select Folder")
        model = QtGui.QFileSystemModel()
        model.setRootPath(QDir.rootPath())
        self.model = model
        tree = self.treeView
        tree.setModel( model )
        tree.setRootIndex( model.index(folder) )
        tree.setColumnHidden(1, True)
        tree.setColumnHidden(2, True)
        tree.setColumnHidden(3, True)

    def file_choose(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())

        fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)
        print filePath

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "file explorer", None))
    


if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	Window = QtGui.QMainWindow()
	#applies the theme
	
	ui = Ui_MainWindow()
	ui.setupUi(Window)
	Window.show()
	sys.exit(app.exec_())
