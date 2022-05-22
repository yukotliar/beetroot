import sys
from practice_calculator.view import *
from .controler import CanculatorControler
from .model import evaluateExpression


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    CanculatorControler(model=evaluateExpression, view=ui)

    sys.exit(app.exec_())
