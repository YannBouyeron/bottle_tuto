# coding: utf-8
from bottle import *

app = Bottle()

@app.route('/' , method = ('POST','GET'))
def index():
	
	x = request.get_cookie("account", secret='password2427')
	
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
		
		response.set_cookie("account", nom, secret='password2427')
		
		response.status = 303
		response.set_header('Location', '/')
		
	else:
		
		t = 'mot de passe incorrecte'
		b = """<form action="/" method="post"> <input type="submit" name="info" value="acceuil"/> </form>"""
		
		return t , b
		
	
	
	
@app.post('/log_out')	
def deconect():
	
	response.set_cookie("account", '' , secret='password2427',expires=0)
	
	response.status = 303
	response.set_header('Location', '/')
	
	
	
	
	
app.run(host='localhost', port=27200, reload=True, debug=True)
