from valida_senha import valida_senha
import unittest

class TesteSenha(unittest.TestCase):
    
    def vazio(self):
        self.assertEqual(valida_senha(''), -1)
    
    def senha_espaço(self):
        self.assertEqual(valida_senha('senha teste'), 1)
    
    def teste_senha_fraca(self):
        self.assertEqual(valida_senha('senhaT'), 0)
    
    def teste_senha_media(self):
        self.assertEqual(valida_senha('Senha0M'), 1)
    
    def teste_senha_forte(self):
        self.assertEqual(valida_senha('Senha0M@123'), 2)

if __name__ == "__main__":
    unittest.main()