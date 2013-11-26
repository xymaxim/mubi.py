# coding: utf-8

import os
import unittest

from mubi import login, MubiException


class MubiTest(unittest.TestCase):
    def test_login(self):
        _, me = login(identify=True)
        assert me == os.environ['MUBI_USER_ID']

    def test_invalid_credentials(self):
        with self.assertRaises(MubiException):
            login('invalid', 'credentials')


if __name__ == '__main__':
    unittest.main()
