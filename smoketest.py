#  Este archivo contendra el Test Suite

from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertion import AssertionTest
from search_tests import SearchTests

assertion_test = TestLoader().loadTestsFromTestCase(AssertionTest)  # Este contendra la Clase de prueba
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

# Se procede a construir nuestra suit de prueba atravez del codigo
smoke_test = TestSuite([assertion_test, search_test])

# para generar los reporters (Diccionario)
kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
