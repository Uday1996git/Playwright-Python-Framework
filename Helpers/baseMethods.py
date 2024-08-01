import yaml
from playwright.sync_api import Page
import os

class Utility:

    def __init__(self, page: Page):
        self.page = page

    def nav_To_Url(self, URL: str):
        self.page.goto(URL, wait_until="load")

    def locatorElement(self, loc):
        return self.page.locator(loc)

    def get_Title(self):
        return self.page.title()

    def get_current_URL(self):
        return self.page.url


class support:

    def read_ConfigValue(self, key):
        config_file = os.path.join('Configs', 'appConfig.yaml')
        # ../Configs/appConfig.yaml
        with open(config_file, "r") as file:
            service = yaml.safe_load(file)
        return service[key]

    def is_Enabled(self, element):
        if element.is_enabled:
            assert True
        else:
            assert False

    def send_Text(self, element, text):
        element.fill(text)

    def isVisible(self, element):
        if element.is_visible(timeout=2000):
            assert True
        else:
            assert False

    def get_Text(self, element):
        return element.inner_text()

    def click(self, element):
        element.click()

    def validate_Strings(self, expected: str or int, actual: str or int):
        assert expected == actual

    def return_testName(self, request):
        return request.node.name
