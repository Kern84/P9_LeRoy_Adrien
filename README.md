Projet 9

LITReview

1 - Configuration pour execution du programme.

Le programme a été concu avec Python 3.10.

Téléchargez le dossier du projet sur GitHub : https://github.com/Kern84/P9_LeRoy_Adrien.git


Entrez les lignes de commandes dans votre terminal.

Placez vous dans le dossier du projet, installez et activez l'environnement virtuel:
python3 -m venv env
source env/bin/activate

Installez les packages nécessaires au fonctionnement du projet:
pip install -r requirements.txt

Placez vous dans le dossier litreview pour lancer le serveur:
python3 manage.py runserver

Vous pouvez maintenant vous rendre sur l'adresse local du site:
http://127.0.0.1:8000

Désactiver l'environnement virtuel, quand vous avez fini de consulter le projet:
deactivate


2 - Utilisateurs

Des utilisateurs ont déjà été créé avec des posts et des abonnements pour chacuns.

utilisateur 1 = adrien, mot de passe = S3cret!1
utilisateur 2 = michel, mot de passe = S3cret!2
utilisateur 3 et superuser = toto, mot de passe = toto


3 - Utilisation du site

Lorsque vous cliquez sur le lien du site il vous est possible de créer un nouvel utilisateur ou de vous connecter avec un utilisateur existant.

Une fois connecté, vous arrivez sur la page du Flux de l'utilisateur, vous pourrez y voir vos posts, les posts des personnes que vous suivez ainsi que les réponses à vos posts même si vous ne suivez pas la personne qui a répondu.
Sur toutes les pages du site il vous est possible de faire une demande ou rédiger une critique.

Dans l'onglet Posts, vous trouverez tous vos posts afin de les modifier ou supprimer.

Dans l'onglet Abonnements, vous pourrez vous abonner à d'autres utilisateurs, voir à qui vous êtes abonné et qui vous suit.

Dans l'onglet Changer de mot de passe, vous pourrez changer votre mot de passe (incroyable).

Enfin, vous avez un onglet Se déconnecter qui vous permettra de fermer votre session et vous rammener à la page de connexion.