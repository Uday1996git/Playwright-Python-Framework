import os
import pytest
from playwright.sync_api import BrowserContext
from ObjectsManager import ObjectManager
import shutil


browser = ObjectManager.get_supportObject().read_ConfigValue("browser")
traces = ObjectManager.get_supportObject().read_ConfigValue("Traces")
param = ObjectManager.get_supportObject().read_ConfigValue("headless")
value = ObjectManager.get_supportObject().read_ConfigValue("slowmo")
record_video = ObjectManager.get_supportObject().read_ConfigValue("RecordVideo")


def check_Traces(context: BrowserContext):
    context.tracing.start(
        name="Test Traces",
        screenshots=True,
        snapshots=True,
        sources=True
    )


@pytest.fixture(scope="session")
def playwrightInstance():
    playwright = ObjectManager.get_ControllerObject().syncPlaywrightInstance()
    try:
        if playwright is not None and record_video is True:
            shutil.rmtree("../RecordedVideos")
    except OSError as e:
        print(f"Error deleting the file: RecordedVideos - {e.strerror}")
    yield playwright


@pytest.fixture(scope="function")
def py_fixture(request, playwrightInstance):
    test_name = ObjectManager.get_supportObject().return_testName(request)
    page, context = ObjectManager.get_ControllerObject().startBrowser(browser, param, value, playwrightInstance, record_video, test_name)
    if traces is True:
        check_Traces(context)
    yield page
    ObjectManager.get_ControllerObject().tear_down(context, traces, test_name, page)
    print("\nclosed all the opened connections")
