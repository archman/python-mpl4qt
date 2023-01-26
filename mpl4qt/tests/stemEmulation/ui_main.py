# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(985, 917)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.matplotliberrorbarWidget = MatplotlibErrorbarWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(
            self.matplotliberrorbarWidget.sizePolicy().hasHeightForWidth())
        self.matplotliberrorbarWidget.setSizePolicy(sizePolicy)
        self.matplotliberrorbarWidget.setFigureAutoScale(False)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matplotliberrorbarWidget.setFigureXYlabelFont(font)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matplotliberrorbarWidget.setFigureTitleFont(font)
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.matplotliberrorbarWidget.setFigureXYticksFont(font)
        self.matplotliberrorbarWidget.setProperty("figureMarkerSize", 10.0)
        self.matplotliberrorbarWidget.setProperty("figureLineVisible", True)
        self.matplotliberrorbarWidget.setProperty("figureEbLineWidth", 2.0)
        self.matplotliberrorbarWidget.setProperty("figureEbMarkerSize", 5.0)
        self.matplotliberrorbarWidget.setProperty("figureEbMarkerThickness",
                                                  2.0)
        self.matplotliberrorbarWidget.setObjectName("matplotliberrorbarWidget")
        self.verticalLayout.addWidget(self.matplotliberrorbarWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_id_cbb = QtWidgets.QComboBox(Form)
        self.line_id_cbb.setObjectName("line_id_cbb")
        self.horizontalLayout.addWidget(self.line_id_cbb)
        self.update_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.update_btn.sizePolicy().hasHeightForWidth())
        self.update_btn.setSizePolicy(sizePolicy)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout.addWidget(self.update_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_curve_btn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.add_curve_btn.sizePolicy().hasHeightForWidth())
        self.add_curve_btn.setSizePolicy(sizePolicy)
        self.add_curve_btn.setObjectName("add_curve_btn")
        self.horizontalLayout.addWidget(self.add_curve_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(
            _translate(
                "Form",
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Cantarell\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- This is an exmple of how to use <span style=\" font-style:italic;\">MatplotlibErrorbarWidget</span> to emulate the stem plot.</p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Press the button \'<span style=\" font-weight:600;\">Add</span>\' to add a new curve on the panel.</p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Press the button \'<span style=\" font-weight:600;\">Update</span>\' to update the selected curve.</p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Select the curve by ID by the left most combobox.</p></body></html>"
            ))
        self.matplotliberrorbarWidget.setFigureTitle(
            _translate("Form", "Stem plot with MatplotlibErrorbarWidget"))
        self.matplotliberrorbarWidget.setProperty("figureLineStyle",
                                                  _translate("Form", "None"))
        self.matplotliberrorbarWidget.setProperty("figureMarkerStyle",
                                                  _translate("Form", "o"))
        self.update_btn.setText(_translate("Form", "Update"))
        self.add_curve_btn.setText(_translate("Form", "Add"))


from mpl4qt.widgets.mplerrorbarwidget import MatplotlibErrorbarWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
