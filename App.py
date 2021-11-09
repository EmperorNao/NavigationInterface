from GUI.StatisticUi import StatisticModel, StatisticUi
from GUI.NavigationUI import NavigationModel, NavigationUi
from PyQt5 import QtWidgets
import sys

TEST_MODE = "navigation"#"stat"#


if __name__ == "__main__":

    # Create an instance of `QApplication`
    app = QtWidgets.QApplication(sys.argv)
    # Show the calculator's GUI

    if len(sys.argv) > 1 or TEST_MODE != "":

        app_mode = ""
        if len(sys.argv) > 1:
            app_mode = sys.argv[1]
        else:
            app_mode = TEST_MODE

        if app_mode == "stat":
            model = StatisticModel()
            view = StatisticUi(model)

        elif app_mode == "navigation":
            model = NavigationModel()
            view = NavigationUi(model)

        else:
            print("Wrong argument was provided, expected on of: 'navigation' or 'stat'")

    else:
        print("Please, provide one of arguments"
              "\n'navigation' - as main application"
              "\n'stat' - as application to count statistics")
        exit(0)

    view.showMaximized()
    # Create instances of the model and the controller
    try:
        sys.exit(app.exec_())
    except:
        sys.exit()
