from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QWidget, QMessageBox)

from checks.user_check import user_in_db, admin_in_db
from ui.pyui.AdminWindow import Ui_AdminWindow


class Ui_MainWindow(object):
    def __init__(self, session):
        self.session = session

        self.success_message = str("Пользователь авторизован")
        self.failure_message = str("Вы ввели некорректный пароль или некорректное имя пользователя")

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 367)

        self.main_window = MainWindow

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 20, 71, 31))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)

        # SIGN UP BUTTON #
        self.sign_up_button = QPushButton(self.centralwidget)
        self.sign_up_button.setObjectName(u"sign_up_button")
        self.sign_up_button.setGeometry(QRect(250, 230, 111, 31))
        self.sign_up_button.setCheckable(False)
        self.sign_up_button.setChecked(False)
        self.sign_up_button.setAutoRepeat(False)
        self.sign_up_button.setAutoExclusive(False)
        self.sign_up_button.setAutoDefault(False)
        self.sign_up_button.setFlat(False)

        self.sign_up_button.clicked.connect(self.open_admin_Window)

        # USER NAME ADN PASSWORD FRAME #
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(140, 70, 351, 141))
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Sunken)

        # user name
        self.user_name_label = QLabel(self.frame)
        self.user_name_label.setObjectName(u"user_name_label")
        self.user_name_label.setGeometry(QRect(90, 20, 161, 21))
        font1 = QFont()
        font1.setPointSize(14)
        self.user_name_label.setFont(font1)
        self.user_name_input = QLineEdit(self.frame)
        self.user_name_input.setObjectName(u"user_name_input")
        self.user_name_input.setGeometry(QRect(60, 50, 221, 21))
        font2 = QFont()
        font2.setPointSize(12)
        self.user_name_input.setFont(font2)

        # password
        self.password_input = QLineEdit(self.frame)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(60, 110, 221, 21))
        self.password_input.setFont(font2)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_label = QLabel(self.frame)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(130, 80, 71, 21))
        self.password_label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sign_up_button.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi
    def show_success_message(self, u_name, main_window):
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText(self.success_message)

        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        button = msg.exec()

        if button == QMessageBox.StandardButton.Ok:
            self.user_name_input.clear()
            self.password_input.clear()

            self.admin_Window = QtWidgets.QMainWindow()
            self.ui_admin = Ui_AdminWindow(session=self.session,
                                           user_name=u_name,
                                           main_window=main_window)
            self.ui_admin.setupUi(self.admin_Window)

            self.admin_Window.show()
            main_window.hide()

    def show_failure_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Failure")
        msg.setText(self.failure_message)

        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        button = msg.exec()

    def open_admin_Window(self):
        session = self.session

        u_name = self.user_name_input.text()
        u_password = self.password_input.text()
        print(u_name)
        print(u_password)

        admin_db = admin_in_db(user_name=u_name, user_password=u_password, session=session)
        if admin_db:
            print(u_name)
            print(u_password)
            self.show_success_message(u_name=u_name, main_window=self.main_window)
        else:
            self.show_failure_message()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.sign_up_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.user_name_label.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                                                                None))
        self.password_label.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi
