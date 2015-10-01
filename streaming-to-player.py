#!/usr/bin/env python3

import subprocess
import os
import re
import sys
from PyQt4 import QtCore, QtGui
#from PyQt4 import QtGui

class MyPopup(QtGui.QWidget):
    def __init__(self, text):
        super(MyPopup, self).__init__()
        self.path = text

    def paintEvent(self, e):
        used = 1
        self.text = QtGui.QTextEdit(self)
        self.text.setText("""\
Non hai selezionato nulla!
Il file selezionato sarebe
%s
mentre dovrebbe essere della forma
"/proc/${PID}/fd/${FD}"
dove ${PID} e ${FD} sono numeri interi.""" % self.path)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.text)
        self.setLayout(layout)
        
        self.setWindowTitle("Attenzione!")
        self.setGeometry(0, 0, 250, 200)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        qr.moveCenter(QtGui.QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

class Stp(QtGui.QWidget):
    def __init__(self, arg, *args):
        super(Stp, self).__init__()
        self.initUI(arg)

    def center(self):
        qr = self.frameGeometry()
        qr.moveCenter(QtGui.QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

    def initVars(self):
        self.baseFilename = "/proc"
        self.filename = ""
        self.pid = ""
        self.fd = ""
        self.null = "/dev/null"
        self.ready = False
        
    def initCombos(self):
        self.pidCombo = QtGui.QComboBox(self)
        self.fdCombo = QtGui.QComboBox(self)

        self.pidCombo.move(20, 160)
        self.fdCombo.move(20, 210)

        self.initPid()

        self.pidCombo.activated[str].connect(self.onPid)
        self.fdCombo.activated[str].connect(self.onFd)

    def initPid(self):
        self.filename = self.baseFilename
        strings = subprocess.Popen(["ps", "x"], stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split("\n")
        regexp = re.compile(r"flash")

        for i in strings:
            if regexp.search(i) is not None:
                words = i.split()
                self.pidCombo.addItem(words[0])
                
    def onPid(self, text):
        self.ready = False
        self.filename = self.baseFilename
        self.filename = self.filename + "/" + text + "/fd"
        self.pid = text
        self.initFd()

    def initFd(self):
        if str(self.fdCombo.itemText(0)) == "":
            strings = subprocess.Popen(["ls", "-l", "-s", "-t", "-r", self.filename], stdout=subprocess.PIPE).communicate()[0].decode("utf-8").split("\n")
            regexp = re.compile(r"Flash")
        
            for i in strings:
                if regexp.search(i) is not None:
                    words = i.split()
                    self.fdCombo.addItem(words[9])

    def isReady(self):
        regexp = re.compile(r"^/proc/[0-9]+/fd/[0-9]+$")
        if regexp.search(self.filename) is not None:
            return True
        else:
            return False

    def onFd(self, text):
        regexp = re.compile(r"/proc/[0-9]+/fd")
        while not regexp.search(self.filename):
            onPid(str(self.pidCombo.itemText(0)))
            
        self.filename = self.filename + "/" + text
        self.fd = text
        self.ready = True

    def autoSelect(self):
        if (str(self.pidCombo.itemText(0)) != "") and (self.pid == ""):
            self.filename = self.filename + "/" + str(self.pidCombo.itemText(0)) + "/fd"
            self.pid = str(self.pidCombo.itemText(0))
            self.initFd()

        if (str(self.fdCombo.itemText(0)) != "") and (self.fd == ""):
            self.filename = self.filename + "/" + str(self.fdCombo.itemText(0))
            self.fd = str(self.fdCombo.itemText(0))
            self.ready = True

    def openFile(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(self, "Open File", self.filename)
        self.ready = True

    def openPlayer(self):
        if self.ready and self.isReady():
            subprocess.Popen(["vlc", self.filename, "2>%s"%self.null, ">%s"%self.null], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            sys.exit()
        self.popupAlert()

    def popupAlert(self):
        self.popup = MyPopup(self.filename)
        self.filename = self.baseFilename
        self.ready = False
        self.pid = ""
        self.fd = ""
        self.popup.show()
        
    def close(self):
        sys.exit()

    def initUI(self, arg):
        self.auto = QtGui.QPushButton("Auto-Select", self)
        self.auto.clicked.connect(self.autoSelect)
        self.search = QtGui.QPushButton("Search", self)
        self.search.clicked.connect(self.openFile)
        self.done = QtGui.QPushButton("Done", self)
        self.done.clicked.connect(self.openPlayer)
        
        self.text = QtGui.QTextEdit()
        self.text.setText("""\
Il primo menu a tendina è per il browser, generalmente ne compare
uno solo.
Il secondo è il video, questi, benchè numeri, vengono mostrati
in ordine di creazione, dal piu vecchio.""")

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(self.auto)
        layout.addWidget(self.search)
        layout.addWidget(self.done)
        
        self.setLayout(layout)
        self.initVars()
        self.initCombos()

        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("Streaming-to-Player")
        self.center()
        self.show()

        self.autoSelect()

        if arg == 'auto':
            self.openPlayer()

    def keyPressEvent(self, e):
        if e.key() == (QtCore.Qt.Key_Control and QtCore.Qt.Key_Q):
            sys.exit()

def main(arg):
    app = QtGui.QApplication(sys.argv)
    executable = Stp(arg)
    sys.exit(app.exec_())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'auto':
            main(sys.argv[1])
    main('')
