import unittest
import pybank

class TestValidateEmailFunction(unittest.TestCase):
    def test_that_validate_email_function_exists(self):
        pybank.validate_email("adex@gmail.com")

    def test_that_if_email_is_eight_characters_long_it_returns_true(self):
        actual = pybank.validate_email("adex@gmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_that_if_email_is_not_eight_characters_long_it_returns_false(self):
        actual = pybank.validate_email("ade.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_that_email_contains_at_symbol_returns_true(self):
        actual = pybank.validate_email("adex@gmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_that_email_does_not_contain_at_symbol_returns_false(self):
        actual = pybank.validate_email("adexgmail.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_that_email_does_not_start_with_at_symbol_returns_true(self):
        actual = pybank.validate_email("adex@gmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_that_email_starts_with_at_symbol_returns_false(self):
        actual = pybank.validate_email("@adex@gmail.com")
        expected = False
        self.assertEqual(actual, expected)

    def test_that_email_does_not_end_with_at_symbol_returns_true(self):
        actual = pybank.validate_email("adex@gmail.com")
        expected = True
        self.assertEqual(actual, expected)

    def test_that_email_does_not_end_with_at_symbol_returns_false(self):
        actual = pybank.validate_email("adex@gmail.com@")
        expected = False
        self.assertEqual(actual, expected)


class TestCalculateBalanceFunction(unittest.TestCase):
    def test_that_calculate_balance_function_exists(self):
        pybank.calculate_balance([100, 200, -230])

    def test_that_calculate_balance_returns_zero_for_empty_list(self):
        actual = pybank.calculate_balance([])
        expected = 0
        self.assertEqual(actual, expected)

    def test_that_calculate_balance_function_returns_correct_positive_balance(self):
        actual = pybank.calculate_balance([100, 200, -230])
        expected = 70
        self.assertEqual(actual, expected)

    def test_that_calculate_balance_function_returns_correct_negative_balance(self):
        actual = pybank.calculate_balance([100, -200, -100])
        expected = -200
        self.assertEqual(actual, expected)


class TestIsStrongPasswordFunction(unittest.TestCase):
    def test_that_is_strong_password_function_exists(self):
        pybank.is_strong_password("a5afa3m")

    def test_that_if_password_is_eight_characters_long_it_returns_true(self):
        actual = pybank.is_strong_password("#541adcom")
        expected = True
        self.assertEqual(actual, expected)

    def test_that_if_password_is_not_eight_characters_long_it_returns_false(self):
        actual = pybank.is_strong_password("adcom")
        expected = False
        self.assertEqual(actual, expected)


class TestApplyInterestFunction(unittest.TestCase):
    def test_that_apply_interest_function_exists(self):
        pybank.apply_interest(1000, 12, 3)

    def test_that_apply_interest_returns_zero_if_rate_is_negative(self):
        actual = pybank.apply_interest(1000, -1, 3)
        expected = 0
        self.assertEqual(actual, expected)

    def test_that_apply_interest_returns_zero_if_years_is_less_than_one(self):
        actual = pybank.apply_interest(1000, 12, 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_that_apply_interest_returns_returns_correct_interest(self):
        actual = pybank.apply_interest(1000, 10, 1)
        expected = 1100
        self.assertEqual(actual, expected)


class TestGetTransactionSummaryFunction(unittest.TestCase):
    def test_that_get_transaction_summary_function_exists(self):
        pybank.get_transaction_summary([])

    def test_that_get_transaction_summary_returns_correct_total_credit(self):
        result = pybank.get_transaction_summary([["credit", 2000], ["debit", 500], ["credit", 300]])
        actual = result[0][1]
        expected = 2300
        self.assertEqual(actual, expected)

    def test_that_get_transaction_summary_returns_correct_total_debit(self):
        result = pybank.get_transaction_summary([["credit", 2000], ["debit", 500], ["credit", 300]])
        actual = result[1][1]
        expected = 500
        self.assertEqual(actual, expected)

    def test_that_get_transaction_summary_returns_correct_net_balance(self):
        result = pybank.get_transaction_summary([["credit", 2000], ["debit", 500], ["credit", 300]])
        actual = result[2][1]
        expected = 1800
        self.assertEqual(actual, expected)

    def test_that_get_transaction_summary_returns_correct_number_of_transactions(self):
        result = pybank.get_transaction_summary([["credit", 2000], ["debit", 500], ["credit", 300]])
        actual = result[3][1]
        expected = 3
        self.assertEqual(actual, expected)
