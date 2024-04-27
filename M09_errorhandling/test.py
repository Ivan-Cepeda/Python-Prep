import herramientas as h
import unittest

class ProbandoMiClase(unittest.TestCase):
    
    def test_crear_objeto1(self):
        param = 'hola'
        self.assertRaises(ValueError, h.Herramientas, param)
        #self.failUnlessRaises(ValueError, h.Herramientas, param)

    def test_crear_objeto2(self):
        param = [1,2,2,5]
        h1 = h.Herramientas(param)
        self.assertEqual(h1.lista, param)

    def test_valor_modal(self):
        lis = [1,2,1,3]
        h1 = h.Herramientas(lis)
        moda, veces = h1.valor_modal(False)
        moda = [moda]
        moda.append(veces)
        resultado = [1, 2]
        self.assertEqual(moda, resultado)

    def test_verifica_primos1(self):
        lis = [2,3,8,10,13]
        h1 = h.Herramientas(lis)
        primos = h1.verifica_primo()
        primos_esperado = [True, True, False, False, True]
        self.assertEqual(primos, primos_esperado)

    def test_verifica_conversion1(self):
        lis = [2,3,8,10,13]
        h1 = h.Herramientas(lis)
        grados = h1.conversion_grados('celsius','farenheit')
        grados_esperado = [35.6, 37.4, 46.4, 50.0, 55.4]
        self.assertEqual(grados, grados_esperado)

    def test_verifica_factorial(self):
        lis = [2,3,8,10,13]
        h1 = h.Herramientas(lis)
        factorial = h1.factorial()
        factorial_esperado = [2, 6, 40320, 3628800, 6227020800]
        self.assertEqual(factorial, factorial_esperado)

print(unittest.main(argv=[''], verbosity=2, exit=False))