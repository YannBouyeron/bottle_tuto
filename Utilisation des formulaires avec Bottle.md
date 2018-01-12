Utilisation des formulaires avec Bottle


Un formulaire permet à l'utilisateur (le navigateur internet) d'envoyer des informations à l'application web (le serveur).

## Créer un formulaire
Le formulaire ci dessous contient deux champs: un champ pour le nom, et un autre champ pour l'e-mail.


    from bottle import *
    
    app = Bottle()
    
    @app.route('/')
    def page_index():
	
		mon_formulaire = """	
    	<form action="/login" method="post"> 
		Nom: <input name="username" type="text" /> 
		Email: <input name="mail" type="email" /> 
		<input value="Login" type="submit" /> 	</form>"""
		
		return mon_formulaire
	
    app.run(host='localhost', port=27200, reload=True, debug=True)
   
Examinons plus en détails ce formulaire:

    <form action="/login" method="post"> 

On définit ici une action: /login , cela signifie que les données entrées dans le formulaire sont renvoyées vers la page /login.
On définit une methode: post , c'est la méthode généralement utilisée pour envoyer un formulaire, elle permet de "cacher" les informations du formulaire lors de l'envoi. Une autre méthode existe, c'est la méthode dite get, avec cette méthode les informations du formulaire sont visibles dans l'adresse de la page.

    Nom: <input name="username" type="text" /> 

On definit ici un premier champ du formulaire, c'est le champ Nom. La valeur entrée dans ce champ par l'utilisateur sera affectée à la variable nommée username. Ce champ est de type text (d'autres types de données peuvent être entrées dans un formulaire: type password, type email...)  

    <input value="Login" type="submit" /> 	</form>"""

On définit ici la dénomination du bouton d'envoi du formulaire : Login.


## Récupérer les données du formulaire

Pour récupérer les données du formulaire il nous faut créer une page /login .
Les données du formulaire ayant été envoyées avec la méthode post, la route de cette page pourra s'écrire de différentes façons:

    @app.route('/login' , method = 'POST')
   
Ou plus simplement:

    @app.post('/login')

Il faut ensuite récupérer les données du formulaire grâce à la fonction request:

    nom = request.forms.get('username')


Le code complet de notre page /login :

    @app.post('/login')
    def login():
	
		nom = request.forms.get('username')
		email = request.forms.get('mail')
	
		mon_texte = 'bonjour ' + nom + ' votre adresse mail est: ' + email
	
		return mon_texte


## Le code complet de l'application  

   
    from bottle import *
    
    app = Bottle()
    
    @app.route('/')
    def page_index():
	
		mon_formulaire = """	
    	<form action="/login" method="post"> 
		Nom: <input name="username" type="text" /> 
		Email: <input name="mail" type="email" /> 
		<input value="Login" type="submit" /> 	</form>"""
		
		return mon_formulaire
    
    @app.post('/login')
    def login():
	
		nom = request.forms.get('username')
		email = request.forms.get('mail')
	
		mon_texte = 'bonjour ' + nom + ' votre adresse mail est: ' + email
	
		return mon_texte
	
    app.run(host='localhost', port=27200, reload=True, debug=True)
   

## Renvoyer des données à une même adresse mais avec une route différente  

Dans l'exemple ci dessous en accède au formulaire de la page  '/ ' par la méthode get grâce une route get:

    @app.route('/')
   
On ne précise pas ici la méthode qui est de toutes façons de type get par défaut 

Ou alors :

    @app.get('/')

On récupère les données du formulaire à la même adresse (' / ') mais avec une route post:

    @app.post('/')
   

Le code complet:

  
    from bottle import *
    
    app = Bottle()
    
    @app.get('/')
    def page_index():
	
		mon_formulaire = """	
    	<form action="/" method="post"> 
		Nom: <input name="username" type="text" /> 
		Email: <input name="mail" type="email" /> 
		<input value="Login" type="submit" /> 	</form>"""
		
		return mon_formulaire
    
    @app.post('/')
    def login():
	
		nom = request.forms.get('username')
		email = request.forms.get('mail')
	
		mon_texte = 'bonjour ' + nom + ' votre adresse mail est: ' + email
	
		return mon_texte
	
    app.run(host='localhost', port=27200, reload=True, debug=True)
   
Ce qui équivaut au code suivant plus court:

   
    from bottle import *
    
    app = Bottle()
    
    @app.route('/', method = ('POST','GET'))
    def page_index():
	
	if request.method == 'GET':
		
		mon_formulaire = """	<form action="/" method="post"> 
		Nom: <input name="username" type="text" /> 
		Email: <input name="mail" type="email" /> 
		<input value="Login" type="submit" /> 	</form>"""
		
		return mon_formulaire
		
	if request.method == 'POST':
	
		nom = request.forms.get('username')
		email = request.forms.get('mail')
	
		mon_texte = 'bonjour ' + nom + ' votre adresse mail est: ' + email
	
		return mon_texte
	
    app.run(host='localhost', port=27200, reload=True, debug=True)
