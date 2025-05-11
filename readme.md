Projet 3DVP - API REST avec FastAPI
Description
Ce projet est une implémentation d'une API REST en Python utilisant FastAPI, réalisée dans le cadre du TP 3DVP de l'école IT. L'API gère une liste d'items avec des opérations CRUD (Create, Read, Update, Delete) et inclut une pipeline CI/CD avec GitHub Actions pour l'automatisation des tests et du linting. Le déploiement a été configuré manuellement sur Render.
Fonctionnalités

Endpoints :
GET / : Retourne un message de statut ("API en ligne").
GET /items : Liste tous les items.
GET /items/{item_id} : Affiche un item spécifique.
POST /items : Crée un nouvel item.
PUT /items/{item_id} : Met à jour un item.
DELETE /items/{item_id} : Supprime un item.


Modèle Item : id (int), name (str), price (float), in_stock (bool).

Prérequis

Python 3.12
Pip (gestionnaire de paquets Python)
Git (pour le versioning)

Installation

Clonez le dépôt :git clone https://github.com/neylie100/Devops.git

cd DevOps


Créez un environnement virtuel :python -m venv env


Activez l'environnement virtuel :
Windows : env\Scripts\activate

Installez les dépendances :pip install -r requirements.txt


Lancez l'API localement :uvicorn main:app --reload

L'API sera accessible à http://localhost:8000/docs

Tests

Exécutez les tests unitaires :pytest


Vérifiez la qualité du code :flake8 . 


Pipeline CI/CD

Configurée avec GitHub Actions dans .github/workflows/ci.yml.
Étapes :
Linting avec flake8.
Exécution des tests avec pytest.


Déploiement

API déployée manuellement sur Render

 URL de l’API : https://devops-lpes.onrender.com
Étapes de déploiement :
Connecter votre compte GitHub à Render

Créer un Nouveau Web Service

Sélectionner le dépôt GitHub → branche main

Définir :

Runtime : Python

Build command : pip install -r requirements.txt

Start command : uvicorn main:app --host 0.0.0.0 --port 10000

Lancer le déploiement

Bonus

Captures d'écran

API en ligne : [img/api.png].
Render : [img/Deploiement1.png,img/Deploiement2.png,img/Deploiement3.png].

Structure du projet
3DVP_ndjumkeng_nguemo_neylie/
│
├── __pycache__/
├── .github/
├── .pytest_cache/
├── configuration/
├── modele/
├── paths/
├── schema/
├── tests/
├── venv_devops/          # Environnement virtuel (à éviter de versionner)
│
├── main.py               # Point d'entrée principal de l'application
├── readme.md             # Description du projet
├── requirements.txt      # Liste des dépendances Python

Réalisé par : stella nguemo



