# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mplconfig.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(933, 299)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.config_tabWidget = QtWidgets.QTabWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.config_tabWidget.sizePolicy().hasHeightForWidth())
        self.config_tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        self.config_tabWidget.setFont(font)
        self.config_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.config_tabWidget.setObjectName("config_tabWidget")
        self.figure_tab = QtWidgets.QWidget()
        self.figure_tab.setObjectName("figure_tab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.figure_tab)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_13 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                    self.label_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.fig_title_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fig_title_lineEdit.sizePolicy().hasHeightForWidth())
        self.fig_title_lineEdit.setSizePolicy(sizePolicy)
        self.fig_title_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_title_lineEdit.setPlaceholderText("")
        self.fig_title_lineEdit.setObjectName("fig_title_lineEdit")
        self.horizontalLayout_12.addWidget(self.fig_title_lineEdit)
        self.title_font_btn = QtWidgets.QPushButton(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.title_font_btn.sizePolicy().hasHeightForWidth())
        self.title_font_btn.setSizePolicy(sizePolicy)
        self.title_font_btn.setAutoDefault(False)
        self.title_font_btn.setObjectName("title_font_btn")
        self.horizontalLayout_12.addWidget(self.title_font_btn)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_12)
        self.label_10 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                    self.label_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_18 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        self.fig_xlabel_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fig_xlabel_lineEdit.sizePolicy().hasHeightForWidth())
        self.fig_xlabel_lineEdit.setSizePolicy(sizePolicy)
        self.fig_xlabel_lineEdit.setText("")
        self.fig_xlabel_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_xlabel_lineEdit.setPlaceholderText("")
        self.fig_xlabel_lineEdit.setObjectName("fig_xlabel_lineEdit")
        self.horizontalLayout_3.addWidget(self.fig_xlabel_lineEdit)
        self.label_11 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.fig_ylabel_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fig_ylabel_lineEdit.sizePolicy().hasHeightForWidth())
        self.fig_ylabel_lineEdit.setSizePolicy(sizePolicy)
        self.fig_ylabel_lineEdit.setText("")
        self.fig_ylabel_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.fig_ylabel_lineEdit.setPlaceholderText("")
        self.fig_ylabel_lineEdit.setObjectName("fig_ylabel_lineEdit")
        self.horizontalLayout_3.addWidget(self.fig_ylabel_lineEdit)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_3)
        self.xy_label_font_btn = QtWidgets.QPushButton(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xy_label_font_btn.sizePolicy().hasHeightForWidth())
        self.xy_label_font_btn.setSizePolicy(sizePolicy)
        self.xy_label_font_btn.setAutoDefault(False)
        self.xy_label_font_btn.setObjectName("xy_label_font_btn")
        self.horizontalLayout_11.addWidget(self.xy_label_font_btn)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_11)
        self.label = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                    self.label)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.autoScale_chkbox = QtWidgets.QCheckBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.autoScale_chkbox.sizePolicy().hasHeightForWidth())
        self.autoScale_chkbox.setSizePolicy(sizePolicy)
        self.autoScale_chkbox.setChecked(True)
        self.autoScale_chkbox.setObjectName("autoScale_chkbox")
        self.horizontalLayout_13.addWidget(self.autoScale_chkbox)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xmin_lbl = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmin_lbl.sizePolicy().hasHeightForWidth())
        self.xmin_lbl.setSizePolicy(sizePolicy)
        self.xmin_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.xmin_lbl.setObjectName("xmin_lbl")
        self.horizontalLayout.addWidget(self.xmin_lbl)
        self.xmin_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmin_lineEdit.sizePolicy().hasHeightForWidth())
        self.xmin_lineEdit.setSizePolicy(sizePolicy)
        self.xmin_lineEdit.setObjectName("xmin_lineEdit")
        self.horizontalLayout.addWidget(self.xmin_lineEdit)
        self.xmax_lbl = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmax_lbl.sizePolicy().hasHeightForWidth())
        self.xmax_lbl.setSizePolicy(sizePolicy)
        self.xmax_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.xmax_lbl.setObjectName("xmax_lbl")
        self.horizontalLayout.addWidget(self.xmax_lbl)
        self.xmax_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xmax_lineEdit.sizePolicy().hasHeightForWidth())
        self.xmax_lineEdit.setSizePolicy(sizePolicy)
        self.xmax_lineEdit.setObjectName("xmax_lineEdit")
        self.horizontalLayout.addWidget(self.xmax_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ymin_lbl = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymin_lbl.sizePolicy().hasHeightForWidth())
        self.ymin_lbl.setSizePolicy(sizePolicy)
        self.ymin_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ymin_lbl.setObjectName("ymin_lbl")
        self.horizontalLayout_2.addWidget(self.ymin_lbl)
        self.ymin_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymin_lineEdit.sizePolicy().hasHeightForWidth())
        self.ymin_lineEdit.setSizePolicy(sizePolicy)
        self.ymin_lineEdit.setObjectName("ymin_lineEdit")
        self.horizontalLayout_2.addWidget(self.ymin_lineEdit)
        self.ymax_lbl = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymax_lbl.sizePolicy().hasHeightForWidth())
        self.ymax_lbl.setSizePolicy(sizePolicy)
        self.ymax_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ymax_lbl.setObjectName("ymax_lbl")
        self.horizontalLayout_2.addWidget(self.ymax_lbl)
        self.ymax_lineEdit = QtWidgets.QLineEdit(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ymax_lineEdit.sizePolicy().hasHeightForWidth())
        self.ymax_lineEdit.setSizePolicy(sizePolicy)
        self.ymax_lineEdit.setObjectName("ymax_lineEdit")
        self.horizontalLayout_2.addWidget(self.ymax_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_13)
        self.label_25 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                    self.label_25)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.legend_on_chkbox = QtWidgets.QCheckBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.legend_on_chkbox.sizePolicy().hasHeightForWidth())
        self.legend_on_chkbox.setSizePolicy(sizePolicy)
        self.legend_on_chkbox.setObjectName("legend_on_chkbox")
        self.horizontalLayout_14.addWidget(self.legend_on_chkbox)
        self.label_24 = QtWidgets.QLabel(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_14.addWidget(self.label_24)
        self.legend_loc_cbb = QtWidgets.QComboBox(self.figure_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.legend_loc_cbb.sizePolicy().hasHeightForWidth())
        self.legend_loc_cbb.setSizePolicy(sizePolicy)
        self.legend_loc_cbb.setObjectName("legend_loc_cbb")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.legend_loc_cbb.addItem("")
        self.horizontalLayout_14.addWidget(self.legend_loc_cbb)
        self.formLayout_2.setLayout(3, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_14)
        self.label_10.raise_()
        self.label.raise_()
        self.label_13.raise_()
        self.label_25.raise_()
        self.config_tabWidget.addTab(self.figure_tab, "")
        self.curve_tab = QtWidgets.QWidget()
        self.curve_tab.setObjectName("curve_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.curve_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.line_label_lineEdit = QtWidgets.QLineEdit(self.curve_tab)
        self.line_label_lineEdit.setObjectName("line_label_lineEdit")
        self.gridLayout.addWidget(self.line_label_lineEdit, 3, 1, 1, 10)
        self.label_2 = QtWidgets.QLabel(self.curve_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.curve_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.curve_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.line_width_lineEdit = QtWidgets.QLineEdit(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.line_width_lineEdit.setSizePolicy(sizePolicy)
        self.line_width_lineEdit.setObjectName("line_width_lineEdit")
        self.gridLayout.addWidget(self.line_width_lineEdit, 1, 10, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.line_style_cbb = QtWidgets.QComboBox(self.curve_tab)
        self.line_style_cbb.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.line_style_cbb.setObjectName("line_style_cbb")
        self.line_style_cbb.addItem("")
        self.line_style_cbb.addItem("")
        self.line_style_cbb.addItem("")
        self.line_style_cbb.addItem("")
        self.line_style_cbb.addItem("")
        self.gridLayout.addWidget(self.line_style_cbb, 1, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)
        self.line_color_btn = QtWidgets.QPushButton(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_color_btn.sizePolicy().hasHeightForWidth())
        self.line_color_btn.setSizePolicy(sizePolicy)
        self.line_color_btn.setStyleSheet(" QPushButton {\n"
                                          "    margin: 1px;\n"
                                          "    border-color: rgb(0, 85, 0);\n"
                                          "    border-style: outset;\n"
                                          "    border-radius: 3px;\n"
                                          "    border-width: 1px;\n"
                                          "    color: black;\n"
                                          "    background-color: gray;\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: white;\n"
                                          "}")
        self.line_color_btn.setText("")
        self.line_color_btn.setAutoDefault(False)
        self.line_color_btn.setObjectName("line_color_btn")
        self.gridLayout.addWidget(self.line_color_btn, 1, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 1, 1, 1)
        self.mk_style_cbb = QtWidgets.QComboBox(self.curve_tab)
        self.mk_style_cbb.setObjectName("mk_style_cbb")
        self.gridLayout.addWidget(self.mk_style_cbb, 2, 2, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 2, 4, 1, 1)
        self.mk_edgecolor_btn = QtWidgets.QPushButton(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mk_edgecolor_btn.sizePolicy().hasHeightForWidth())
        self.mk_edgecolor_btn.setSizePolicy(sizePolicy)
        self.mk_edgecolor_btn.setStyleSheet(
            " QPushButton {\n"
            "    margin: 1px;\n"
            "    border-color: rgb(0, 85, 0);\n"
            "    border-style: outset;\n"
            "    border-radius: 3px;\n"
            "    border-width: 1px;\n"
            "    color: black;\n"
            "    background-color: gray;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: white;\n"
            "}")
        self.mk_edgecolor_btn.setText("")
        self.mk_edgecolor_btn.setAutoDefault(False)
        self.mk_edgecolor_btn.setObjectName("mk_edgecolor_btn")
        self.gridLayout.addWidget(self.mk_edgecolor_btn, 2, 5, 1, 1)
        self.mk_facecolor_btn = QtWidgets.QPushButton(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mk_facecolor_btn.sizePolicy().hasHeightForWidth())
        self.mk_facecolor_btn.setSizePolicy(sizePolicy)
        self.mk_facecolor_btn.setStyleSheet(
            " QPushButton {\n"
            "    margin: 1px;\n"
            "    border-color: rgb(0, 85, 0);\n"
            "    border-style: outset;\n"
            "    border-radius: 3px;\n"
            "    border-width: 1px;\n"
            "    color: black;\n"
            "    background-color: gray;\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: white;\n"
            "}")
        self.mk_facecolor_btn.setText("")
        self.mk_facecolor_btn.setAutoDefault(False)
        self.mk_facecolor_btn.setObjectName("mk_facecolor_btn")
        self.gridLayout.addWidget(self.mk_facecolor_btn, 2, 6, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 7, 1, 1)
        self.mk_size_lineEdit = QtWidgets.QLineEdit(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mk_size_lineEdit.sizePolicy().hasHeightForWidth())
        self.mk_size_lineEdit.setSizePolicy(sizePolicy)
        self.mk_size_lineEdit.setObjectName("mk_size_lineEdit")
        self.gridLayout.addWidget(self.mk_size_lineEdit, 2, 8, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 2, 9, 1, 1)
        self.mk_width_lineEdit = QtWidgets.QLineEdit(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mk_width_lineEdit.sizePolicy().hasHeightForWidth())
        self.mk_width_lineEdit.setSizePolicy(sizePolicy)
        self.mk_width_lineEdit.setObjectName("mk_width_lineEdit")
        self.gridLayout.addWidget(self.mk_width_lineEdit, 2, 10, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.curve_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 9, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.line_id_cbb = QtWidgets.QComboBox(self.curve_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line_id_cbb.sizePolicy().hasHeightForWidth())
        self.line_id_cbb.setSizePolicy(sizePolicy)
        self.line_id_cbb.setObjectName("line_id_cbb")
        self.gridLayout.addWidget(self.line_id_cbb, 0, 1, 1, 3)
        self.line_hide_chkbox = QtWidgets.QCheckBox(self.curve_tab)
        self.line_hide_chkbox.setObjectName("line_hide_chkbox")
        self.gridLayout.addWidget(self.line_hide_chkbox, 0, 8, 1, 1)
        self.config_tabWidget.addTab(self.curve_tab, "")
        self.style_tab = QtWidgets.QWidget()
        self.style_tab.setObjectName("style_tab")
        self.formLayout_3 = QtWidgets.QFormLayout(self.style_tab)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_16 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                    self.label_16)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.style_tab)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.figWidth_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figWidth_lineEdit.sizePolicy().hasHeightForWidth())
        self.figWidth_lineEdit.setSizePolicy(sizePolicy)
        self.figWidth_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.figWidth_lineEdit.setObjectName("figWidth_lineEdit")
        self.horizontalLayout_5.addWidget(self.figWidth_lineEdit)
        self.label_14 = QtWidgets.QLabel(self.style_tab)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.figHeight_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figHeight_lineEdit.sizePolicy().hasHeightForWidth())
        self.figHeight_lineEdit.setSizePolicy(sizePolicy)
        self.figHeight_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.figHeight_lineEdit.setObjectName("figHeight_lineEdit")
        self.horizontalLayout_5.addWidget(self.figHeight_lineEdit)
        self.label_15 = QtWidgets.QLabel(self.style_tab)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.figDpi_lineEdit = QtWidgets.QLineEdit(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.figDpi_lineEdit.sizePolicy().hasHeightForWidth())
        self.figDpi_lineEdit.setSizePolicy(sizePolicy)
        self.figDpi_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.figDpi_lineEdit.setObjectName("figDpi_lineEdit")
        self.horizontalLayout_5.addWidget(self.figDpi_lineEdit)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_5)
        self.label_17 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                    self.label_17)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bkgd_color_label = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bkgd_color_label.sizePolicy().hasHeightForWidth())
        self.bkgd_color_label.setSizePolicy(sizePolicy)
        self.bkgd_color_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bkgd_color_label.setObjectName("bkgd_color_label")
        self.horizontalLayout_6.addWidget(self.bkgd_color_label)
        self.bkgd_color_btn = QtWidgets.QPushButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bkgd_color_btn.sizePolicy().hasHeightForWidth())
        self.bkgd_color_btn.setSizePolicy(sizePolicy)
        self.bkgd_color_btn.setAutoDefault(False)
        self.bkgd_color_btn.setObjectName("bkgd_color_btn")
        self.horizontalLayout_6.addWidget(self.bkgd_color_btn)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_6)
        self.label_7 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                  | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                    self.label_7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.mticks_chkbox = QtWidgets.QCheckBox(self.style_tab)
        self.mticks_chkbox.setObjectName("mticks_chkbox")
        self.horizontalLayout_7.addWidget(self.mticks_chkbox)
        self.xy_ticks_sample_lbl = QtWidgets.QLabel(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xy_ticks_sample_lbl.sizePolicy().hasHeightForWidth())
        self.xy_ticks_sample_lbl.setSizePolicy(sizePolicy)
        self.xy_ticks_sample_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.xy_ticks_sample_lbl.setObjectName("xy_ticks_sample_lbl")
        self.horizontalLayout_7.addWidget(self.xy_ticks_sample_lbl)
        self.xy_ticks_font_btn = QtWidgets.QPushButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.xy_ticks_font_btn.sizePolicy().hasHeightForWidth())
        self.xy_ticks_font_btn.setSizePolicy(sizePolicy)
        self.xy_ticks_font_btn.setAutoDefault(False)
        self.xy_ticks_font_btn.setObjectName("xy_ticks_font_btn")
        self.horizontalLayout_7.addWidget(self.xy_ticks_font_btn)
        self.ticks_color_label = QtWidgets.QLabel(self.style_tab)
        self.ticks_color_label.setObjectName("ticks_color_label")
        self.horizontalLayout_7.addWidget(self.ticks_color_label)
        self.ticks_color_btn = QtWidgets.QPushButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ticks_color_btn.sizePolicy().hasHeightForWidth())
        self.ticks_color_btn.setSizePolicy(sizePolicy)
        self.ticks_color_btn.setAutoDefault(False)
        self.ticks_color_btn.setObjectName("ticks_color_btn")
        self.horizontalLayout_7.addWidget(self.ticks_color_btn)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_7)
        self.label_6 = QtWidgets.QLabel(self.style_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                    self.label_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tightLayout_chkbox = QtWidgets.QCheckBox(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tightLayout_chkbox.sizePolicy().hasHeightForWidth())
        self.tightLayout_chkbox.setSizePolicy(sizePolicy)
        self.tightLayout_chkbox.setObjectName("tightLayout_chkbox")
        self.horizontalLayout_8.addWidget(self.tightLayout_chkbox)
        self.gridon_chkbox = QtWidgets.QCheckBox(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gridon_chkbox.sizePolicy().hasHeightForWidth())
        self.gridon_chkbox.setSizePolicy(sizePolicy)
        self.gridon_chkbox.setObjectName("gridon_chkbox")
        self.horizontalLayout_8.addWidget(self.gridon_chkbox)
        self.grid_color_btn = QtWidgets.QPushButton(self.style_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.grid_color_btn.sizePolicy().hasHeightForWidth())
        self.grid_color_btn.setSizePolicy(sizePolicy)
        self.grid_color_btn.setStyleSheet(" QPushButton {\n"
                                          "    margin: 1px;\n"
                                          "    border-color: rgb(0, 85, 0);\n"
                                          "    border-style: outset;\n"
                                          "    border-radius: 3px;\n"
                                          "    border-width: 1px;\n"
                                          "    color: black;\n"
                                          "    background-color: gray;\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: white;\n"
                                          "}")
        self.grid_color_btn.setText("")
        self.grid_color_btn.setAutoDefault(False)
        self.grid_color_btn.setObjectName("grid_color_btn")
        self.horizontalLayout_8.addWidget(self.grid_color_btn)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.FieldRole,
                                    self.horizontalLayout_8)
        self.config_tabWidget.addTab(self.style_tab, "")
        self.horizontalLayout_4.addWidget(self.config_tabWidget)

        self.retranslateUi(Dialog)
        self.config_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_13.setText(_translate("Dialog", "Title"))
        self.title_font_btn.setText(_translate("Dialog", "Font"))
        self.label_10.setText(_translate("Dialog", "Labels"))
        self.label_18.setText(_translate("Dialog", "X-Label"))
        self.label_11.setText(_translate("Dialog", "Y-Label"))
        self.xy_label_font_btn.setText(_translate("Dialog", "Font"))
        self.label.setText(_translate("Dialog", "XY Range"))
        self.autoScale_chkbox.setText(_translate("Dialog", "Auto Scale"))
        self.xmin_lbl.setText(_translate("Dialog", "xmin"))
        self.xmax_lbl.setText(_translate("Dialog", "xmax"))
        self.ymin_lbl.setText(_translate("Dialog", "ymin"))
        self.ymax_lbl.setText(_translate("Dialog", "ymax"))
        self.label_25.setText(_translate("Dialog", "Legend"))
        self.legend_on_chkbox.setToolTip(
            _translate("Dialog", "Check to show legend"))
        self.legend_on_chkbox.setText(_translate("Dialog", "Show"))
        self.label_24.setText(_translate("Dialog", "Location"))
        self.legend_loc_cbb.setToolTip(
            _translate("Dialog", "Select location for legend"))
        self.legend_loc_cbb.setItemText(0, _translate("Dialog", "Auto"))
        self.legend_loc_cbb.setItemText(1, _translate("Dialog", "Upper Right"))
        self.legend_loc_cbb.setItemText(2, _translate("Dialog", "Upper Left"))
        self.legend_loc_cbb.setItemText(3, _translate("Dialog", "Lower Left"))
        self.legend_loc_cbb.setItemText(4, _translate("Dialog", "Lower Right"))
        self.legend_loc_cbb.setItemText(5, _translate("Dialog", "Right"))
        self.legend_loc_cbb.setItemText(6, _translate("Dialog", "Center Left"))
        self.legend_loc_cbb.setItemText(7, _translate("Dialog",
                                                      "Center Right"))
        self.legend_loc_cbb.setItemText(8, _translate("Dialog",
                                                      "Lower Center"))
        self.legend_loc_cbb.setItemText(9, _translate("Dialog",
                                                      "Upper Center"))
        self.legend_loc_cbb.setItemText(10, _translate("Dialog", "Center"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.figure_tab),
            _translate("Dialog", "Figure"))
        self.label_2.setText(_translate("Dialog", "Line ID"))
        self.label_4.setText(_translate("Dialog", "Marker"))
        self.label_3.setText(_translate("Dialog", "Line"))
        self.label_8.setText(_translate("Dialog", "Style"))
        self.line_style_cbb.setItemText(0, _translate("Dialog", "solid"))
        self.line_style_cbb.setItemText(1, _translate("Dialog", "dashed"))
        self.line_style_cbb.setItemText(2, _translate("Dialog", "dashdot"))
        self.line_style_cbb.setItemText(3, _translate("Dialog", "dotted"))
        self.line_style_cbb.setItemText(4, _translate("Dialog", "None"))
        self.label_5.setText(_translate("Dialog", "Color"))
        self.label_19.setText(_translate("Dialog", "Style"))
        self.label_21.setText(_translate("Dialog", "Color"))
        self.mk_edgecolor_btn.setToolTip(_translate("Dialog", "Edge Color"))
        self.mk_facecolor_btn.setToolTip(_translate("Dialog", "Face Color"))
        self.label_20.setText(_translate("Dialog", "Size"))
        self.label_22.setText(_translate("Dialog", "Width"))
        self.label_23.setText(_translate("Dialog", "Label"))
        self.label_9.setText(_translate("Dialog", "Width"))
        self.line_id_cbb.setToolTip(
            _translate("Dialog", "Select line to configure"))
        self.line_hide_chkbox.setText(_translate("Dialog", "Hide"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.curve_tab),
            _translate("Dialog", "Curve"))
        self.label_16.setText(_translate("Dialog", "Figure Size"))
        self.label_12.setText(_translate("Dialog", "Width"))
        self.figWidth_lineEdit.setText(_translate("Dialog", "4"))
        self.figWidth_lineEdit.setPlaceholderText(_translate("Dialog", "4"))
        self.label_14.setText(_translate("Dialog", "Height"))
        self.figHeight_lineEdit.setText(_translate("Dialog", "3"))
        self.figHeight_lineEdit.setPlaceholderText(_translate("Dialog", "3"))
        self.label_15.setText(_translate("Dialog", "DPI"))
        self.figDpi_lineEdit.setText(_translate("Dialog", "120"))
        self.figDpi_lineEdit.setPlaceholderText(_translate("Dialog", "120"))
        self.label_17.setText(_translate("Dialog", "Background Color"))
        self.bkgd_color_label.setText(_translate("Dialog", "#FFFFFF"))
        self.bkgd_color_btn.setText(_translate("Dialog", "Pick Color"))
        self.label_7.setText(_translate("Dialog", "Ticks"))
        self.mticks_chkbox.setText(_translate("Dialog", "Minor On"))
        self.xy_ticks_sample_lbl.setText(_translate("Dialog", "Sample"))
        self.xy_ticks_font_btn.setText(_translate("Dialog", "Choose Font"))
        self.ticks_color_label.setText(_translate("Dialog", "#FFFFFF"))
        self.ticks_color_btn.setText(_translate("Dialog", "Pick Color"))
        self.label_6.setText(_translate("Dialog", "Layout"))
        self.tightLayout_chkbox.setText(_translate("Dialog", "Tight"))
        self.gridon_chkbox.setText(_translate("Dialog", "Grid On"))
        self.config_tabWidget.setTabText(
            self.config_tabWidget.indexOf(self.style_tab),
            _translate("Dialog", "Style"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
