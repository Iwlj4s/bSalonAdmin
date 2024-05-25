from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QPushButton, QSizePolicy, QTextBrowser, QWidget)

from ui.pyui.AddUserWindow import Ui_AddUserWindow


class Ui_AdminWindow(object):
    def __init__(self, main_window, session, user_name):
        self.main_window = main_window
        self.session = session

        self.user_name = user_name

    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(764, 364)

        # ADMIN NAME #
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.admin_name_label = QLabel(self.centralwidget)
        self.admin_name_label.setObjectName(u"admin_name_label")
        self.admin_name_label.setGeometry(QRect(270, 20, 221, 21))
        font = QFont()
        font.setPointSize(20)
        self.admin_name_label.setFont(font)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(140, 70, 421, 71))
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.admin_name = QLabel(self.frame)
        self.admin_name.setObjectName(u"admin_name")
        self.admin_name.setGeometry(QRect(10, 20, 181, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.admin_name.setFont(font1)

        # admin name text
        self.admin_name_text = QTextBrowser(self.frame)
        self.admin_name_text.setObjectName(u"admin_name_text")
        self.admin_name_text.setGeometry(QRect(180, 20, 211, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.admin_name_text.setFont(font2)
        self.admin_name_text.setText(self.user_name)


        # BUTTONS FRAME #
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(220, 220, 301, 71))
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)

        # add user button
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 10, 171, 21))

        self.pushButton.clicked.connect(lambda: self.open_add_user_Window(self.main_window))

        # EXIT BUTTON #
        self.exit_button = QPushButton(self.frame_2)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(70, 40, 171, 21))
        self.exit_button.setAcceptDrops(False)
        self.exit_button.setCheckable(False)
        self.exit_button.setAutoRepeat(False)
        self.exit_button.setAutoExclusive(False)

        self.exit_button.clicked.connect(lambda: self.open_main_Window(AdminWindow))

        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)

        QMetaObject.connectSlotsByName(AdminWindow)

    # setupUi

    def open_main_Window(self, UserWindow):
        self.main_window.show()
        UserWindow.hide()

    def open_add_user_Window(self, MainWindow):
        self.add_user_Window = QtWidgets.QMainWindow()
        self.ui_add_user = Ui_AddUserWindow(MainWindow, self.session)
        self.ui_add_user.setupUi(self.add_user_Window)

        self.add_user_Window.show()
        MainWindow.hide()

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"MainWindow", None))
        self.admin_name_label.setText(QCoreApplication.translate("AdminWindow",
                                                                 u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442",
                                                                 None))
        self.admin_name.setText(QCoreApplication.translate("AdminWindow",
                                                           u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440",
                                                           None))
        self.pushButton.setText(QCoreApplication.translate("AdminWindow",
                                                           u"\u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439",
                                                           None))
        self.exit_button.setText(QCoreApplication.translate("AdminWindow",
                                                            u"\u0412\u044b\u0445\u043e\u0434 \u0438\u0437 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430",
                                                            None))
    # retranslateUi
