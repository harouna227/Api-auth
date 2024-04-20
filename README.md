## API POUR UN SYSTEME D'AUTHENTIFICATION
Ce API REST du système d'authentification est conçu avec Django, Django Rest Framework, Djoser, rest_framework_simplejwt et drf_yasg(utilisation du paramètre swagger) pour le plaisir de programmer et dans le cadre de l'apprentisage.



## LES ROUTES IMPLEMENTEES
| METHODES | ROUTES | FONCTIONALITES |
| ------- | ----- | ------------- | 
| *POST* | ```/auth/jwt/create/``` | _Connecter un user_|
| *POST* | ```/auth/jwt/refresh/``` | _Actualiser le jeton d'accès_|
| *POST* | ```/auth/jwt/verify/``` | _Verifier la validité du jeton_|
| *GET* | ```/users/``` | _Lister les users_|
| *POST* | ```/users/``` | _Créer un user_|
| *POST* | ```/users/activation/``` | _Activer le compte user_|
| *GET* | ```/users/me/``` | _Lecture seule_|
| *PUT* | ```/users/me/``` | _Mis à jour_|
| *PATCH* | ```/users/me/``` | _Mis à jour partiel_|
| *DELETE* | ```/users/me/``` | _Supprimer users_|
| *POST* | ```/user/resend_activation/``` | _Renvoyer le lien d'activation si pas reçu_|
| *POST* | ```/user/reset_email/``` | _Reinitialiser votre email_|
| *POST* | ```/users/reset_email_confirm/``` | _Confirmer lien de reinitialisation de l'email_|
| *POST* | ```/users/reset_password/``` | _Reinitialiser le mot de passe_|
| *POST* | ```/users/reset_password_confirm/``` | _Confirmer lien de reinitialisation de mot de passe_|
| *POST* | ```/users/set_email``` | _Changer d'email_|
| *POST* | ```/users/set_password/``` | _Changer de mot de passe_|
| *GET* | ```/users/{id}/``` | _Obtenir un user en utilisant son id_|
| *PUT* | ```/users/{id}/``` | _Mis à jour user en utilisant son id_|
| *PATCH* | ```/users/{id}/``` | _Mis à jour partiel user en utilisant son id_|
| *DELETE* | ```/users/{id}``` | _Supprimer un user en utilisant son id_|
| *GET* | ```/docs/``` | _Afficher la documentation de l'API_|

## Comment Installer et Demarrer ce projet?

### Pre-requis:
1. Installer Git
[ https://git-scm.com/ ]

2. Installer Python Derniére Version
[ https://www.python.org/downloads/ ]

### Installation
**1. Créer un dossier dans lequel vous souhaitez enregistrer le projet**

**2. Créer un environnement virtuel et activez**
Ouvre ce dossier dans ton éditeur de Code
Allez-y dans votre terminal gitbash

Installer l'Environnement Virtuel
```
pip install virtualenv
```

Création de l'Environnement virtuel:
Sur Window
```
python -m venv .env
```
Sur Mac
```
python3 -m venv .env
```

Activation de l'Environnement Virtuel

Sur Windows
```
source .env/scripts/activate
```

Sur Mac
```
source .env/bin/activate
```

**3. Cloner le projet**
```
git clone https://github.com/harouna227/Api-auth.git
```
Une fois cloné, rentrer dans le dossier src
```
cd src
```

**4. Installer les exigences dépuis 'requirements.txt'**
```
pip install -r requirements.txt
```
**5. Congiguration d'envoi d'email par SMTP lors de restauration de mot de passe**

Vous pouvez configurer ça aussi, aprés le demarrage du Serveur

- Allez-y dans le fichier settings.py se trouvant dans le dossier core
- A la variable **EMAIL_HOST_USER** affecter votre mail configuré sur votre compte google pour test. Mettez un email fonctionnel.
- A la variable **EMAIL_HOST_PASSWORD** affecter le mot de passe générer au niveau de votre compte google

Vous pouvez aussi faire une configuration locale d'envoi d'email avec MAILHOC.

**6. Idenfiant de Connexion**

Créer un Super utiliseur (Admin)

Sur Windows:
```
python manage.py createsuperuser
```
Sur MAC:
```
python3 manage.py createsuperuser
```
Ensuite ajouter Usename, Email, et mot de passe

### Demarrage
**1.  Maintenant demarrer le Serveur**

Sur Windows:
```
python manage.py runserver
```

Sur Mac:
```
python3 manage.py runserver
```
**2. Copier et Caller l'Addresse locale sur laquelle le serveur est demarragée dans votre navigateur**

```
http://127.0.0.1:8000/
```

**3. Connexion à la page Admin avec ses indentifiants**
```
http://127.0.0.1:8000/admin/
```