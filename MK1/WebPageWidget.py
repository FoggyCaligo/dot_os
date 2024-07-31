from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
    def release(self):
        self.deleteLater()
        self.close()

class WebPageWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self._editUrl = QLineEdit()
        self._webview = WebView()
        self.initControl()
        self. initLayout()
    def release(self):
        self._webview.release()
    def initLayout(self):
        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(0,4,0,0)
        vbox.setSpacing(4)
        subwgt = QWidget()
        subwgt.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        hbox=QHBoxLayout(subwgt)
        hbox.setContentsMargins(4,0,4,0)
        hbox.setSpacing(4)
        hbox.addWidget(self._editUrl)
        vbox.addWidget(subwgt)
        vbox.addWidget(self._webview)

    def initControl(self):
        self._editUrl.returnPressed.connect(self.onEditUrlReturnPressed)
    def onEditUrlReturnPressed(self):
        url = self._editUrl.text()
        self._webview.load(QUrl(url))


if __name__=='__main__':
    import sys
    from PyQt5.QtCore import QCoreApplication
    from PyQt5.QtWidgets import QApplication

    QApplication.setStyle('fusion')
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    wgt_ = WebPageWidget()
    wgt_.show()
    wgt_.resize(600,600)

    app.exec_()
    wgt_.release()

