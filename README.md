# td-djangorestapi-GUILLET-SIMON
TP Django RESTAPI

## Installation

### Prérequis

- Python 3.8
- Pip
- Un serveur MySQL (ex: [Laragon](https://laragon.org/download/))

### Installation de l'environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Linux
```

### Configuration de la base de données
    
Créer une base de données MySQL nommée `suivi_recherche`.
```sql
CREATE DATABASE suivi_recherche;
```

Créer un fichier `.env` à la racine du projet avec les informations de connexion à la base de données.
Le fichier `.env.example` est fourni en exemple.
```env
DB_NAME=suivi_recherche
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

### Installation des dépendances

```bash
pip install --no-cache-dir -r requirements.txt
```

### Lancement des migrations

```bash
python manage.py migrate
```

## Utilisation

### Lancement du serveur

```bash
python manage.py runserver
```

### Création d'un super utilisateur

```bash
python manage.py createsuperuser
```

### Création d'un token pour un utilisateur

```bash
python manage.py drf_create_token <username>
```

### Ajouter le token d'accès à l'API dans le fichier `.env`

```env
API_TOKEN=f8f0d32f6d47cbc3f766b5eede8a453d63e4ddcb
```

### Configuration des tests

- Installer l'extension [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) pour Visual Studio Code.
- Créer un fichier `.vscode/settings.json` à la racine du projet avec les informations suivantes :
```json
{
    "rest-client.environmentVariables": {
        "$shared": {
            "baseUrl": "http://localhost:8000/api",
            "token": "<token>"
        },
    }
}
```


### Accès

- Le site : [http://127.0.0.1:8000/](http://127.0.1:8000/)
- Le panel d'adminitration : [http://127.0.0.1:8000/admin/](http://127.0.1:8000/admin/)
- L'API : [http://127.0.0.1:8000/api/](http://127.0.1:8000/api/)
- La documentation : [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)
- Le Swagger : [http://127.0.0.1:8000/api/schema/](http://127.0.1:8000/api/schema/)

