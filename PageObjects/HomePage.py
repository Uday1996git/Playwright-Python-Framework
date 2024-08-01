import logging
from enum import Enum
from ObjectsManager import ObjectManager
from playwright.sync_api import Page


class LocatorsEnum(Enum):
    get_Started_button = "Get started"
    get_Started_heading = ".theme-doc-markdown h1"


class HomePage:

    def __init__(self, page: Page):
        self.page = page

    def get_Started_Button(self, uRL: str):
        logging.info("Running Get Started button Test case")
        ObjectManager.get_UtilityObject(self.page).nav_To_Url(uRL)
        logging.info("Successfully navigated to desired url")
        get_started_button = self.page.get_by_text(LocatorsEnum['get_Started_button'].value)
        logging.info("Successfully located element")
        ObjectManager.get_supportObject().isVisible(get_started_button)
        logging.info("Get started button is visible and is validated")
        ObjectManager.get_supportObject().click(get_started_button)
        logging.info("Successfully clicked on get Started button")
        ObjectManager.get_supportObject().validate_Strings("Installation",
                                                           ObjectManager.get_supportObject().get_Text(
                                                               ObjectManager.get_UtilityObject(self.page).locatorElement(LocatorsEnum['get_Started_heading'].value)))
        logging.info("Validated the Installation heading on the get started page")

