# Import des librairies
from unittest import TestCase, main
from fastapi.testclient import TestClient
from api import app
import os


# assertEqual(a, b) : Vérifie si a est égal à b.
# assertNotEqual(a, b) : Vérifie si a est différent de b.
        
# assertIn(a, b) : Vérifie si a est dans b.
# assertNotIn(a, b) : Vérifie si a n'est pas dans b.
        
# assertIs(a, b) : Vérifie si a est b.
# assertIsNot(a, b) : Vérifie si a n'est pas b.
        
# assertTrue(x) : Vérifie si x est vrai.
# assertFalse(x) : Vérifie si x est faux.
        
# assertIsNone(x) : Vérifie si x est None.
# assertIsNotNone(x) : Vérifie si x n'est pas None.
        
# assertIsInstance(a, b) : Vérifie si a est une instance de b.
# assertNotIsInstance(a, b) : Vérifie si a n'est pas une instance de b.
        
# assertRaises(exc, fun, *args, **kwargs) : Vérifie si fun(*args, **kwargs) lève une exception de type exc.
# assertRaisesRegex(exc, r, fun, *args, **kwargs) : Vérifie si fun(*args, **kwargs) lève une exception de type exc et dont le message correspond à l'expression régulière r.


# Tests unitaire de l'environnement de développement
class TestDev(TestCase):

        # Vérifie que les fichiers sont présents
    def test_files(self):
        # Obtenez la liste des fichiers dans le répertoire actuel
        list_files = os.listdir()

        # Définissez les fichiers attendus dans votre projet
        expected_files = ["main.py", "config.yaml", ".gitignore", "requirements.txt"]

        # Utilisez l'assertion assertIn pour vérifier chaque fichier attendu
        for expected_file in expected_files:
            self.assertIn(expected_file, list_files, f"Le fichier {expected_file} est manquant.")


        # Vérifie que les requirements sont présents
    # Vérifie que les requirements sont présents
    def test_requirements(self):
        print(os.path.isfile("requirements.txt"))  # Ajoutez cette ligne pour déboguer
        # Utilisez l'assertion assertFalse pour vérifier que le fichier requirements.txt est vide
        self.assertFalse(os.path.getsize("requirements.txt") > 0, "Le fichier requirements.txt ne devrait pas contenir de dépendances.")

    # Vérifie que le gitignore est présent
    def test_gitignore(self):
        # Utilisez l'assertion assertTrue pour vérifier que le fichier .gitignore est présent et non vide
        self.assertTrue(os.path.isfile(".gitignore") and os.path.getsize(".gitignore") > 0, "Le fichier .gitignore est manquant ou vide.")

    

# Création du client de test

# Tests unitaire de l'API
    
    # Vérifie que l'API est bien lancée

    # Vérifie que l'API est bien lancée
    

    # Vérifie le endpoint hello_you
    

    # Vérifie le endpoint predict



# Test du modèle individuellement
#class TestModel(TestCase):

    # Vérifie que le modèle est bien présent
    

    # Vérifie que le modèle est bien chargé
    

    # Vérifie que le modèle est bien chargé
    

# Démarrage des tests
if __name__== "__main__" :
    main(
        verbosity=2,
    )
