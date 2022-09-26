import unittest


# Testing function + len()
def factors(n):
    p = 2
    f = list()
    while n >= p*p :
        if n % p == 0:
            f.append(p)
            n = int(n / p)
        else:
           p = p + 1
    f.append(n)
    return f

def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
        else:
            return True

def vowels(text):
    v = list()
    for i in text:
        if i in 'aeiouAEIOU':
            v.append(i)
    return v


# Our class
class TestingTask(unittest.TestCase):
    def test_factors(self):
        self.assertCountEqual(factors(1), [1], "Should be [1]")
        self.assertCountEqual(factors(7), [7], "Should be [7]")
        self.assertCountEqual(factors(10), [5,2], "Should be [5,2]")
        self.assertCountEqual(factors(18), [2,3,3], "Should be [2,3,3]")

    def test_is_prime(self):
        self.assertEqual(is_prime(-1), False, "Should be False")
        self.assertEqual(is_prime(0), False, "Should be False")
        self.assertEqual(is_prime(3), True, "Should be True")
        self.assertEqual(is_prime(10), False, "Should be False")
        self.assertEqual(is_prime(131), True, "Should be True")

    def test_vowels(self):
        self.assertCountEqual(vowels("s"), [], 'Should be []')
        self.assertCountEqual(vowels("skills"), ["i"], 'Should be ["i"]')
        self.assertCountEqual(vowels("londOn"), ["o", "O"], 'Should be ["o", "O"]')

    def test_len(self):
        self.assertEqual(len(" "), 1, "Should be 1")
        self.assertEqual(len("test"), 4, "Should be 4")
        self.assertEqual(len([1, 2, 3, 4, 5]), 5, "Should be 5")


# Initialize unittest
if __name__ == '__main__':
    unittest.main()