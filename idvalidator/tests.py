from django.test import TestCase

from idvalidator import ares


class IdTestCase(TestCase):

    def test_checksum_validation(self):
        self.assertEqual(ares.validate_business_id_checksum("69663963"), True)
        self.assertEqual(ares.validate_business_id_checksum("75151472"), True)
        self.assertEqual(ares.validate_business_id_checksum("07398824"), True)
        self.assertEqual(ares.validate_business_id_checksum("00064581"), True)

        self.assertEqual(ares.validate_business_id_checksum("12345678"), False)
        self.assertEqual(ares.validate_business_id_checksum("abcdefgh"), False)
        self.assertEqual(ares.validate_business_id_checksum("abcd"), False)
        self.assertEqual(ares.validate_business_id_checksum("1234"), False)
        self.assertEqual(ares.validate_business_id_checksum("1"), False)
