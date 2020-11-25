from django.test import TestCase

from idvalidator import ares


class IdTestCase(TestCase):

    def test_id_validation(self):
        self.assertEqual(ares.validate_business_id("69663963"), True)
        self.assertEqual(ares.validate_business_id("75151472"), True)
        self.assertEqual(ares.validate_business_id("07398824"), True)
        self.assertEqual(ares.validate_business_id("00064581"), True)

        self.assertEqual(ares.validate_business_id("12345678"), False)
        self.assertEqual(ares.validate_business_id("abcdefgh"), False)
        self.assertEqual(ares.validate_business_id("abcd"), False)
        self.assertEqual(ares.validate_business_id("1234"), False)
        self.assertEqual(ares.validate_business_id("1"), False)
