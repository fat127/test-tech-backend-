# Démarrer le Backend (villa_app)

## Naviguer dans le dossier villa_app

1. **Ouvrir un terminal ou utiliser celui intégré à votre IDE**.
2. Tapez la commande suivante :
   ```sh
   cd "chemin/vers/test-tech-backend/villa_app"
   ```

## Créer un environnement virtuel (si non fait)

### Sous Windows :
1. Créez l'environnement virtuel :
   ```sh
   python -m venv myvenv
   ```
2. Activez-le :
   ```sh
   myvenv\Scripts\activate
   ```

### Sous Linux/Mac :
1. Créez l'environnement virtuel :
   ```sh
   python3 -m venv myvenv
   ```
2. Activez-le :
   ```sh
   source myvenv/bin/activate
   ```



## Appliquer les migrations (si nécessaire)

1. Générez les migrations :
   ```sh
   python manage.py makemigrations
   ```
2. Appliquez les migrations :
   ```sh
   python manage.py migrate
   ```

## Lancer le serveur Django

1. Exécutez la commande :
   ```sh
   python manage.py runserver
   ```
2. Accédez au backend via [http://localhost:8000](http://localhost:8000).

