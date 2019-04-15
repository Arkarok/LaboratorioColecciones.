import unittest
import statistics
from custom_functions import temperature_methods

class Test_OMN(unittest.TestCase):

    def test_calculate_prom(self):
        departamento=[31,34,35,34,33,33,32,34,32,35,36,33]
        prom=temperature_methods.promedio_temperature(departamento)
        self.assertEqual(prom,33.5)


    def test_calculate_cal(self):
        departamento_1=[31,34,35,34,33,33,32,34,32,35,36,33]
        cal_1=temperature_methods.temperature_best(departamento_1)
        self.assertEqual(cal_1,36)

    def test_desviacion_estandar(self):
        departamento_2=[31,34,35,34,33,33,32,34,32,35,36,33]
        s=statistics.stdev(departamento_2)
        self.assertEqual(s,1.4459976109624424)


if __name__ == '__main__':
    unittest.main()
