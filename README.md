Projet Python (Django)

E-Learning App


Une application web e-learning développée en utilisant Django. Cette application permet à différents types d'utilisateurs de se connecter et de gérer les cours et les inscriptions. Les différents types d'utilisateurs sont :
- Admin
- Teacher
- Student




Prérequis techniques
- Python 3.6 ou supérieur
- Django 4.2
- sqlparse 0.4.3
Installation
1. Clonez ce dépôt de code en utilisant la commande suivante :
	git clone (repo url)
2. Installez les dépendances requises :
	pip install -r requirements.txt
3. Configurez la base de données en exécutant les migrations :
	python manage.py migrate
4. Lancez l'application :
	python manage.py runserver
5. Accédez à l'application en ouvrant votre navigateur Web et en accédant à l'URL suivante :
	http://127.0.0.1:8000

Fonctionnalités


 Admin
- Peut consulter la liste des utilisateurs
- Peut supprimer des utilisateurs
- Peut consulter la liste des cours
- Peut supprimer des cours


Teacher
- Peut créer un nouveau cours
- Peut modifier un cours existant
- Peut consulter un cours
- Peut supprimer un cours
- Peut gérer les inscriptions aux cours


Student
- Peut s'inscrire à un cours
- Peut consulter la liste des cours
- Peut consulter les chapitres du cours


Contributions
Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez suivre les instructions suivantes :
1. Forkez le dépôt de code
2. Créez une branche pour vos modifications
3. Effectuez vos modifications
4. Faites un pull request en expliquant vos modifications
Crédits
Ce projet utilise les bibliothèques suivantes :
- Django (https://www.djangoproject.com/)
- Bootstrap (https://getbootstrap.com/)
- Javascript et JQuery


Project developed by
Youssef El moudene
Youssef Elyourizi
Amal Benattik


