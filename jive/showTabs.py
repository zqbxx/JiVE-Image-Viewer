# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jive/tabs.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(370, 430, 251, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabs = QtWidgets.QTabWidget(Dialog)
        self.tabs.setEnabled(True)
        self.tabs.setGeometry(QtCore.QRect(20, 20, 601, 391))
        self.tabs.setObjectName("tabs")
        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setObjectName("tab_0")
        self.frame = QtWidgets.QFrame(self.tab_0)
        self.frame.setGeometry(QtCore.QRect(10, 10, 581, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.urlLineEdit = QtWidgets.QLineEdit(self.frame)
        self.urlLineEdit.setGeometry(QtCore.QRect(20, 20, 541, 30))
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.extractButton = QtWidgets.QPushButton(self.frame)
        self.extractButton.setGeometry(QtCore.QRect(20, 190, 81, 30))
        self.extractButton.setObjectName("extractButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 70, 71, 18))
        self.label.setObjectName("label")
        self.distanceSpinBox = QtWidgets.QSpinBox(self.frame)
        self.distanceSpinBox.setGeometry(QtCore.QRect(104, 64, 52, 28))
        self.distanceSpinBox.setProperty("value", 10)
        self.distanceSpinBox.setObjectName("distanceSpinBox")
        self.getLinksCheckBox = QtWidgets.QCheckBox(self.frame)
        self.getLinksCheckBox.setGeometry(QtCore.QRect(20, 110, 141, 23))
        self.getLinksCheckBox.setChecked(True)
        self.getLinksCheckBox.setObjectName("getLinksCheckBox")
        self.getImagesCheckBox = QtWidgets.QCheckBox(self.frame)
        self.getImagesCheckBox.setGeometry(QtCore.QRect(20, 140, 141, 23))
        self.getImagesCheckBox.setChecked(True)
        self.getImagesCheckBox.setObjectName("getImagesCheckBox")
        self.clearButton = QtWidgets.QPushButton(self.frame)
        self.clearButton.setGeometry(QtCore.QRect(500, 60, 61, 30))
        self.clearButton.setObjectName("clearButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 237, 74, 18))
        self.label_2.setObjectName("label_2")
        self.miniLogTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.miniLogTextEdit.setGeometry(QtCore.QRect(20, 260, 541, 71))
        self.miniLogTextEdit.setReadOnly(True)
        self.miniLogTextEdit.setObjectName("miniLogTextEdit")
        self.clearButton_2 = QtWidgets.QPushButton(self.frame)
        self.clearButton_2.setGeometry(QtCore.QRect(500, 220, 61, 30))
        self.clearButton_2.setObjectName("clearButton_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(478, 53, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(477, 213, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabs.addTab(self.tab_0, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 581, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab1TextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.tab1TextEdit.setReadOnly(False)
        self.tab1TextEdit.setObjectName("tab1TextEdit")
        self.verticalLayout.addWidget(self.tab1TextEdit)
        self.tab1Label = QtWidgets.QLabel(self.tab_1)
        self.tab1Label.setGeometry(QtCore.QRect(10, 10, 321, 18))
        self.tab1Label.setObjectName("tab1Label")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(11, 330, 301, 18))
        self.label_5.setObjectName("label_5")
        self.tab1CountLabel = QtWidgets.QLabel(self.tab_1)
        self.tab1CountLabel.setGeometry(QtCore.QRect(510, 10, 74, 18))
        self.tab1CountLabel.setObjectName("tab1CountLabel")
        self.tab1CopyButton = QtWidgets.QPushButton(self.tab_1)
        self.tab1CopyButton.setGeometry(QtCore.QRect(530, 325, 61, 30))
        self.tab1CopyButton.setObjectName("tab1CopyButton")
        self.tabs.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 581, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tab2TextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.tab2TextEdit.setReadOnly(False)
        self.tab2TextEdit.setObjectName("tab2TextEdit")
        self.verticalLayout_2.addWidget(self.tab2TextEdit)
        self.tab2Label = QtWidgets.QLabel(self.tab_2)
        self.tab2Label.setGeometry(QtCore.QRect(10, 10, 331, 18))
        self.tab2Label.setObjectName("tab2Label")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(11, 330, 301, 18))
        self.label_6.setObjectName("label_6")
        self.tab2CountLabel = QtWidgets.QLabel(self.tab_2)
        self.tab2CountLabel.setGeometry(QtCore.QRect(510, 10, 74, 18))
        self.tab2CountLabel.setObjectName("tab2CountLabel")
        self.tab2CopyButton = QtWidgets.QPushButton(self.tab_2)
        self.tab2CopyButton.setGeometry(QtCore.QRect(530, 325, 61, 30))
        self.tab2CopyButton.setObjectName("tab2CopyButton")
        self.tabs.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 40, 581, 281))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tab3TextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        self.tab3TextEdit.setReadOnly(False)
        self.tab3TextEdit.setObjectName("tab3TextEdit")
        self.verticalLayout_3.addWidget(self.tab3TextEdit)
        self.tab3Label = QtWidgets.QLabel(self.tab_3)
        self.tab3Label.setGeometry(QtCore.QRect(10, 10, 311, 18))
        self.tab3Label.setObjectName("tab3Label")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(11, 330, 311, 18))
        self.label_7.setObjectName("label_7")
        self.tab3CountLabel = QtWidgets.QLabel(self.tab_3)
        self.tab3CountLabel.setGeometry(QtCore.QRect(510, 10, 74, 18))
        self.tab3CountLabel.setObjectName("tab3CountLabel")
        self.tab3CopyButton = QtWidgets.QPushButton(self.tab_3)
        self.tab3CopyButton.setGeometry(QtCore.QRect(530, 325, 61, 30))
        self.tab3CopyButton.setObjectName("tab3CopyButton")
        self.tabs.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 40, 581, 281))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tab4TextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_4)
        self.tab4TextEdit.setReadOnly(False)
        self.tab4TextEdit.setObjectName("tab4TextEdit")
        self.verticalLayout_4.addWidget(self.tab4TextEdit)
        self.tab4Label = QtWidgets.QLabel(self.tab_4)
        self.tab4Label.setGeometry(QtCore.QRect(10, 10, 331, 18))
        self.tab4Label.setObjectName("tab4Label")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(11, 330, 291, 18))
        self.label_8.setObjectName("label_8")
        self.tab4CountLabel = QtWidgets.QLabel(self.tab_4)
        self.tab4CountLabel.setGeometry(QtCore.QRect(510, 10, 74, 18))
        self.tab4CountLabel.setObjectName("tab4CountLabel")
        self.tab4CopyButton = QtWidgets.QPushButton(self.tab_4)
        self.tab4CopyButton.setGeometry(QtCore.QRect(530, 325, 61, 30))
        self.tab4CopyButton.setObjectName("tab4CopyButton")
        self.tabs.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)
        self.tabs.setCurrentIndex(4)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.clearButton_2.clicked.connect(self.miniLogTextEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.urlLineEdit, self.distanceSpinBox)
        Dialog.setTabOrder(self.distanceSpinBox, self.getLinksCheckBox)
        Dialog.setTabOrder(self.getLinksCheckBox, self.getImagesCheckBox)
        Dialog.setTabOrder(self.getImagesCheckBox, self.extractButton)
        Dialog.setTabOrder(self.extractButton, self.clearButton)
        Dialog.setTabOrder(self.clearButton, self.tabs)
        Dialog.setTabOrder(self.tabs, self.tab2TextEdit)
        Dialog.setTabOrder(self.tab2TextEdit, self.tab3TextEdit)
        Dialog.setTabOrder(self.tab3TextEdit, self.tab4TextEdit)
        Dialog.setTabOrder(self.tab4TextEdit, self.tab1TextEdit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Extract images from a webpage"))
        self.urlLineEdit.setPlaceholderText(_translate("Dialog", "URL of the webpage"))
        self.extractButton.setText(_translate("Dialog", "Extract"))
        self.label.setText(_translate("Dialog", "Distance:"))
        self.getLinksCheckBox.setText(_translate("Dialog", "get links"))
        self.getImagesCheckBox.setText(_translate("Dialog", "get images"))
        self.clearButton.setText(_translate("Dialog", "Clear"))
        self.label_2.setText(_translate("Dialog", "Mini log:"))
        self.clearButton_2.setText(_translate("Dialog", "Clear"))
        self.label_3.setText(_translate("Dialog", "└"))
        self.label_4.setText(_translate("Dialog", "┌"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_0), _translate("Dialog", "Tab 0"))
        self.tab1TextEdit.setPlaceholderText(_translate("Dialog", "empty"))
        self.tab1Label.setText(_translate("Dialog", "Elements were found in this order:"))
        self.label_5.setText(_translate("Dialog", "Press OK to open these images"))
        self.tab1CountLabel.setText(_translate("Dialog", "Count: 0"))
        self.tab1CopyButton.setText(_translate("Dialog", "Copy"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_1), _translate("Dialog", "Tab 1"))
        self.tab2TextEdit.setPlaceholderText(_translate("Dialog", "empty"))
        self.tab2Label.setText(_translate("Dialog", "Sorting: OFF; this is the largest cluster:"))
        self.label_6.setText(_translate("Dialog", "Press OK to open these images"))
        self.tab2CountLabel.setText(_translate("Dialog", "Count: 0"))
        self.tab2CopyButton.setText(_translate("Dialog", "Copy"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
        self.tab3TextEdit.setPlaceholderText(_translate("Dialog", "empty"))
        self.tab3Label.setText(_translate("Dialog", "Sorting: ON; no clustering:"))
        self.label_7.setText(_translate("Dialog", "Press OK to open these images"))
        self.tab3CountLabel.setText(_translate("Dialog", "Count: 0"))
        self.tab3CopyButton.setText(_translate("Dialog", "Copy"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), _translate("Dialog", "Tab 3"))
        self.tab4TextEdit.setPlaceholderText(_translate("Dialog", "empty"))
        self.tab4Label.setText(_translate("Dialog", "Sorting: ON; this is the largest cluster:"))
        self.label_8.setText(_translate("Dialog", "Press OK to open these images"))
        self.tab4CountLabel.setText(_translate("Dialog", "Count: 0"))
        self.tab4CopyButton.setText(_translate("Dialog", "Copy"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_4), _translate("Dialog", "Tab 4"))

