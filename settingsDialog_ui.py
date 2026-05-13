# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(301, 234)
        icon = QIcon(QIcon.fromTheme(u"applications-development"))
        Dialog.setWindowIcon(icon)
        self.saveSettingspushButton = QPushButton(Dialog)
        self.saveSettingspushButton.setObjectName(u"saveSettingspushButton")
        self.saveSettingspushButton.setGeometry(QRect(210, 200, 81, 23))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.saveSettingspushButton.setFont(font)
        self.saveSettingspushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.saveSettingspushButton.setStyleSheet(u"background-color: rgb(57, 136, 220);\n"
"color: rgb(255, 255, 255);")
        self.closePushButton = QPushButton(Dialog)
        self.closePushButton.setObjectName(u"closePushButton")
        self.closePushButton.setGeometry(QRect(120, 200, 75, 24))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 0, 246, 190))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ServerLabel = QLabel(self.widget)
        self.ServerLabel.setObjectName(u"ServerLabel")
        font1 = QFont()
        font1.setPointSize(10)
        self.ServerLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.ServerLabel)

        self.portLabel = QLabel(self.widget)
        self.portLabel.setObjectName(u"portLabel")
        self.portLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.portLabel)

        self.databaseLabel = QLabel(self.widget)
        self.databaseLabel.setObjectName(u"databaseLabel")
        self.databaseLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.databaseLabel)

        self.userLabel = QLabel(self.widget)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.userLabel)

        self.passwordLabel = QLabel(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.passwordLabel)

        self.departmentLabel = QLabel(self.widget)
        self.departmentLabel.setObjectName(u"departmentLabel")
        self.departmentLabel.setFont(font1)

        self.verticalLayout_2.addWidget(self.departmentLabel)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.serverLineEdit = QLineEdit(self.widget)
        self.serverLineEdit.setObjectName(u"serverLineEdit")
        font2 = QFont()
        font2.setPointSize(11)
        self.serverLineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.serverLineEdit)

        self.portLineEdit = QLineEdit(self.widget)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.portLineEdit)

        self.databaseLineEdit = QLineEdit(self.widget)
        self.databaseLineEdit.setObjectName(u"databaseLineEdit")
        self.databaseLineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.databaseLineEdit)

        self.userLineEdit = QLineEdit(self.widget)
        self.userLineEdit.setObjectName(u"userLineEdit")
        self.userLineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.userLineEdit)

        self.paswordLineEdit = QLineEdit(self.widget)
        self.paswordLineEdit.setObjectName(u"paswordLineEdit")
        self.paswordLineEdit.setFont(font2)
        self.paswordLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.paswordLineEdit)

        self.departmentLineEdit = QLineEdit(self.widget)
        self.departmentLineEdit.setObjectName(u"departmentLineEdit")
        self.departmentLineEdit.setFont(font2)
        self.departmentLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.verticalLayout.addWidget(self.departmentLineEdit)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.saveSettingspushButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Tallentaa asetukset tiedostoon</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.saveSettingspushButton.setText(QCoreApplication.translate("Dialog", u"Tallenna", None))
        self.closePushButton.setText(QCoreApplication.translate("Dialog", u"Sulje", None))
        self.ServerLabel.setText(QCoreApplication.translate("Dialog", u"Palvelin", None))
        self.portLabel.setText(QCoreApplication.translate("Dialog", u"Portti", None))
        self.databaseLabel.setText(QCoreApplication.translate("Dialog", u"Tietokanta", None))
        self.userLabel.setText(QCoreApplication.translate("Dialog", u"K\u00e4ytt\u00e4j\u00e4tunnus", None))
        self.passwordLabel.setText(QCoreApplication.translate("Dialog", u"Salasana", None))
        self.departmentLabel.setText(QCoreApplication.translate("Dialog", u"Osasto", None))
#if QT_CONFIG(tooltip)
        self.serverLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Palvelimen nimi tai IP-osoite</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.portLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Palvelimen porttinumero</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.databaseLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Tietokannan nimi</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.userLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Sovelluksen k\u00e4ytt\u00e4j\u00e4tunnus</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.paswordLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Salasana</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.departmentLineEdit.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">Salasana</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

