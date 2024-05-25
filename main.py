import logging
import unittest

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QApplication

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.database import Base

from ui.pyui.MainWindow import Ui_MainWindow

from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    engine = create_engine('sqlite:///users.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    app = QApplication([])

    MainWindow = QMainWindow()
    ui_main = Ui_MainWindow(Session())
    ui_main.setupUi(MainWindow)
    MainWindow.show()

    app.exec()
