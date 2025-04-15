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

    def test_ala_la(self):
       resultado = is_palindrome("ala la")
       self.assertEqual(resultado, True)


    def test_anita_lava_la_tina(self):
       resultado = is_palindrome("Anita lava la tina")
       self.assertEqual(resultado, True)


    def test_Aman_a_plan_a_canal_Panama(self):
       resultado = is_palindrome("A man, a plan, a canal: Panama")
       self.assertEqual(resultado, True)

    def test_levels(self):
       resultado = is_palindrome("levels")
       self.assertEqual(resultado, False)


    def test_hello(self):
       resultado = is_palindrome("hello")
       self.assertEqual(resultado, False)


    def test_aCs(self):
       resultado = is_palindrome("aCs")
       self.assertEqual(resultado, False)


    def test_ab(self):
       resultado = is_palindrome("ab")
       self.assertEqual(resultado, False)

    def test_avion(self):
       resultado = is_palindrome("avion")
       self.assertEqual(resultado, False)

    def test_trabajo_practico(self):
        resultado = is_palindrome("trabajo practico")
        self.assertEqual(resultado, False)

    def test_palabras(self):
        resultado = is_palindrome("palabras")
        self.assertEqual(resultado, False)

    def test_vacio(self):
        resultado = is_palindrome("")
        self.assertEqual(resultado, True)

    def test_aA(self):
        resultado = is_palindrome("aA")
        self.assertEqual(resultado, True)

    def test_A(self):
        resultado = is_palindrome("A")
        self.assertEqual(resultado, True)

if __name__ == '__main__':
    unittest.main()