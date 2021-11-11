import unittest
from ChangePassword import *
from TestData import *

class TestChangePassword(unittest.TestCase):
    def test_change_password_passed(self):
        self.assertTrue(change_password(old_pwd_match,new_pwd_valid))

    def test_old_password_empty_failed(self):
        self.assertFalse(change_password('', new_pwd_valid))

    def test_new_password_empty_failed(self):
        self.assertFalse(change_password(old_pwd_match, ''))

    def test_old_password_not_match_failed(self):
        self.assertFalse(change_password(old_pwd_not_match, new_pwd_valid))

    def test_old_and_new_password_are_similar_failed(self):
        self.assertFalse(change_password(old_pwd_similar, new_pwd_similar))

    def test_password_less_than_min_char_requirement_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_less_min_char))

    def test_password_equal_to_min_char_requirement_passed(self):
        self.assertTrue(change_password(old_pwd_match, new_pwd_equal_min_char))

    def test_password_contain_non_alnum_special_char_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_with_thai))

    def test_password_no_upper_case_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_no_upper))

    def test_password_min_upper_case_passed(self):
        self.assertTrue(change_password(old_pwd_match, new_pwd_min_upper))

    def test_password_no_lower_case_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_no_lower))

    def test_password_min_lower_case_passed(self):
        self.assertTrue(change_password(old_pwd_match, new_pwd_min_lower))

    def test_password_no_numeric_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_no_numeric))

    def test_password_min_numeric_passed(self):
        self.assertTrue(change_password(old_pwd_match, new_pwd_min_numeric))

    def test_password_no_special_char_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_no_special))

    def test_password_min_special_char_passed(self):
        self.assertTrue(change_password(old_pwd_match, new_pwd_min_special))

    def test_password_repeat_char_equal_to_limit_passed(self):
        self.assertTrue(change_password(old_pwd_match, new_pwd_repeat_char))

    def test_password_repeat_char_greater_than_limit_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_exceed_repeat_char))

    def test_password_special_char_equal_to_limit_passed(self):
        self.assertTrue(change_password(old_pwd_match, new_pwd_special_char))

    def test_password_special_char_greater_than_limit_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_exceed_special_char))

    def test_password_numeric_less_than_50_percent_failed(self):
        self.assertTrue(change_password(old_pwd_match, new_pwd_less_numeric_50_percent))

    def test_password_numeric_equal_to_50_percent_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_equal_numeric_50_percent))

    def test_password_numeric_greater_than_50_percent_failed(self):
        self.assertFalse(change_password(old_pwd_match, new_pwd_greater_numeric_50_percent))


if __name__ == '__main__':
    unittest.main()