#!/usr/bin/env python3

from tidas.duts import duts
from tidas.isi import isi

ERROR_MESSAGE = "[selftest] test Failure!"


class Test_Loop:

    def setup_class(self):
        print("""
[FLASH_TEST] Preconditions Definitions:
  - HW disconnect all duts
  - Flash latest ENO SW
  - Boot the phone, wait the phone is fully start
""")
        self.duts = duts()
        for dut in self.duts:
            dut.hw_disconnect()
        assert  self.duts[0].do_safe_flashing(flash_type="eno"), "Flashing/booting issue"

    def test_ST_CAMERA_IF_TEST(self):
        assert isi("ST_CAMERA_IF_TEST")[0], ERROR_MESSAGE

    def test_ST_SEC_CAMERA_IF_TEST(self):
        assert isi("ST_SEC_CAMERA_IF_TEST")[0], ERROR_MESSAGE

    def test_ST_CAMERA_FLASH_TEST(self):
        assert isi("ST_CAMERA_FLASH_TEST")[0], ERROR_MESSAGE

    def test_ST_DISPLAY_IF_TEST(self):
        assert isi("ST_DISPLAY_IF_TEST")[0], ERROR_MESSAGE

    def test_ST_BTEMP_TEST(self):
        assert isi("ST_BTEMP_TEST")[0], ERROR_MESSAGE

    def test_ST_PA_TEMP_TEST(self):
        assert isi("ST_PA_TEMP_TEST")[0], ERROR_MESSAGE

    def test_ST_OSC_TEMP_TEST(self):
        assert isi("ST_OSC_TEMP_TEST")[0], ERROR_MESSAGE

    def test_ST_BATTERY_ALARM_TEST(self):
        assert isi("ST_BATTERY_ALARM_TEST")[0], ERROR_MESSAGE

    def test_ST_CURRENT_CONS_TEST(self):
        assert isi("ST_CURRENT_CONS_TEST")[0], ERROR_MESSAGE

    def test_ST_ACCEL_IF_TEST(self):
        assert isi("ST_ACCEL_IF_TEST")[0], ERROR_MESSAGE

    def test_ST_PROXIMITY_TEST(self):
        assert isi("ST_PROXIMITY_TEST")[0], ERROR_MESSAGE

    def test_ST_TOUCH_TEST(self):
        assert isi("ST_TOUCH_TEST")[0], ERROR_MESSAGE

    def test_ST_WLAN_TEST(self):
        assert isi("ST_WLAN_TEST")[0], ERROR_MESSAGE

    def test_ST_RADIO_TEST(self):
        assert isi("ST_RADIO_TEST")[0], ERROR_MESSAGE

    def test_ST_BT_IF_TEST(self):
        assert isi("ST_BT_IF_TEST")[0], ERROR_MESSAGE
