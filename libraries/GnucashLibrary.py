from decimal import Decimal
import re
import os

from RPA.Desktop import Desktop
from settings import GNUCASH_DATABASE, GNUCASH_EXECUTABLE, GNUCASH_LOCK_FILE


class GnucashLibrary:
    def __init__(self):
        self.desktop = Desktop() # BuiltIn().get_library_instance("RPA.Desktop")
        self.gnuapp = None

    def remove_lock_file(self):
        if os.path.exists(GNUCASH_LOCK_FILE):
            os.remove(GNUCASH_LOCK_FILE)
            print(f"File {GNUCASH_LOCK_FILE} has been removed successfully")

    def open_gnucash(self):
        self.remove_lock_file()
        self.gnuapp = self.desktop.open_application(GNUCASH_EXECUTABLE, GNUCASH_DATABASE)
        # Use image locator here instead as the "New" option has image and a small text, it's very fragile with OCR
        localor = f"image:{os.path.join('resources', 'gnucash_new-path.png')}"
        self.desktop.wait_for_element(localor, timeout=20)
        # Maximize the app to make sure OCR finds locators only from this application
        self.desktop.press_keys("cmd", "up")

    def close_gnucash(self):
        if self.gnuapp:
            self.desktop.close_application(self.gnuapp)

    def open_create_new_account_form(self):
        localor = f"image:{os.path.join('resources', 'gnucash_new-path.png')}"
        self.desktop.click(localor)
        self.desktop.wait_for_element('ocr:"Account name",80')

    def click_ok(self):
        self.desktop.click("ocr:OK")

    def click_cancel(self):
        locator = f"image:{os.path.join('resources', 'gnucash_cancel-path.png')}"
        self.desktop.click(locator)

    def _fill_name(self, name):
        # Finding the correct "Account name" region is fragile.
        # Better just exploit the fact that the cursor is already
        # in the correct position.
        # name_text_regions = self.desktop.find_elements(locator)
        # name_input_region = self.desktop.move_region(name_text_regions[0], 200, 0)
        # self.desktop.click(name_input_region)
        self.desktop.type_text(name)

    def _fill_region(self, region, text):
        self.desktop.click(region)
        self.desktop.type_text(text)

    def _fill_description(self, region, text):
        self.desktop.click(f"{region} offset:0,40")
        self.desktop.type_text(text)

    def _fill_notes(self, text):
        self.desktop.click("ocr:Notes + offset:200,0")
        self.desktop.type_text(text)

    def fill_data(self):
        self._fill_name("OCR testing")
        region = self.desktop.find_element('ocr:"Account code" + offset:200,0')
        self._fill_region(region, "1337")
        self._fill_description(region, "Found by OCR and region locators")
        self._fill_notes("Next we'll find the cancel button by image template")
