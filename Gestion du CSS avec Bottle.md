# Gestion du CSS avec bottle.
### Lien HTML statique / CSS.
Vous savez déjà lier un fichier CSS à une page HTML statistique; on ajoute la balise `<link rel="stylesheet" href="style.css" />` entre les balises `<head>` et `</head>` .

Le fichier HTML (nommé index.html):


    <!doctype html>
    <html>
    
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="style.css" />
		<title>index</title>
	</head>
	
	<body>
		<h1>Bienvenue sur mon site</h1>
		<p>blablabla</p>
	</body>
    </html>
  
Le fichier CSS lié à cette page HTML est nommé "style.css" et se trouve dans le même dossier que la page HTML L'arborescence des 
dossiers et fichiers:
    – dossier mon_site
         – fichier index.html
         – fichier style.css
	 
### Lien HTML / CSS avec bottle.
Le fichier HTML (index.html):

    <!doctype html>
    <html>
	<head>
		<meta charset="utf-8">
		<title>{{titre}}</title>
		<link rel="stylesheet" href="./static/style.css" type="text/css" />
	</head>
    
	<body>
	<h1>'monsite'</h1>
	<h1>{{!body}}</h1>
	</body>
	
    </html>
  
Le fichier Python (site.py) :
    
    from bottle import*
	
    @route('/')
    def index():
	    return template('index.html',{'titre':'index','body': 'salut'} )
	    
	
    #la route ci dessous permet de faire le lien entre les fichiers HTML et CSS
    
    @route('/static/<filepath:path>')
    def send_static(filepath):
	    return static_file(filepath, root='./static/')
	    
    run()
   
L'arborescence des dossiers et fichiers:
    – dossier mon_site
       – fichier site.py
       – dossier view
           – fichier index.html
       – dossier static
           – fichier style.css
	   
C'est un peu complexe,  mais il suffit d'écrire une fois la route `@route('/static/<filepath:path>')` dans votre script Python, et de bien respecter l'exemple de balise link `<link rel="stylesheet" href="./static/style.css" type="text/css" />` dans vos pages HTML 
