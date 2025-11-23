# ue19-lab-05

Cette application interroge l'API publique **JokeAPI** et affiche une blague aléatoire.

# Installation

1. Cloner le repository : git clone https://github.com/Mohammad-git340/ue19-lab-05

2. Installer les dépendances : pip install -r requirements.txt
3.  Pour lancer l'application : python3 app.py
# Exécution avec Docker

1. Construire l'image : docker build -t jokes-app .
2. Lancer le conteneur : docker run jokes-app

Cette application utilise **JokeAPI** :  
https://v2.jokeapi.dev/

L’API retourne soit :
- une blague simple (`type: "single"`)
- une blague en deux parties (`setup` + `delivery`)
