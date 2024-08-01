from ObjectsManager import ObjectManager
import os

URL = ObjectManager.get_supportObject().read_ConfigValue("env")


def test_2ndTest(py_fixture):
    print("Current Working Directory is " + os.getcwd())
    try:
        page = py_fixture
        ObjectManager.get_Learn_Videos_Object(page).validate_Learn_Videos(URL)
    except:
        raise Exception("Failed to validate Learn Videos button")

