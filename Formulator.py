import sys

class Form:
	
	
	def __init__(self):
		
		self.btn_link = """
	border:none;
	outline:none;
	background:none;
	cursor:pointer;
	color:#0000EE;
	padding:0;
	text-decoration:underline;
	font-family:inherit;
	font-size:inherit;
	"""
	
		self.lienblanc = """
	border:none;
	outline:none;
	background:none;
	cursor:pointer;
	color:#FAF0E6;
	padding:0;
	text-decoration:underline;
	font-family:inherit;
	font-size:inherit;
	"""
		
		self.iconecss = """
	background-image:url("/img/opo.gif");
	top right no-repeat;
	width: 16px;
	height: 16px;
	padding: 0 0 0 10px;
	border-width: 0px;
	background-color:#ffffff;
	cursor: pointer;
	border:0;
	"""
		
		self.icone = """
	border-width: 0px;
	background-color:#ffffff;
	"""
		
		
	#formulaires automatiques	
		
	def formulaire(self, action = '/', method = 'post', value = 'send', *txt, **name_type):
		
		"""La liste txt contient les textes associés au chanps
		Le dico name_type contient les noms des champs et leur type
		
		Attention ca ne marche que en 3.6, pour les versions inferieures, le dico n’est pas dans le meme ordre que txt !!!
		"""
		
		k = name_type.keys()
		
		q = " ".join(["""{t}: <input name = "{n}" type = "{ty}" />""".format(t = i, n = j, ty = name_type[j])for i , j in zip(txt, k)])

		f = """<form action="{0}" method="{1}"> {2} <input value = "{3}" type="submit" />   </form>""".format(action, method, q, value)
		
		return f
		
	def text(self, action, method, label, titre, name, bouton, value, rows=5, cols=10):
		
		return """<form method="{method}" action="{action}" accept-charset="Windows-1256"><p><label for="{label}">{titre}</label><br/><textarea name="{name}" id="{name}" rows="{rows}" cols="{cols}" wrap="virtual">{value}</textarea></p><input type="submit" value="{bouton}"/></form>""".format(action=action, method=method, label=label, titre=titre, name=name, bouton=bouton, value=value, rows=rows, cols=cols)
		
	
		
	#boutons automatiques			
		
	def boutimp(self, action, method, name, value, classe = ''):
		
		return """<form action = "{0}" method = "{1}"> <input type = "submit" name = "{2}" value = "{3}" style = "{4}"/> </form>""".format(action, method, name, value, classe)
		
		
	def bouton(self, action, method, name, value, txt, classe = ''):
		
		return """<form action="{0}" method="{1}" accept-charset="Windows-1256"> <button type="submit" name="{2}" value="{3}" style = "{5}" >{4}</button></form>""".format(action, method, name, value, txt, classe)
		
	def bouton_lien(self, action, method, name, value, txt):
		
		return """<form action="{0}" method="{1}"> <button type="submit" name="{2}" value="{3}" style = "{5}" >{4}</button></form>""".format(action, method, name, value, txt, self.btn_link)
		
	def bouton_lienb(self, action, method, name, value, txt):
		
		return """<form action="{0}" method="{1}"> <button type="submit" name="{2}" value="{3}" style = "{5}" >{4}</button></form>""".format(action, method, name, value, txt, self.lienblanc)
	
	
	
	
	#liste deroulante automatique
	
	def listder(self, action, method, name, label, classe = '', bout = 'Envoyer', **value_txt):
		
		"""le dico value_txt associe les noms des champs de la liste au text des champs de la liste.
		Attention:
			
			en python3.6 les champs sont dans l'ordre du dico
			en python<3.6 les chanps sont dans l'ordre alphabetique
		"""
		
		k = value_txt.keys()
		
		if sys.version_info < (3,6):
			
			k = sorted(k)
		
		q = " ".join(["""<option value="{v}">{t}</option>""".format(v = i, t = value_txt[i]) for i in k])
		
		#return """<form action="{0}" method="{1}"><label for="{3}">{2}</label><select name="{2}" class="{4}">{q}</select><input type="submit" value="{5}"/></form>""".format(action, method, name, label, classe, bout, q=q)
	
		return """<form action="{0}" method="{1}"><label for="{3}">{3}</label><select name="{2}" class="{4}">{q}</select><input type="submit" value="{5}"/></form>""".format(action, method, name, label, classe, bout, q=q)
	
			
							
	#cases automatiques
					
	def case(self, action, method, txt, value, **namevalue):

		x = " ".join(["""<input type="checkbox" name="{n}" value="{m} id="{n}" /> <label for="{n}">{m}</label><br/>""".format(n = i, m = namevalue[i]) for i in namevalue.keys()])
	
		return """<form action="{0}" method="{1}"> {2} <br/> {3} <input value="{4}" type="submit" /> </form>""".format(action, method, txt, x, value)
		
		
	
		
