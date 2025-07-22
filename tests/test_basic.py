#!/usr/bin/env python3

import unittest

import cepton_sdk3 as sdk


class BasicTests(unittest.TestCase):
    """Basic tests"""

    def test_initialize(self):
        """Test initialize and deinitialize"""
        sdk.initialize()
        sdk.deinitialize()
