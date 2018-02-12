# Géstion des cookies avec Bottle

Les cookies permettent de stocker et de récupérer des informations directement dans et depuis le navigateur du client.

### Envoyer un cookie:

	response.set_cookie("account", "Djibril", secret='hgcghgfygfytfftyf')

- "account" est le nom de mon cookie
- "Djibril" est le contenu de mon cookie (⚠️ le contenu est limité à 4ko)
- secret est une phrase passe qui permet de signer le cookie, afin d’en  vérifier son authenticité.


### Récupérer un cookie (si il existe !)

	x = request.get_cookie("account", secret='hgcghgfygfytfftyf')

Si le cookie recherché n’est pas présent dans le navigateur du client, x serra égale à None.

### Supprimer un cookie:

	response.set_cookie("account", '' ,secret='hgcghgfygfytfftyf',expires=0)

Il faut envoyer un nouveau cookie du même nom, et le faire expirer immédiatement :
expires = 0 signifie que le cookie expire au timestamp 0 (soit le 1 janvier 1970)

On peut aussi utiliser max_age = 0 (expire dans 0 secondes)


### Exemple basique d’utilisation :

	from bottle import *
	
	app = Bottle()
	
	@app.route('/' , method = ('POST','GET'))
	def index():
	
		x = request.get_cookie("account", secret='hgcghgfygfytfftyf')
		
		if x:
			
			p = 'bonjour ' + str(x)
			d = """<form action="/log_out" method="post"> <input type="submit" name="info" value="deconnection"/> </form>"""
		
			return p , d
			
		else:
			f = """	<form action="/login" method="post"> 
			Nom : <input name='nom' type='text' />
			Password : <input name="mdp" type="password" /> 
			<input value="Login" type="submit" /> 	</form>"""
			
			return f
	
	
	
	
	@app.post('/login')
	def login():
	
		password = request.forms.get('mdp')
		nom = request.forms.get('nom')
		passref = 'csmh'
		
		if password == passref:
			
			response.set_cookie("account", nom, secret='hgcghgfygfytfftyf')
			
			response.status = 303
			response.set_header('Location', '/')
			
		else:
			
			t = 'mot de passe incorrecte'
			b = """<form action="/" method="post"> <input type="submit" name="info" value="acceuil"/> </form>"""
			
			return t , b
		
	
	
	
	@app.post('/log_out')	
	def deconect():
	
		response.set_cookie("account", '' ,
		secret='hgcghgfygfytfftyf',expires=0)
	
		response.status = 303
		response.set_header('Location', '/')
	
	
	
	
	
	app.run(host='localhost', port=27200, reload=True, debug=True)
