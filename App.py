from GUI import *
import sys

if __name__ == "__main__":
    # Create an instance of `QApplication`
    app = QtWidgets.QApplication(sys.argv)
    # Show the calculator's GUI
    model = Navigation()
    view = NavigationUi(model)
    view.showMaximized()
    # Create instances of the model and the controller
    try:
        sys.exit(app.exec_())
    except:
        sys.exit()
