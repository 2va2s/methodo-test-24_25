import unittest
from unittest.mock import patch
from src.main import process_input

import datetime

class TestFunctions(unittest.TestCase):

    def test_bonjour(self):
        # Teste le terme "Bonjour" avant midi avec un mot non-palindrome
        now = datetime.datetime(2023, 10, 10, 9, 0, 0)  # Matin
        response, should_exit = process_input("hello", now)
        self.assertNotIn("exit", response)
        self.assertFalse(should_exit)  # Doit pas quitter le programme
        self.assertEqual(response, "olleh")  # Retour miroir attendu

    def test_bien_joue(self):
        # Teste le retour "Bien joué" pour un palindrome
        now = datetime.datetime(2023, 10, 10, 14, 0, 0)  # Après-midi
        response, should_exit = process_input("kayak", now)
        self.assertNotIn("exit", response)
        self.assertFalse(should_exit)  # Doit pas quitter le programme
        self.assertEqual(response, "Bien joué")

    def test_au_revoir(self):
        # Liste des cas pour "Au revoir"
        cas = [
            {"heure": 8, "attendu": "Bonjour"},
            {"heure": 15, "attendu": "Bonne après-midi"},
            {"heure": 20, "attendu": "Bonsoir"},
        ]

        for c in cas:
            with self.subTest(heure=c["heure"], attendu=c["attendu"]):
                now = datetime.datetime(2023, 10, 10, c["heure"], 0, 0)
                response, should_exit = process_input("exit", now)
                self.assertIn(c["attendu"], response)  # Vérifie le bon terme
                self.assertTrue(should_exit)  # Doit quitter le programme

    def test_retour_miroir(self):
        # Teste que les mots non-palindromes retournent leur miroir
        cas = [
            {"input": "world", "attendu": "dlrow"},
            {"input": "hello world", "attendu": "dlrowolleh"},
        ]

        for c in cas:
            with self.subTest(input=c["input"], attendu=c["attendu"]):
                now = datetime.datetime(2023, 10, 10, 11, 0, 0)  # Matin
                response, should_exit = process_input(c["input"], now)
                self.assertEqual(response, c["attendu"])  # Vérifie le retour miroir
                self.assertFalse(should_exit)  # Doit pas quitter le programme

    def test_invalid_input(self):
        # Teste les entrées invalides
        cas = [
            {"input": "12345", "attendu": "Je n'accepte que des mots en entrée"},
            {"input": "hello!", "attendu": "Je n'accepte que des mots en entrée"},
        ]

        for c in cas:
            with self.subTest(input=c["input"], attendu=c["attendu"]):
                now = datetime.datetime(2023, 10, 10, 16, 0, 0)  # Après-midi
                response, should_exit = process_input(c["input"], now)
                self.assertEqual(response, c["attendu"])  # Vérifie le message d'erreur
                self.assertFalse(should_exit)  # Doit pas quitter le programme


if __name__ == '__main__':
    unittest.main()