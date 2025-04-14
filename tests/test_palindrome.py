from src.palindrome import is_palindrome
import unittest


class TestPalindrome(unittest.TestCase):

    def test_a(self):
        resultado = is_palindrome("a")
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome ("aa")
        self.assertEqual(resultado,(True))
  
    def test_as(self):
        resultado = is_palindrome ("as")
        self.assertEqual(resultado, False)

    def test_aca(self):
        resultado = is_palindrome("ana")
        self.assertEqual(resultado, True)

    def test_apta(self):
        resultado = is_palindrome("apta")
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    
if __name__ == '__main__':
    unittest.main()