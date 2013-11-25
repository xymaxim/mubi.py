# coding: utf-8

import os
import unittest

from mubi import login, MubiException


MUBI_EMAIL = os.getenv('MUBI_EMAIL')
MUBI_PASSWORD = os.getenv('MUBI_PASSWORD')
MUBI_USER_ID = os.getenv('MUBI_USER_ID')

class MubiTest(unittest.TestCase):
    def test_login(self):
        _, me = login(MUBI_EMAIL, MUBI_PASSWORD, identify=True)
        assert me == MUBI_USER_ID

    def test_invalid_credentials(self):
        with self.assertRaises(MubiException):
            login('invalid', 'credentials')


if __name__ == '__main__':
    unittest.main()
