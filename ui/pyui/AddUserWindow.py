from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QListWidget, QListWidgetItem, QMainWindow, QPushButton,
                               QSizePolicy, QTextBrowser, QWidget, QMessageBox)

from database.orm_query import orm_user_add_info, orm_delete_user
from utils.utils import count_list_items, get_users_list


class Ui_AddUserWindow(object):
    def __init__(self, main_window, session):
        self.main_window = main_window
        self.session = session

        self.item = count_list_items(self.session)
        self.user_data = {}
        self.found = False

        self.success_message = str("Вы успешно добавили пользователя!")
        self.failure_message = str("Ошибка")

    def setupUi(self, AddUserWindow):
        if not AddUserWindow.objectName():
            AddUserWindow.setObjectName(u"AddUserWindow")
        AddUserWindow.resize(649, 651)
        self.centralwidget = QWidget(AddUserWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # USER INFO FRAME #
        self.user_info_frame = QFrame(self.centralwidget)
        self.user_info_frame.setObjectName(u"user_info_frame")
        self.user_info_frame.setGeometry(QRect(20, 20, 381, 311))
        self.user_info_frame.setFrameShape(QFrame.WinPanel)
        self.user_info_frame.setFrameShadow(QFrame.Sunken)

        # NAME#
        # label
        self.name_label = QLabel(self.user_info_frame)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(60, 30, 61, 25))
        font = QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        # Input
        self.name_input = QLineEdit(self.user_info_frame)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(140, 30, 167, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_input.sizePolicy().hasHeightForWidth())
        self.name_input.setSizePolicy(sizePolicy)
        self.name_input.setSizeIncrement(QSize(40, 0))
        font1 = QFont()
        font1.setPointSize(12)
        self.name_input.setFont(font1)

        # PHONE
        # Input
        self.phone_input = QLineEdit(self.user_info_frame)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setGeometry(QRect(140, 70, 167, 25))
        sizePolicy.setHeightForWidth(self.phone_input.sizePolicy().hasHeightForWidth())
        self.phone_input.setSizePolicy(sizePolicy)
        self.phone_input.setSizeIncrement(QSize(40, 0))
        self.phone_input.setFont(font1)
        # label
        self.phone_label = QLabel(self.user_info_frame)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setGeometry(QRect(60, 70, 77, 25))
        self.phone_label.setFont(font)

        # EMAIL
        # label
        self.email_label = QLabel(self.user_info_frame)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(60, 110, 61, 25))
        self.email_label.setFont(font)
        # Input
        self.email_input = QLineEdit(self.user_info_frame)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(140, 110, 167, 25))
        sizePolicy.setHeightForWidth(self.email_input.sizePolicy().hasHeightForWidth())
        self.email_input.setSizePolicy(sizePolicy)
        self.email_input.setSizeIncrement(QSize(40, 0))
        self.email_input.setFont(font1)

        # SERVICE
        # label
        self.service_label = QLabel(self.user_info_frame)
        self.service_label.setObjectName(u"service_label")
        self.service_label.setGeometry(QRect(60, 150, 61, 25))
        self.service_label.setFont(font)
        # Input
        self.service_input = QLineEdit(self.user_info_frame)
        self.service_input.setObjectName(u"service_input")
        self.service_input.setGeometry(QRect(140, 150, 167, 25))
        sizePolicy.setHeightForWidth(self.service_input.sizePolicy().hasHeightForWidth())
        self.service_input.setSizePolicy(sizePolicy)
        self.service_input.setSizeIncrement(QSize(40, 0))
        self.service_input.setFont(font1)

        # MASTER
        # label
        self.master_label = QLabel(self.user_info_frame)
        self.master_label.setObjectName(u"master_label")
        self.master_label.setGeometry(QRect(60, 190, 71, 25))
        self.master_label.setFont(font)
        # Input
        self.mster_input = QLineEdit(self.user_info_frame)
        self.mster_input.setObjectName(u"mster_input")
        self.mster_input.setGeometry(QRect(140, 190, 167, 25))
        sizePolicy.setHeightForWidth(self.mster_input.sizePolicy().hasHeightForWidth())
        self.mster_input.setSizePolicy(sizePolicy)
        self.mster_input.setSizeIncrement(QSize(40, 0))
        self.mster_input.setFont(font1)

        # DATA
        # Input
        self.data_input = QLineEdit(self.user_info_frame)
        self.data_input.setObjectName(u"data_input")
        self.data_input.setGeometry(QRect(140, 230, 167, 25))
        sizePolicy.setHeightForWidth(self.data_input.sizePolicy().hasHeightForWidth())
        self.data_input.setSizePolicy(sizePolicy)
        self.data_input.setSizeIncrement(QSize(40, 0))
        self.data_input.setFont(font1)
        # label
        self.data_label = QLabel(self.user_info_frame)
        self.data_label.setObjectName(u"data_label")
        self.data_label.setGeometry(QRect(60, 230, 71, 25))
        self.data_label.setFont(font)

        # TIME
        # label
        self.time_label = QLabel(self.user_info_frame)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(60, 270, 71, 25))
        self.time_label.setFont(font)
        # Input
        self.time_input = QLineEdit(self.user_info_frame)
        self.time_input.setObjectName(u"time_input")
        self.time_input.setGeometry(QRect(140, 270, 167, 25))
        sizePolicy.setHeightForWidth(self.time_input.sizePolicy().hasHeightForWidth())
        self.time_input.setSizePolicy(sizePolicy)
        self.time_input.setSizeIncrement(QSize(40, 0))
        self.time_input.setFont(font1)

        # LIST FRAME #
        self.list_frame = QFrame(self.centralwidget)
        self.list_frame.setObjectName(u"list_frame")
        self.list_frame.setGeometry(QRect(10, 380, 621, 261))
        self.list_frame.setFrameShape(QFrame.WinPanel)
        self.list_frame.setFrameShadow(QFrame.Sunken)

        # user list
        self.user_list = QListWidget(self.list_frame)
        self.user_list.setObjectName(u"user_list")
        self.user_list.setGeometry(QRect(10, 20, 591, 191))
        self.user_list.setFont(font)

        self.users = get_users_list(self.session)
        for user_info in self.users.split("\n"):
            item = QListWidgetItem(user_info)
            self.user_list.addItem(item)

        # USER COUNT #
        # label
        self.user_count_label = QLabel(self.list_frame)
        self.user_count_label.setObjectName(u"user_count_label")
        self.user_count_label.setGeometry(QRect(10, 230, 47, 13))

        # user count
        self.user_count = QTextBrowser(self.list_frame)
        self.user_count.setObjectName(u"user_count")
        self.user_count.setGeometry(QRect(60, 230, 51, 21))

        self.user_count.setText(self.item)

        # List label
        self.list_label = QLabel(self.centralwidget)
        self.list_label.setObjectName(u"list_label")
        self.list_label.setGeometry(QRect(20, 350, 81, 21))
        self.list_label.setFont(font)

        # BUTTON FRAME #
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(450, 50, 171, 191))
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Sunken)

        # add button
        self.add_button = QPushButton(self.frame)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(30, 10, 101, 31))

        self.add_button.clicked.connect(self.add_user)

        # delete button
        self.delete_button = QPushButton(self.frame)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(30, 50, 101, 31))

        self.delete_button.clicked.connect(self.delete_user)

        # Sign Up button
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 160, 101, 21))

        self.pushButton.clicked.connect(lambda: self.open_main_Window(AddUserWindow))

        # search button
        self.search_user_button = QPushButton(self.frame)
        self.search_user_button.setObjectName(u"search_user_button")
        self.search_user_button.setGeometry(QRect(30, 110, 101, 31))

        self.search_user_button.clicked.connect(self.search_user)

        AddUserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddUserWindow)

        QMetaObject.connectSlotsByName(AddUserWindow)

    # setupUi

    def show_success_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText(self.success_message)

        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        button = msg.exec()

        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.service_input.clear()
        self.mster_input.clear()

    def show_failure_message(self, error):
        msg = QMessageBox()
        msg.setWindowTitle("Failure")
        msg.setText(self.failure_message)

        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        button = msg.exec()

    def open_main_Window(self, AddUserWindow):
        self.main_window.show()
        AddUserWindow.hide()

    def add_user(self):
        self.user_data["user_name"] = self.name_input.text()
        self.user_data["user_phone"] = self.phone_input.text()
        self.user_data["user_email"] = self.email_input.text()
        self.user_data["user_service"] = self.service_input.text()
        self.user_data["user_master"] = self.mster_input.text()
        self.user_data["user_appointment_data"] = self.data_input.text()
        self.user_data["user_time"] = self.time_input.text()

        session = self.session
        try:
            orm_user_add_info(session=session, data=self.user_data)
            print("New user: \n"
                  f"{self.user_data["user_name"]}\n"
                  f"{self.user_data["user_phone"]}\n"
                  f"{self.user_data["user_email"]}\n"
                  f"{self.user_data["user_service"]}\n"
                  f"{self.user_data["user_master"]}\n"
                  f"{self.user_data["user_appointment_data"]}\n"
                  f"{self.user_data["user_time"]}\n")

            user_info = (f"{self.user_data['user_name']}"
                         f" {self.user_data['user_phone']}"
                         f" {self.user_data["user_email"]}"
                         f" {self.user_data["user_service"]}"
                         f" {self.user_data["user_master"]}"
                         f" {self.user_data["user_appointment_data"]}"
                         f" {self.user_data["user_time"]}")

            self.show_success_message()

            self.user_list.clear()
            self.users = get_users_list(self.session)
            for user_info in self.users.split("\n"):
                item = QListWidgetItem(user_info)
                self.user_list.addItem(item)

            self.user_count.setText(count_list_items(self.session))

            self.name_input.clear()
            self.phone_input.clear()
            self.email_input.clear()
            self.service_input.clear()
            self.mster_input.clear()
            self.data_input.clear()
            self.time_input.clear()

        except Exception as e:
            self.show_failure_message(f"Some error: \n"
                                      f"{e}")
            print("Some error: ")
            print(e)

    def delete_user(self):
        selected_items = self.user_list.selectedItems()
        if not selected_items:
            return

        selected_user = selected_items[0].text()
        user_info = selected_user.split(",")
        user_name = user_info[0].split(":")[1].strip()
        user_phone = user_info[1].split(":")[1].strip()
        user_email = user_info[2].split(":")[1].strip()
        user_service = user_info[3].split(":")[1].strip()
        user_master = user_info[4].split(":")[1].strip()
        user_data = user_info[5].split(":")[1].strip()
        user_time = user_info[6].split(":")[1].strip()

        session = self.session
        try:
            orm_delete_user(session=session,
                            name=user_name,
                            phone=user_phone,
                            email=user_email,
                            service=user_service,
                            master=user_master,
                            data=user_data,
                            time=user_time)

            self.user_list.clear()
            self.users = get_users_list(self.session)

            for user_info in self.users.split("\n"):
                item = QListWidgetItem(user_info)
                self.user_list.addItem(item)
            self.user_count.setText(count_list_items(self.session))

            self.name_input.clear()
            self.phone_input.clear()
            self.email_input.clear()
            self.service_input.clear()
            self.mster_input.clear()
            self.data_input.clear()
            self.time_input.clear()

        except Exception as e:
            print("Error deleting user:")
            print(e)

    def search_user(self):
        search_name = self.name_input.text()
        search_phone = self.phone_input.text()

        if not search_name and not search_phone:
            QMessageBox.warning(self.centralwidget, 'Search Error', 'Введите имя пользователя и телефон')
            return

        for index in range(self.user_list.count()):
            item = self.user_list.item(index)
            user_info = item.text()
            if search_name in user_info or search_phone in user_info:
                self.found = True
                self.user_list.setCurrentItem(item)
                return

        if not self.found:
            QMessageBox.warning(self.centralwidget, 'Search Error', 'Введите корректные данные')
            return

    def retranslateUi(self, AddUserWindow):
        AddUserWindow.setWindowTitle(QCoreApplication.translate("AddUserWindow", u"MainWindow", None))
        self.name_label.setText(QCoreApplication.translate("AddUserWindow", u"\u0418\u043c\u044f", None))
        self.phone_label.setText(
            QCoreApplication.translate("AddUserWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.email_label.setText(QCoreApplication.translate("AddUserWindow", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.service_label.setText(
            QCoreApplication.translate("AddUserWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430", None))
        self.master_label.setText(
            QCoreApplication.translate("AddUserWindow", u"\u041c\u0430\u0441\u0442\u0435\u0440", None))
        self.data_label.setText(QCoreApplication.translate("AddUserWindow", u"\u0414\u0430\u0442\u0430", None))
        self.time_label.setText(QCoreApplication.translate("AddUserWindow", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.user_count_label.setText(
            QCoreApplication.translate("AddUserWindow", u"\u0412\u0441\u0435\u0433\u043e:", None))
        self.list_label.setText(
            QCoreApplication.translate("AddUserWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a:", None))
        self.add_button.setText(
            QCoreApplication.translate("AddUserWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_button.setText(
            QCoreApplication.translate("AddUserWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("AddUserWindow",
                                                           u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443",
                                                           None))
        self.search_user_button.setText(
            QCoreApplication.translate("AddUserWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi
