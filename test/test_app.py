# Pruebas básicas
import unittest
from app import process_pdf

class TestApp(unittest.TestCase):
    def test_process_pdf(self):
        result = process_pdf("sample.pdf", {"use_plugins": False})
        self.assertIn("title", result)

if __name__ == "__main__":
    unittest.main()