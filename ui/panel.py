# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IDAngrPanel(object):
    def setupUi(self, IDAngrPanel):
        IDAngrPanel.setObjectName("IDAngrPanel")
        IDAngrPanel.setEnabled(True)
        IDAngrPanel.resize(1547, 1042)
        IDAngrPanel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayout_6 = QtWidgets.QGridLayout(IDAngrPanel)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget = QtWidgets.QWidget(IDAngrPanel)
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QtCore.QSize(0, 61))
        self.widget.setObjectName("widget")
        self.resetBtn = QtWidgets.QPushButton(self.widget)
        self.resetBtn.setEnabled(True)
        self.resetBtn.setGeometry(QtCore.QRect(10, 10, 121, 45))
        self.resetBtn.setObjectName("resetBtn")
        self.runBtn = QtWidgets.QPushButton(self.widget)
        self.runBtn.setEnabled(False)
        self.runBtn.setGeometry(QtCore.QRect(140, 10, 121, 45))
        self.runBtn.setObjectName("runBtn")
        self.todbgBtn = QtWidgets.QPushButton(self.widget)
        self.todbgBtn.setEnabled(False)
        self.todbgBtn.setGeometry(QtCore.QRect(270, 10, 121, 45))
        self.todbgBtn.setObjectName("todbgBtn")
        self.gridLayout_6.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(IDAngrPanel)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.hexMemBox = QtWidgets.QCheckBox(IDAngrPanel)
        self.hexMemBox.setChecked(True)
        self.hexMemBox.setObjectName("hexMemBox")
        self.gridLayout.addWidget(self.hexMemBox, 0, 1, 1, 1)
        self.memoryView = QtWidgets.QTableView(IDAngrPanel)
        self.memoryView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.memoryView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.memoryView.setSortingEnabled(False)
        self.memoryView.setObjectName("memoryView")
        self.gridLayout.addWidget(self.memoryView, 1, 0, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.regsView = QtWidgets.QTableView(IDAngrPanel)
        self.regsView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.regsView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.regsView.setSortingEnabled(False)
        self.regsView.setObjectName("regsView")
        self.gridLayout_2.addWidget(self.regsView, 1, 0, 1, 2)
        self.registerChooser = QtWidgets.QComboBox(IDAngrPanel)
        self.registerChooser.setObjectName("registerChooser")
        self.gridLayout_2.addWidget(self.registerChooser, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(IDAngrPanel)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(IDAngrPanel)
        self.splitter_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.findView = QtWidgets.QListWidget(self.layoutWidget)
        self.findView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.findView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.findView.setObjectName("findView")
        self.gridLayout_3.addWidget(self.findView, 1, 0, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.avoidView = QtWidgets.QListWidget(self.layoutWidget_2)
        self.avoidView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.avoidView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.avoidView.setObjectName("avoidView")
        self.gridLayout_4.addWidget(self.avoidView, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.splitter_2, 2, 0, 1, 1)

        self.retranslateUi(IDAngrPanel)
        QtCore.QMetaObject.connectSlotsByName(IDAngrPanel)

    def retranslateUi(self, IDAngrPanel):
        _translate = QtCore.QCoreApplication.translate
        IDAngrPanel.setWindowTitle(_translate("IDAngrPanel", "IDAngr Panel"))
        self.resetBtn.setText(_translate("IDAngrPanel", "RESET"))
        self.runBtn.setText(_translate("IDAngrPanel", "RUN"))
        self.todbgBtn.setText(_translate("IDAngrPanel", "TO DBG"))
        self.label_2.setText(_translate("IDAngrPanel", "   Symbolic memory"))
        self.hexMemBox.setText(_translate("IDAngrPanel", "HEX"))
        self.label.setText(_translate("IDAngrPanel", "   Symbolic registers"))
        self.label_3.setText(_translate("IDAngrPanel", "   Find"))
        self.findView.setSortingEnabled(False)
        self.label_4.setText(_translate("IDAngrPanel", "   Avoid"))

