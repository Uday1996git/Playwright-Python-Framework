from ObjectsManager import ObjectManager

URL = ObjectManager.get_supportObject().read_ConfigValue("env")
print(URL)

def test_first(py_fixture):
    try:
        page = py_fixture
        ObjectManager.get_HomaPageObject(page).get_Started_Button(URL)
    except:
        raise Exception("Failed to validate the get started button")
