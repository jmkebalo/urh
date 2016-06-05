# -*- coding: utf-8 -*-

#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FAnalysis(object):
    def setupUi(self, FAnalysis):
        FAnalysis.setObjectName("FAnalysis")
        FAnalysis.resize(1053, 746)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FAnalysis.sizePolicy().hasHeightForWidth())
        FAnalysis.setSizePolicy(sizePolicy)
        FAnalysis.setMinimumSize(QtCore.QSize(0, 0))
        FAnalysis.setFocusPolicy(QtCore.Qt.ClickFocus)
        FAnalysis.setAcceptDrops(True)
        FAnalysis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        FAnalysis.setFrameShadow(QtWidgets.QFrame.Raised)
        FAnalysis.setLineWidth(1)
        FAnalysis.setMidLineWidth(0)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(FAnalysis)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter = QtWidgets.QSplitter(FAnalysis)
        self.splitter.setStyleSheet("QSplitter::handle {\n"
"    background-color: #AAAAAA;\n"
"}")
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(2)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lSignalNr = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSignalNr.sizePolicy().hasHeightForWidth())
        self.lSignalNr.setSizePolicy(sizePolicy)
        self.lSignalNr.setObjectName("lSignalNr")
        self.horizontalLayout_2.addWidget(self.lSignalNr)
        self.lSignalName = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSignalName.sizePolicy().hasHeightForWidth())
        self.lSignalName.setSizePolicy(sizePolicy)
        self.lSignalName.setMinimumSize(QtCore.QSize(0, 0))
        self.lSignalName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lSignalName.setAcceptDrops(False)
        self.lSignalName.setObjectName("lSignalName")
        self.horizontalLayout_2.addWidget(self.lSignalName)
        self.btnSaveProto = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveProto.sizePolicy().hasHeightForWidth())
        self.btnSaveProto.setSizePolicy(sizePolicy)
        self.btnSaveProto.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnSaveProto.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.btnSaveProto.setIcon(icon)
        self.btnSaveProto.setObjectName("btnSaveProto")
        self.horizontalLayout_2.addWidget(self.btnSaveProto)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.treeViewProtocols = ProtocolTreeView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeViewProtocols.sizePolicy().hasHeightForWidth())
        self.treeViewProtocols.setSizePolicy(sizePolicy)
        self.treeViewProtocols.setAcceptDrops(True)
        self.treeViewProtocols.setDragEnabled(True)
        self.treeViewProtocols.setDragDropOverwriteMode(False)
        self.treeViewProtocols.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.treeViewProtocols.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.treeViewProtocols.setObjectName("treeViewProtocols")
        self.treeViewProtocols.header().setVisible(False)
        self.verticalLayout_4.addWidget(self.treeViewProtocols)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbProtoView = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbProtoView.sizePolicy().hasHeightForWidth())
        self.cbProtoView.setSizePolicy(sizePolicy)
        self.cbProtoView.setObjectName("cbProtoView")
        self.cbProtoView.addItem("")
        self.cbProtoView.addItem("")
        self.cbProtoView.addItem("")
        self.gridLayout_2.addWidget(self.cbProtoView, 0, 0, 1, 3)
        self.cbDecoding = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDecoding.sizePolicy().hasHeightForWidth())
        self.cbDecoding.setSizePolicy(sizePolicy)
        self.cbDecoding.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cbDecoding.setObjectName("cbDecoding")
        self.cbDecoding.addItem("")
        self.cbDecoding.addItem("")
        self.cbDecoding.addItem("")
        self.cbDecoding.addItem("")
        self.cbDecoding.addItem("")
        self.gridLayout_2.addWidget(self.cbDecoding, 1, 0, 1, 3)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.lEncodingErrors = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lEncodingErrors.sizePolicy().hasHeightForWidth())
        self.lEncodingErrors.setSizePolicy(sizePolicy)
        self.lEncodingErrors.setObjectName("lEncodingErrors")
        self.verticalLayout_4.addWidget(self.lEncodingErrors)
        self.lDecodingErrorsValue = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lDecodingErrorsValue.sizePolicy().hasHeightForWidth())
        self.lDecodingErrorsValue.setSizePolicy(sizePolicy)
        self.lDecodingErrorsValue.setObjectName("lDecodingErrorsValue")
        self.verticalLayout_4.addWidget(self.lDecodingErrorsValue)
        self.btnAnalyze = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAnalyze.setObjectName("btnAnalyze")
        self.verticalLayout_4.addWidget(self.btnAnalyze)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.listViewParticipants = QtWidgets.QListView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewParticipants.sizePolicy().hasHeightForWidth())
        self.listViewParticipants.setSizePolicy(sizePolicy)
        self.listViewParticipants.setObjectName("listViewParticipants")
        self.verticalLayout_4.addWidget(self.listViewParticipants)
        self.cbShowDiffs = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbShowDiffs.sizePolicy().hasHeightForWidth())
        self.cbShowDiffs.setSizePolicy(sizePolicy)
        self.cbShowDiffs.setObjectName("cbShowDiffs")
        self.verticalLayout_4.addWidget(self.cbShowDiffs)
        self.chkBoxShowOnlyDiffs = QtWidgets.QCheckBox(self.layoutWidget)
        self.chkBoxShowOnlyDiffs.setObjectName("chkBoxShowOnlyDiffs")
        self.verticalLayout_4.addWidget(self.chkBoxShowOnlyDiffs)
        self.chkBoxOnlyShowLabelsInProtocol = QtWidgets.QCheckBox(self.layoutWidget)
        self.chkBoxOnlyShowLabelsInProtocol.setObjectName("chkBoxOnlyShowLabelsInProtocol")
        self.verticalLayout_4.addWidget(self.chkBoxOnlyShowLabelsInProtocol)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.searchLayout = QtWidgets.QHBoxLayout()
        self.searchLayout.setObjectName("searchLayout")
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.searchLayout.addItem(spacerItem1)
        self.lineEditSearch = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
        self.lineEditSearch.setSizePolicy(sizePolicy)
        self.lineEditSearch.setAcceptDrops(False)
        self.lineEditSearch.setClearButtonEnabled(True)
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.searchLayout.addWidget(self.lineEditSearch)
        self.btnSearchSelectFilter = QtWidgets.QToolButton(self.layoutWidget)
        self.btnSearchSelectFilter.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.btnSearchSelectFilter.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btnSearchSelectFilter.setObjectName("btnSearchSelectFilter")
        self.searchLayout.addWidget(self.btnSearchSelectFilter)
        self.lFilterShown = QtWidgets.QLabel(self.layoutWidget)
        self.lFilterShown.setObjectName("lFilterShown")
        self.searchLayout.addWidget(self.lFilterShown)
        self.btnPrevSearch = QtWidgets.QToolButton(self.layoutWidget)
        self.btnPrevSearch.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPrevSearch.sizePolicy().hasHeightForWidth())
        self.btnPrevSearch.setSizePolicy(sizePolicy)
        self.btnPrevSearch.setMaximumSize(QtCore.QSize(20, 16777215))
        icon = QtGui.QIcon.fromTheme("go-previous")
        self.btnPrevSearch.setIcon(icon)
        self.btnPrevSearch.setObjectName("btnPrevSearch")
        self.searchLayout.addWidget(self.btnPrevSearch)
        self.lSearchCurrent = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSearchCurrent.sizePolicy().hasHeightForWidth())
        self.lSearchCurrent.setSizePolicy(sizePolicy)
        self.lSearchCurrent.setMinimumSize(QtCore.QSize(40, 0))
        self.lSearchCurrent.setStyleSheet("QLabel\n"
"{\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.lSearchCurrent.setObjectName("lSearchCurrent")
        self.searchLayout.addWidget(self.lSearchCurrent)
        self.lSlash = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSlash.sizePolicy().hasHeightForWidth())
        self.lSlash.setSizePolicy(sizePolicy)
        self.lSlash.setAlignment(QtCore.Qt.AlignCenter)
        self.lSlash.setObjectName("lSlash")
        self.searchLayout.addWidget(self.lSlash)
        self.lSearchTotal = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSearchTotal.sizePolicy().hasHeightForWidth())
        self.lSearchTotal.setSizePolicy(sizePolicy)
        self.lSearchTotal.setMinimumSize(QtCore.QSize(40, 0))
        self.lSearchTotal.setStyleSheet("QLabel\n"
"{\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.lSearchTotal.setObjectName("lSearchTotal")
        self.searchLayout.addWidget(self.lSearchTotal)
        self.btnNextSearch = QtWidgets.QToolButton(self.layoutWidget)
        self.btnNextSearch.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNextSearch.sizePolicy().hasHeightForWidth())
        self.btnNextSearch.setSizePolicy(sizePolicy)
        self.btnNextSearch.setMaximumSize(QtCore.QSize(20, 16777215))
        icon = QtGui.QIcon.fromTheme("go-next")
        self.btnNextSearch.setIcon(icon)
        self.btnNextSearch.setObjectName("btnNextSearch")
        self.searchLayout.addWidget(self.btnNextSearch)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchLayout.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.searchLayout.addWidget(self.label_2)
        self.lblRSSI = QtWidgets.QLabel(self.layoutWidget)
        self.lblRSSI.setObjectName("lblRSSI")
        self.searchLayout.addWidget(self.lblRSSI)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.searchLayout.addWidget(self.label_3)
        self.lTime = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lTime.sizePolicy().hasHeightForWidth())
        self.lTime.setSizePolicy(sizePolicy)
        self.lTime.setObjectName("lTime")
        self.searchLayout.addWidget(self.lTime)
        self.verticalLayout_3.addLayout(self.searchLayout)
        self.tblViewProtocol = ProtocolTableView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblViewProtocol.sizePolicy().hasHeightForWidth())
        self.tblViewProtocol.setSizePolicy(sizePolicy)
        self.tblViewProtocol.setAcceptDrops(True)
        self.tblViewProtocol.setAutoFillBackground(True)
        self.tblViewProtocol.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblViewProtocol.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tblViewProtocol.setLineWidth(1)
        self.tblViewProtocol.setAutoScroll(True)
        self.tblViewProtocol.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.tblViewProtocol.setAlternatingRowColors(True)
        self.tblViewProtocol.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tblViewProtocol.setTextElideMode(QtCore.Qt.ElideNone)
        self.tblViewProtocol.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblViewProtocol.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblViewProtocol.setShowGrid(False)
        self.tblViewProtocol.setGridStyle(QtCore.Qt.NoPen)
        self.tblViewProtocol.setSortingEnabled(False)
        self.tblViewProtocol.setWordWrap(False)
        self.tblViewProtocol.setCornerButtonEnabled(False)
        self.tblViewProtocol.setObjectName("tblViewProtocol")
        self.tblViewProtocol.horizontalHeader().setDefaultSectionSize(40)
        self.verticalLayout_3.addWidget(self.tblViewProtocol)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lBits = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lBits.sizePolicy().hasHeightForWidth())
        self.lBits.setSizePolicy(sizePolicy)
        self.lBits.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lBits.setObjectName("lBits")
        self.horizontalLayout_4.addWidget(self.lBits)
        self.lBitsSelection = QtWidgets.QLineEdit(self.layoutWidget)
        self.lBitsSelection.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lBitsSelection.setAcceptDrops(False)
        self.lBitsSelection.setReadOnly(True)
        self.lBitsSelection.setObjectName("lBitsSelection")
        self.horizontalLayout_4.addWidget(self.lBitsSelection)
        self.lHex = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lHex.sizePolicy().hasHeightForWidth())
        self.lHex.setSizePolicy(sizePolicy)
        self.lHex.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lHex.setObjectName("lHex")
        self.horizontalLayout_4.addWidget(self.lHex)
        self.lHexSelection = QtWidgets.QLineEdit(self.layoutWidget)
        self.lHexSelection.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lHexSelection.setAcceptDrops(False)
        self.lHexSelection.setReadOnly(True)
        self.lHexSelection.setObjectName("lHexSelection")
        self.horizontalLayout_4.addWidget(self.lHexSelection)
        self.lDecimal = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lDecimal.sizePolicy().hasHeightForWidth())
        self.lDecimal.setSizePolicy(sizePolicy)
        self.lDecimal.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lDecimal.setObjectName("lDecimal")
        self.horizontalLayout_4.addWidget(self.lDecimal)
        self.lDecimalSelection = QtWidgets.QLineEdit(self.layoutWidget)
        self.lDecimalSelection.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lDecimalSelection.setAcceptDrops(False)
        self.lDecimalSelection.setReadOnly(True)
        self.lDecimalSelection.setObjectName("lDecimalSelection")
        self.horizontalLayout_4.addWidget(self.lDecimalSelection)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.lNumSelectedColumns = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lNumSelectedColumns.sizePolicy().hasHeightForWidth())
        self.lNumSelectedColumns.setSizePolicy(sizePolicy)
        self.lNumSelectedColumns.setMinimumSize(QtCore.QSize(40, 0))
        self.lNumSelectedColumns.setObjectName("lNumSelectedColumns")
        self.horizontalLayout_4.addWidget(self.lNumSelectedColumns)
        self.lColumnsSelectedText = QtWidgets.QLabel(self.layoutWidget)
        self.lColumnsSelectedText.setObjectName("lColumnsSelectedText")
        self.horizontalLayout_4.addWidget(self.lColumnsSelectedText)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.cbLabelsets = QtWidgets.QComboBox(self.layoutWidget1)
        self.cbLabelsets.setEditable(True)
        self.cbLabelsets.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cbLabelsets.setObjectName("cbLabelsets")
        self.verticalLayout_2.addWidget(self.cbLabelsets)
        self.listViewLabelNames = ProtocolLabelListView(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewLabelNames.sizePolicy().hasHeightForWidth())
        self.listViewLabelNames.setSizePolicy(sizePolicy)
        self.listViewLabelNames.setAcceptDrops(False)
        self.listViewLabelNames.setObjectName("listViewLabelNames")
        self.verticalLayout_2.addWidget(self.listViewLabelNames)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblLabelValues = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLabelValues.sizePolicy().hasHeightForWidth())
        self.lblLabelValues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblLabelValues.setFont(font)
        self.lblLabelValues.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLabelValues.setObjectName("lblLabelValues")
        self.verticalLayout.addWidget(self.lblLabelValues)
        self.tblLabelValues = LabelValueTableView(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblLabelValues.sizePolicy().hasHeightForWidth())
        self.tblLabelValues.setSizePolicy(sizePolicy)
        self.tblLabelValues.setAlternatingRowColors(True)
        self.tblLabelValues.setShowGrid(False)
        self.tblLabelValues.setObjectName("tblLabelValues")
        self.tblLabelValues.horizontalHeader().setVisible(True)
        self.tblLabelValues.horizontalHeader().setCascadingSectionResizes(False)
        self.tblLabelValues.horizontalHeader().setStretchLastSection(True)
        self.tblLabelValues.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tblLabelValues)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addWidget(self.splitter)

        self.retranslateUi(FAnalysis)
        QtCore.QMetaObject.connectSlotsByName(FAnalysis)

    def retranslateUi(self, FAnalysis):
        _translate = QtCore.QCoreApplication.translate
        FAnalysis.setWindowTitle(_translate("FAnalysis", "Frame"))
        self.lSignalNr.setText(_translate("FAnalysis", "1:"))
        self.lSignalName.setText(_translate("FAnalysis", "Signalname"))
        self.btnSaveProto.setText(_translate("FAnalysis", "Save.."))
        self.cbProtoView.setToolTip(_translate("FAnalysis", "<html><head/><body><p>Set the desired view here.</p><p><br/></p><p>You can set the <span style=\" font-weight:600;\">alignment</span> where evaluation of Hex/ASCII starts using right-click menu in Bits-View. Use this, to correct <span style=\" font-style:italic;\">slided/missing Bits</span> or something like that.</p></body></html>"))
        self.cbProtoView.setItemText(0, _translate("FAnalysis", "Bits"))
        self.cbProtoView.setItemText(1, _translate("FAnalysis", "Hex"))
        self.cbProtoView.setItemText(2, _translate("FAnalysis", "ASCII"))
        self.cbDecoding.setItemText(0, _translate("FAnalysis", "NRZ"))
        self.cbDecoding.setItemText(1, _translate("FAnalysis", "Manchester"))
        self.cbDecoding.setItemText(2, _translate("FAnalysis", "Manchester II"))
        self.cbDecoding.setItemText(3, _translate("FAnalysis", "Differential Manchester"))
        self.cbDecoding.setItemText(4, _translate("FAnalysis", "..."))
        self.lEncodingErrors.setText(_translate("FAnalysis", "Decoding errors for block:"))
        self.lDecodingErrorsValue.setText(_translate("FAnalysis", "0 (0.00%)     "))
        self.btnAnalyze.setText(_translate("FAnalysis", "Analyze"))
        self.label_4.setText(_translate("FAnalysis", "Show these participants:"))
        self.cbShowDiffs.setText(_translate("FAnalysis", "Mark diffs in protocol"))
        self.chkBoxShowOnlyDiffs.setText(_translate("FAnalysis", "Show only diffs in protocol"))
        self.chkBoxOnlyShowLabelsInProtocol.setText(_translate("FAnalysis", "Show only labels in protocol"))
        self.lineEditSearch.setPlaceholderText(_translate("FAnalysis", "Search Pattern"))
        self.btnSearchSelectFilter.setText(_translate("FAnalysis", "Search"))
        self.lFilterShown.setText(_translate("FAnalysis", "shown: 42/108"))
        self.btnPrevSearch.setText(_translate("FAnalysis", "<"))
        self.lSearchCurrent.setText(_translate("FAnalysis", "-"))
        self.lSlash.setText(_translate("FAnalysis", "/"))
        self.lSearchTotal.setText(_translate("FAnalysis", "-"))
        self.btnNextSearch.setText(_translate("FAnalysis", ">"))
        self.label_2.setToolTip(_translate("FAnalysis", "<html><head/><body><p>The <span style=\" font-weight:600;\">Received Signal Strength Indicator</span> indicates the average signal power of the current block.</p></body></html>"))
        self.label_2.setText(_translate("FAnalysis", "RSSI:"))
        self.lblRSSI.setToolTip(_translate("FAnalysis", "<html><head/><body><p>The <span style=\" font-weight:600;\">Received Signal Strength Indicator</span> indicates the average signal power of the current block.</p></body></html>"))
        self.lblRSSI.setText(_translate("FAnalysis", "1.04"))
        self.label_3.setToolTip(_translate("FAnalysis", "<html><head/><body><p>The <span style=\" font-weight:600;\">Block Start</span> is the point in time when a protocol block begins. Additionally the relative time (+ ...) from the previous block is shown.</p></body></html>"))
        self.label_3.setText(_translate("FAnalysis", "Timestamp:"))
        self.lTime.setToolTip(_translate("FAnalysis", "<html><head/><body><p>The <span style=\" font-weight:600;\">Block Start</span> is the point in time when a protocol block begins. Additionally the relative time (+ ...) from the previous block is shown.</p></body></html>"))
        self.lTime.setText(_translate("FAnalysis", "0 (+0)"))
        self.lBits.setText(_translate("FAnalysis", "Bit:"))
        self.lHex.setText(_translate("FAnalysis", "Hex:"))
        self.lDecimal.setText(_translate("FAnalysis", "Decimal:"))
        self.lNumSelectedColumns.setText(_translate("FAnalysis", "0"))
        self.lColumnsSelectedText.setText(_translate("FAnalysis", "Column(s) selected"))
        self.label.setText(_translate("FAnalysis", "Show these protocol labels:"))
        self.lblLabelValues.setText(_translate("FAnalysis", "Label values for block"))

from urh.ui.views.LabelValueTableView import LabelValueTableView
from urh.ui.views.ProtocolLabelListView import ProtocolLabelListView
from urh.ui.views.ProtocolTableView import ProtocolTableView
from urh.ui.views.ProtocolTreeView import ProtocolTreeView
from . import urh_rc
