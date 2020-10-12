from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QLabel

from Actions.home_page_action import Action


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        self.action = Action()
        super(Ui, self).__init__()
        uic.loadUi('interface.ui', self)
        self.login_name = self.findChild(QtWidgets.QLineEdit, 'login_name')
        self.password_value = self.findChild(QtWidgets.QLineEdit, 'password_value')
        self.min_com_word = self.findChild(QtWidgets.QSpinBox, 'min_word_value')
        self.min_followers = self.findChild(QtWidgets.QLineEdit, 'min_followers')
        self.max_followers = self.findChild(QtWidgets.QLineEdit, 'max_followers')
        self.info_text: QLabel() = self.findChild(QtWidgets.QLabel, 'info')
        self.run = self.findChild(QtWidgets.QPushButton, 'run')
        self.run.clicked.connect(self.printButtonPressed)
        self.show()

    def printButtonPressed(self):
        self.action.user.set_user_name(str(self.login_name.text()))
        self.action.user.set_user_password(str(self.password_value.text()))
        print("login name: ", self.action.user.get_user_name())
        print("password: ", self.action.user.get_user_password())
        self.info_text.setText(
            'login: ' + str(self.login_name.text()) +
            '\npassword: ' + str(self.password_value.text())
        )
        self.action.browser()

        print('printButtonPressed')


if __name__ == '__main__':
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = Ui()
        app.exec_()
    except:
        pass
