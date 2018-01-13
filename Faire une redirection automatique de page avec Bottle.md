# Faire une redirection automatique de page avec bottle.  

L'algorithme ci dessous demande un mot de passe à l'utilisateur. Si le mot de passe est correcte, la page `/login` renvoie le message "identification correcte" . Dans le cas contraire, l'utilisateur est automatiquement redirigé vers la page d'accueil à la racine du site `/`.  

	from bottle import *
	
	@route('/')
	def index():
	
		formulaire = """	<form action="/login" method="post"> Mot de
		passe: <input name = "mdp" type = "password" />  <input value="Login" type="submit" /> 	</form>"""
	
		return formulaire
	
	
	@post('/login')
	def login():
	
		mot = request.forms.get('mdp')
	
		if mot == 'csmh2016':
			return 'identification correcte'
	
		else:
			response.status = 303
			response.set_header('Location', '/')
			
			
	run(host='localhost', port=27200, reload=True, debug=True)

La redirection consiste à générer une erreur de type 303 et à préciser l'adresse de la redirection.  (Ici la route est `/`)

	response.status = 303
	response.set_header('Location', '/')
