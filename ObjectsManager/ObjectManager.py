from playwright.sync_api import Page
from Helpers.baseMethods import support, Utility
from PageObjects.HomePage import HomePage
from PageObjects.LearnVideos import Learn_Vidoes
from Utility.BrowserFactory import Controller


def get_UtilityObject(page: Page):
    obj = Utility(page)
    return obj


def get_supportObject():
    obj = support()
    return obj


def get_HomaPageObject(page: Page):
    obj = HomePage(page)
    return obj


def get_Learn_Videos_Object(page: Page):
    obj = Learn_Vidoes(page)
    return obj


def get_ControllerObject():
    obj = Controller()
    return obj
