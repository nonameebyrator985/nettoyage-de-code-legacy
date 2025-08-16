import unittest
from nettoyage_de_code_legacy.analyser import analyser


class TestAnalyser(unittest.TestCase):
    def test_analyser_non_existant_path(self):
        resultats = analyser('chemin/inexistant')
        self.assertIn("Le chemin 'chemin/inexistant' n'existe pas.", resultats)

    def test_analyser_code_obsolete(self):
        # Créez un fichier temporaire pour tester
        import tempfile
        chemin_temp = tempfile.mkdtemp()
        with open(os.path.join(chemin_temp, 'test_obsolete.py'), 'w') as f:
            f.write('print "Hello World"
import module')
        
        resultats = analyser(chemin_temp)
        self.assertIn("'test_obsolete.py' utilise une syntaxe obsolète.", resultats)
        self.assertIn("'test_obsolete.py' contient un module importé obsolète.", resultats)


if __name__ == '__main__':
    unittest.main()
