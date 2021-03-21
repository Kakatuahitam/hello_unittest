#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:54:08 2021

@author: kakatuahitam
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 22:53:07 2021

@author: 
    Yuda Kurnia Nurul Fikri   11180910000073  github.com/Kakatuahitam
    Rima Adriani              11180910000088  github.com/rimaadriani
    Aliandra Akram            11180910000094  github.com/aliandraakram
"""

from simplecalc import *
import unittest

class Test_SimpleCalc(unittest.TestCase):
    def test_tambah(self):
        test_a = 78
        test_b = 54
        expected = 132
        self.assertEqual(tambah(test_a, test_b),expected)
    
    def test_kurang(self):
        test_a = 78
        test_b = 54
        expected = 24
        self.assertEqual(kurang(test_a, test_b),expected)
        
    def test_kali(self):
        test_a = 78
        test_b = 54
        expected = 4212
        self.assertEqual(kali(test_a, test_b),expected)
        
    def test_bagi(self):
        test_a = 78
        test_b = 54
        expected = 1.4444444444444444
        self.assertEqual(bagi(test_a, test_b),expected)
        
    def test_pangkat(self):  
        test_a = 78
        test_b = 4
        expected = 37015056
        self.assertEqual(pangkat(test_a, test_b),expected)
        
unittest.main()
