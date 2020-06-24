import unittest
import class1

class Test_test1(unittest.TestCase):
    def test_1(self):
       expError = 'R'
       expResult = []
       a = 0
       b = 0
       c = 0
       actError, actResult = class1.Yravnenie(a, b, c)
       self.assertEqual(expError, actError)
       self.assertEqual(len(expResult), len(actResult))
    def test_2(self):
        expError = "Нет корней"
        expResult = []
        a = 0
        b = 0
        c = 7
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение об ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
    def test_3(self):
        expError = ""
        expResult = [ -0.5 ]
        a = 0
        b = 2
        c = 1
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение об ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
        self.assertEqual(expResult[0], actResult[0])
    def test_4(self):
        expError = "Нет корней"
        expResult = []
        a = 1
        b = 4
        c = 25
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение об ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
    def test_5(self):
        expError = ""
        expResult = [ 1 ]
        a = 4
        b = -8
        c = 4
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение об ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
        self.assertEqual(expResult[0], actResult[0])
    def test_6(self):
        expError = ""
        expResult = [ 2, 1 ]
        a = 1
        b = -3
        c = 2
        actError, actResult = class1.Yravnenie(a, b, c)
        self.assertEqual(expError, actError, "Полученное сообщение ошибке (" + actError + ") не совпадает с ожидаемым" + expError)
        self.assertEqual(len(expResult), len(actResult))
        self.assertEqual(expResult[0], actResult[0])
        self.assertEqual(expResult[1], actResult[1])
        

if __name__ == '__main__':
    unittest.main()

