# Web_lib

Projet api avec flask petite librairies (meme projet que **Flask_Bibliothèque**)

> CSS inclut pour plus de confort

## Fonctionnement

apres avoir compiler le fichier _app.py_ aller à l'adresse :
Chercher un livre par son **titre** ou **isbn**

Egalement le `Dockerfile` est présent ce qui permet d mettre ce projet dans un `CONTAINER`

Commande pour tester l'app avec docker:

```bash
sudo docker build -t <image_name> .
sudo docker run -t -i <image_name>
```
