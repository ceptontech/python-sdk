#!/usr/bin/env python3

import unittest

import cepton_sdk3 as sdk


class SdkApiTest(unittest.TestCase):
    """API tests"""

    def test_initialize(self):
        """Test initialize and deinitialize"""
        sdk.initialize()
        sdk.deinitialize()

    def test_read_frames(self):
        """No-op"""
