import unittest


class TestPalindrome(unittest.TestCase):

    def test_a(self):
        resultado = is_palindrome("a")
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome("aa")
        self.assertEqual(resultado, True)

    def test_aCa(self):
        resultado = is_palindrome("aCa")
        self.assertEqual(resultado, True)

    def test_ABBA(self):
        resultado = is_palindrome("ABBA")
        self.assertEqual(resultado, True)

    def test_ABCBA(self):
        resultado = is_palindrome("ABCBA")
        self.assertEqual(resultado, True)

    def test_ABCCBA(self):
        resultado = is_palindrome("ABCCBA")
        self.assertEqual(resultado, True)

    def test_neuquen(self):
        resultado = is_palindrome("neuquen")
        self.assertEqual(resultado, True)

    def test_ABbA(self):
        resultado = is_palindrome("ABbA")
        self.assertEqual(resultado, True)

    def test_ala(self):
        resultado = is_palindrome("ala")
        self.assertEqual(resultado, True)

    def test_madam(self):
        resultado = is_palindrome("madam")
        self.assertEqual(resultado, True)

    def test_racecar(self):
        resultado = is_palindrome("racecar")
        self.assertEqual(resultado, True)

if __name__ == '__main__':
    unittest.main()