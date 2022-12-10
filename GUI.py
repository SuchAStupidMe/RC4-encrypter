# -*- coding: utf-8 -*-

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QTabWidget, QFileDialog
from crypt import rc4_encrypt, rc4_decrypt


class Window(QTabWidget):

    def __init__(self):
        super(Window, self).__init__()
        loadUi("GUI.ui", self)
        self.setWindowTitle('RC4')
        self.show()

        # Activities
        self.browse_file.clicked.connect(self.browse_files)
        self.browse_file_2.clicked.connect(self.browse_files)
        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)

        # Properties
        self.password = None
        self.file_name = None

    def browse_files(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:')
        self.file_name = fname[0]
        self.filename_label.setText(self.file_name)
        self.filename_label_2.setText(self.file_name)

    def encrypt(self):
        self.password = self.password_line.text()
        rc4_encrypt(self.password, self.file_name)

    def decrypt(self):
        self.password = self.password_line_2.text()
        rc4_decrypt(self.password, self.file_name)


def app_launch():
    app = QApplication([])
    window = Window()
    app.exec_()
