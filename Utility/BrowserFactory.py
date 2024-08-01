from playwright.sync_api import sync_playwright, BrowserContext, Page, Playwright

global brow


class Controller:

    # async def setup(self, browser: str):
    #     async with async_playwright() as playwright:
    #         if browser.lower() == "chromium":
    #             launch_browser = await playwright.chromium.launch(headless=param, slow_mo=value)
    #         elif browser.lower() == "firefox":
    #             launch_browser = await playwright.firefox.launch(headless=param, slow_mo=value)
    #         context = await launch_browser.new_context(no_viewport=True)
    #         page = await context.new_page()
    #         yield page

    def syncPlaywrightInstance(self):
        playwright = sync_playwright().start()
        return playwright

    def chooseBroswer(self, browser: str, param, value, playwright: Playwright):
        if browser is not None:
            if browser.lower() == "chromium" or "chrome":
                return playwright.chromium.launch(headless=param, slow_mo=value)
            elif browser.lower() == "firefox":
                return playwright.firefox.launch(headless=param, slow_mo=value)
            else:
                raise NameError(f"{browser} is not supported")

    def startBrowser(self, browser: str, param, value, playwright: Playwright,
                     record_video_option: bool, record_video_dir):
        global brow
        brow = Controller.chooseBroswer(self, browser, param, value, playwright)
        context = Controller.check_record_video(self, record_video_option, record_video_dir)
        page = context.new_page()
        if brow is None or context is None or page is None:
            raise AttributeError("Null pointer exception")
        return page, context

    def tear_down(self, context: BrowserContext, traces: bool, trace_name, page: Page):
        if context and page is not None:
            if traces is True:
                context.tracing.stop(path=f"Traces//{trace_name}.zip")
            page.close()
            context.close()
        brow.close()

    def check_record_video(self, record_video_option: bool, record_video_dir):
        if record_video_option is True:
            context = brow.new_context(record_video_dir=f"RecordedVideos/{record_video_dir}")
        else:
            context = brow.new_context()
        return context
