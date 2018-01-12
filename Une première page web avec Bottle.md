# Une première page web avec Bottle

Bottle est un module de Python qui permet de réaliser des sites web ou applications web dynamiques. Contrairement à un site statique 
qui permet des échanges limités entre le serveur et votre navigateur internet (le navigateur se contente d'envoyer des requêtes 
destinées au serveur qui lui renvoie des réponses: les pages internet correspondant aux requêtes), un site dynamique permet un échange 
d'informations plus important, notamment en permettant l'envoi d'informations du navigateur vers le serveur (grâce aux formulaires) , 
éventuellement le stockage des ces informations dans une base de donnée gérée par le serveur hébergeant l'application, le traitement 
de ces informations, et la genèse d'une page internet adaptée aux requêtes de l'utilisateur.
## Importer Bottle
Comme tout module, Bottle peut s'importer de différentes manières, il est toutefois conseillé de l'importer de la façon suivante:

    from bottle import *
   
## Une route, une page
Voici un exemple de code basique pour présenter le principe général de Bottle:

    from bottle import *
    app = Bottle()
    
    @app.route('/index')
    def page_index():
		return 'voici ma première application web'
		
    app.run(host='localhost', port=27200, reload=True, debug=True)
   
Quelques explications: 
- ligne 1: On indique l'encodage uft-8 qui permet l´affichage des accents (inutile en python3). 
- ligne 2: On importe bottle. 
- ligne 3: On crée une application bottle, ce n'est pas indispensable mais c'est plus propre ainsi. 
- ligne 4: On crée une route (un chemin) indiquant la localisation de notre page internet: /index - ligne 5: On définit une fonction qui correspond à notre page; le nom de la fonction a peu d'importance. Dans cet exemple simplifié, le bloc d'instruction de notre fonction ne contient rien. 
- ligne 6: Le "return" renvoie une chaîne de caractères. 
- ligne 7: On lance le serveur sur l'adresse locale: http://localhost:27200 ; notre page sera accessible à l'adresse suivante: [http://localhost:27200/index](http://localhost:27200/index)
  
## Une même page accessible depuis différentes routes

    from bottle import *
    app = Bottle()
                                      
    @app.route('/')
    @app.route('/index')
    
    def page_index():
		return 'voici ma première application web'
	
    app.run(host='localhost', port=27200, reload=True, debug=True)
  
 
Notre page index est désormais accessible via les routes  [http://localhost:27200](http://localhost:27200) et [http://localhost:27200/index](http://localhost:27200/index) 

