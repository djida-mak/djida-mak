import unittest
from IAs.intermediaire import Intermediaire
class TestIntermediare(unittest.TestCase):
    def test_get_distance(self):
        self.i.get_distance()
    def test_get_angle(self):
        self.i.get_angle()
    def test_tourner_gauche(self):
        self.i.tourner_gauche(40)
    def test_tourner_droite(self):
        self.i.tourner_droite(54)
    def test_avancer(self):
        self.i.avancer(30,50)