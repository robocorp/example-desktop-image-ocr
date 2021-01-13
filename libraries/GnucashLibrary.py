from decimal import Decimal
import re
import time

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from RPA.Desktop.keywords import keyword


class GnucashLibrary:
    def __init__(self):
        self.desktop = BuiltIn().get_library_instance("RPA.Desktop")
        self.gnuapp = None

    @keyword
    def open_gnucash(self):
        builtin = BuiltIn()
        self.gnuapp = self.desktop.open_application(
            builtin.get_variable_value("$GNUCASH_EXECUTABLE"),
            builtin.get_variable_value("$GNUCASH_DATABASE"),
        )
        self.desktop.wait_for_element("ocr:New", timeout=20)

    @keyword
    def close_gnucash(self):
        if self.gnuapp:
            self.desktop.close_application(self.gnuapp)

    @keyword
    def open_create_new_account_form(self):
        self.desktop.click("ocr:New")
        self.desktop.wait_for_element("ocr:New Account")

    @keyword
    def fill_name(self, text):
        locator = "ocr:Account name"
        # Finding the correct "Account name" region is fragile.
        # Better just exploit the fact that the cursor is already
        # in the correct position.
        # name_text_regions = self.desktop.find_elements(locator)
        # name_input_region = self.desktop.move_region(name_text_regions[0], 200, 0)
        # self.desktop.click(name_input_region)
        self.desktop.type_text(text)

    @keyword
    def fill_code_and_get_region(self, text):
        region = self.desktop.find_element("ocr:Account code")
        region = region.move(200,0)
        self.desktop.click(region)
        self.desktop.type_text(text)
        return region

    @keyword
    def fill_description(self, region, text):
        region = region.move(0, 70)
        self.desktop.click(region)
        self.desktop.type_text(text)

    @keyword
    def fill_notes(self, text):
        self.desktop.click_with_offset("ocr:Notes", 200, 0)
        self.desktop.type_text(text)

    @keyword
    def click_cancel(self):
        locator = "image:resources/gnucash_newaccount_cancel_button.png"
        self.desktop.click(locator)

    @keyword
    def click_ok(self):
        self.desktop.click("ocr:OK")

    @keyword
    def get_net_assets(self):
        """
        Get the net assets sum visible in the lower part of the screen.

        This is only done in Python as it is easier and more sensible
        to implement.
        """
        netassets_region = self.desktop.find_element('ocr:"Net Assets"')
        sum_region = self.desktop.move_region(netassets_region, 100, 0)
        # Sometimes you have to play around with the region size:
        sum_region = self.desktop.resize_region(sum_region, bottom=10)
        sum_text = self.desktop.read_text(sum_region)

        assets = Decimal(self._get_sum_from_raw_text(sum_text))
        if assets == 0:
            logger.warn(f"No assets! ({assets})")

        return assets

    def _get_sum_from_raw_text(self, text):
        matches = re.match(r".*(\d+\,\d+).*", text)
        if not matches:
            raise RuntimeError("Couldn't find net assets sum")
        return matches.group(1).replace(",", ".")
