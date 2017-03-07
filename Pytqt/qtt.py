import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Window(QtGui.QMainWindow):
   def __init__(self):
	  super(Window, self).__init__()
	  self.initUI()						   

   def initUI(self):

	self.setGeometry(50,50,500,300)
	self.setWindowTitle("PYQT tut")
	self.setWindowIcon(QtGui.QIcon('pylogo.png'))


     
	exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
	exitAction.setShortcut('Ctrl+Q')
	exitAction.setStatusTip('Exit application')
	exitAction.triggered.connect(self.closeEvent)
   
	openEditor = QtGui.QAction('&Editor',self)
	openEditor.setShortcut('Ctrl+E')
	openEditor.setStatusTip('Open Editor')
	openEditor.triggered.connect(self.editor)



	openFile = QtGui.QAction('&Open File',self)
	openFile.setShortcut('Ctrl+O')
	openFile.setStatusTip('Open File')
	openFile.triggered.connect(self.file_open)



	
	

	saveFile = QtGui.QAction('&Save File',self)
	saveFile.setShortcut('Ctrl+S')
	saveFile.setStatusTip('Save File')
	saveFile.triggered.connect(self.file_save)

	mainmenu = self.menuBar()
	file_menu = mainmenu.addMenu('File')
	edit_menu = mainmenu.addMenu('Edit')
	view_menu = mainmenu.addMenu('View')
        theme_menu = mainmenu.addMenu('Theme')

	

	file_menu.addAction(openFile)
	file_menu.addAction(saveFile)
	file_menu.addAction(exitAction)

	edit_menu.addAction(openEditor)

	# super(tooldemo, self).__init__(parent)
	
	layout = QtGui.QVBoxLayout()
	tb = self.addToolBar("File")
	
	new = QtGui.QAction(QtGui.QIcon("new.jpg"),"new",self)

	tb.addAction(new)
	
	open = QtGui.QAction(QtGui.QIcon("open.jpg"),"open",self)
	open.triggered.connect(self.file_open)
	tb.addAction(open)
        
         
        
	edit = QtGui.QAction(QtGui.QIcon("edit.png"),"edit",self)
	edit.triggered.connect(self.editor)
	tb.addAction(edit)




        self.setWindowTitle("PYQT tut")
        self.show()

	save = QtGui.QAction(QtGui.QIcon("save.jpg"),"save",self)
	save.triggered.connect(self.file_save)
	tb.addAction(save)


	tb.actionTriggered[QtGui.QAction].connect(self.toolbtnpressed)
	self.setLayout(layout)
	
	self.setWindowTitle("PYQT tut")
   
   def toolbtnpressed(self,a):
	print "pressed tool button is",a.text()  


   def file_open(self):
	name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
	file = open(name,'r')

	self.editor()

	with file:
	   text = file.read()
	   self.textEdit.setText(text)

   def editor(self):
	self.textEdit = QtGui.QTextEdit()
	self.setCentralWidget(self.textEdit)

   def file_save(self):
	name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
	file = open(name,'w')
	text = self.textEdit.toPlainText()
	file.write(text)
	file.close()

   def closeEvent(self, event):

     quit_msg = "Are you sure you want to exit the program?"
     reply = QtGui.QMessageBox.question(self, 'Message', 
                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

     if reply == QtGui.QMessageBox.Yes:
        event.accept()
     else:
        event.ignore()

class QCustomTabWidget (QtGui.QTabWidget):
    def __init__ (self, parent = None):
        super(QCustomTabWidget, self).__init__(parent)
        # ex=Window()
        self.initUI()

    def initUI(self):

        self.setGeometry( 0, 0, 650, 350)
        self.tabwidget = QtGui.QTabWidget(self)
        self.tabwidget.setTabsClosable(True)
        self.tabwidget.tabCloseRequested.connect(self.closeTab)
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.tabwidget)
        self.setLayout(vbox)
        self.pages = []
        self.add_page()
        self.tabButton = QtGui.QToolButton(self)
        self.tabButton.setText('+')
        font = self.tabButton.font()
        font.setBold(True)
        self.tabButton.setFont(font)
        self.tabwidget.setCornerWidget(self.tabButton)
        self.tabButton.clicked.connect(self.add_page)
    
    def closeTab (self, currentIndex):
        currentQWidget = self.tabwidget.widget(currentIndex)
        currentQWidget.deleteLater()
        self.removeTab(currentIndex)

    def create_page(self):
        page = QtGui.QWidget()
        return page

    def add_page(self):
        self.pages.append(self.create_page())
        self.tabwidget.addTab(self.pages[-1] , 'Page %s' % len(self.pages) )
        self.tabwidget.setCurrentIndex( len(self.pages)-1 )

   


   
def main():
    
   app = QtGui.QApplication(sys.argv)
   ex = Window()
   myCustomTabWidget =QCustomTabWidget(ex)
   ex.show()

   sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
