from enum import Enum
from playwright.sync_api import Page
from ObjectsManager import ObjectManager


class LocatorEnums(Enum):
    get_Learn_Videos = "Learn Videos"


class Learn_Vidoes:

    def __init__(self, page: Page):
        self.page = page

    def validate_Learn_Videos(self, URL: str):
        ObjectManager.get_UtilityObject(self.page).nav_To_Url(URL)
        learn_videos = self.page.get_by_role("link", name=LocatorEnums['get_Learn_Videos'].value)
        ObjectManager.get_supportObject().isVisible(learn_videos)
        ObjectManager.get_supportObject().is_Enabled(learn_videos)
        ObjectManager.get_supportObject().click(learn_videos)
