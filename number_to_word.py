import unittest


numbers = {
    0 : " ",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}

teens = {
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fiveteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen"
}

tens = {
    2 : "twenty",
    3 : "thirty",
    4 : "fourty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety"
}


p = " pound"
t = "s"
def number_to_word(s):
        if not 1<= s <= 100:
            return "incorrect input"
        if s==1:
            return numbers[s] + p
        elif 1 < s <= 9:  # single digits
            return numbers[s] + p + t
        elif 10 <= s <= 19:
            return teens[s] + p + t
        elif s==100 :
            return "one hundred pounds"
        elif 20 <= s <= 99:
            single = s%10
            double = s//10
            return tens[double] + numbers[single] + p + t
            

class TestNumberToWords(unittest.TestCase):
    def test_1_return_one_pound(self):
        self.assertEqual(
        number_to_word(1),
        "one pound"
    )
    
    def test_2_return_error(self):
        self.assertEqual(
        number_to_word(0),
        "incorrect input"
    )
    def test_3_return_number2(self):
        self.assertEqual(
        number_to_word(2),
        "two pounds"
    ) 
    
    def test_4_return_teens(self):
        self.assertEqual(
        number_to_word(16),
        "sixteen pounds"
    ) 
    def test_5_return_tens(self):
        self.assertEqual(
        number_to_word(24),
        "twentyfour pounds"
    ) 
    def test_6_return_hundred(self):
        self.assertEqual(
        number_to_word(100),
        "one hundred pounds"
    ) 
    def test_7_return_neg(self):
        self.assertEqual(
        number_to_word(-87),
        "incorrect input"
    ) 
    def test_8_return_hundreds(self):
        self.assertEqual(
        number_to_word(124),
        "incorrect input"
    ) 
if __name__ == '__main__':
     unittest.main()
