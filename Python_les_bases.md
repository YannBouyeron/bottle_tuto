
</br>
#####<p style="color:;text-align:center;font-size:4em;">Tutoriel Python</p>
</br></br></br></br></br></br></br></br></br></br></br></br></br></br><p style="color:;text-align:center;font-size:2em;">Partie 1: Les bases</p></br></br></br></br></br></br>
 
<p style="color:;text-align:center;font-size:2em;">Informatique et Créations Numériques</p>

<p style="color:;text-align:center;font-size:px;">Cours Sainte Marie de Hann </p>
</br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br></br>

Copyright (c)  Yann Bouyeron.</br>
Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU Free Documentation License".
</br></br>
  
# I Definir une variable 

Pour définir une variable, vous devez lui donner un nom sans espace et commençant obligatoirement par une lettre. Vous devez ensuite lui attribuer une valeur ou un contenu en utilisant le signe "=".
Après avoir créé une variable, vous pouvez appeler cette variable dans le Shell en écrivant son nom, ce qui entraînera l'affichage de son contenu.

    >>> ma_variable = 5
    >>> ma_variable
    5


#Les différents types de variables

Différents types de contenus peuvent être attribués à une variable:

    >>> ma_variable = 5
    >>> type(ma_variable)
    <type 'int'>
        
    >>> ma_variable2 = 5.0
    >>> type(ma_variable2)
    <type 'float'>
    
    >>> ma_variable3 = "cinq"
    >>> type(ma_variable3)
    <type 'str'>
   
La fonction `type(nom_de_la_variable)` permet de connaître le type d'une variable préalablement définie.  
Le type int : ce sont des nombres entiers relatifs.  
Le type float : ce sont des nombres réels (avec un point représentant la virgule).  
Le type str : ce sont des chaînes de caractères , qui doivent être écrites entre guillemets

#Modifier une variable.

Comme son nom l'indique, une variable peut varier !

    >>> var = 2
    >>> var
    2
    >>> var = 34
    >>> var
    34

###Les opérations sur les variables de types int ou float

Il est possible d'effectuer des opérations avec les entiers de type int et les réels de type float:

    >>> a = 5
    >>> b = 2
    >>> a + b
    7
    >>> a - b
    3
    >>> a * b
    10
    >>> a / b
    2.5
    >>> a ** b
	25

⚠️ En python 2.7, lorsqu'on divise deux entiers, le résultat est aussi un entier !!! Ainsi, 5/2 donne 2 !
Pour faire une division réelle, il faut que au moins  l'un des deux nombres soit un réel (type float)

    >>> a = 5.0
	>>> b = 2
	>>> a / b
	2.5

Le résultat d'une opération peut être affecté à une variable :

	>>> a = 5
	>>> b = 2
	>>> c = a + b
	>>> c
	7
	>>> a = a + 10
	>>> a
	15

###Assembler des chaînes de caractères.   

La méthode "bricolage"

	>>> nom = 'Robert'
	>>> age = '32'
	>>> phrase = 'Bonjour ' + nom + ' vous avez ' + age + ' ans'
	>>> phrase
	'Bonjour Robert, vous avez 32 ans'
⚠️ Attention , ici la variable âge est de type str; il est impossible avec la méthode "bricolage" d'assembler des int ou des float avec des str !

La méthode "pro"

	>>> nom = 'Robert'
	>>> age = 32
	>>> phrase = 'Bonjour {n}, vous avez {a} ans'.format(n = nom, a = age)
	>>> phrase
	'Bonjour Robert, vous avez 32 ans'

###Modifier le type d'une variable.   

	>>> a = 5
	>>> type (a)
	<type 'int'>
	
	>>> b = float(a)
	>>> b
	5.0
	
	>>> c = str(a)
	>>> c
	'5'
	
	>>> d = int(c)
	>>> d
	5

</br>

#II L'éditeur , les entrées , et les sorties.

###L'éditeur. 

Vous avez jusqu'à présent utilisé Python en mode Shell. Ce mode est très pratique pour écrire et interpréter "à la volée" des lignes de codes ; ce qui est idéal pour tester rapidement quelques lignes de codes.   

Le désavantage étant que les lignes de codes écrites ne peuvent être sauvegardées ni même corrigées; en cas d'erreurs il faut tout ré écrire ! 

Pour remédier à cela, il existe un mode "éditeur" qui permet de sauvegarder son code.  
Pour accéder à l'éditeur, allez dans "File"  puis cliquez "New File"; une page dans laquelle vous pourrez écrire votre code s'ouvre alors.   

Indiquer toujours cette ligne en haut de votre page: `# coding: utf-8` afin de fixer l'encodage du texte (c'est inutile sur Python 3)

Pour interpréter votre code, cliquez sur F5; après avoir attribué un nom à votre algorithme se terminant en .py , cliquez à nouveau sur F5.  

Pour ré ouvrir un algorithme déjà enregistré, allez dans "File", puis "open", et recherchez le nom de votre algorithme.

###Les entrées.   

Votre algorithme peut interagir avec l'utilisateur, en lui demandant d'entrer des informations que vous attribuerez à des variables.

En Python3, la fonction input permet d’entrer des int, float, ou str qui seront automatiquement transformés en str

	nom = input('Entrez votre nom: ')
	age = input('Entrez votre age: ')
	
	phrase = 'Bonjour {n} , vous avez {a} ans'.format(n = nom, a = age)

⚠️ En Python2.7:

- Utiliser la fonction `input` pour demander à l'utilisateur d'entrer un nombre de type int ou float. 
- Utiliser la fonction `raw_input` pour demander à l'utilisateur d'entrer une chaîne de caractères de type str.  

###Les sorties.   

Vous pouvez en retour, envoyer des informations à l'utilisateur. Pour cela , utilisez la fonction `print`

	nom = input('Entrez votre nom: ')
	age = input('Entrez votre age: ')
	
	phrase = 'Bonjour {n} , vous avez {a} ans'.format(n = nom, a = age)
	
	print (phrase)

⚠️ Les parenthèses du print sont facultatives avec Python 2 mais obligatoires avec Python 3

#III Les booléens et la structure conditionnelle if.

###Les booléens.  

Un booléen est un type de variable à deux états. Les variables de ce type sont ainsi soit à l'état vrai (True) soit à l'état faux (False).
Les booléens permettent de faire des comparaisons:

	>>> a = 4
	>>> b = 2
	>>> c = 'maristes'
	
	>>> a == b
	False
	
	>>> a == 4
	True
	
	>>> a < b
	False
	
	>>> a <= b
	False
	
	>>> a > b
	True
	
	>>> a >= b
	True
	
	>>> a != b
	True
	
	>>> a != 'ok'
	True
	
	>>> type(a) == type(b)
	True
	
	>>> type(a) == type(c)
	False
	
	>>> c == 'maristes'
	True
	
	>>> c == 'Maristes'
	False

⚠️ Attention:  ne pas confondre l'affectation `a = 4` et la comparaison `a == 4` !!!

###La structure conditionnelle `if`

#### Exemple 1:

	# coding: utf-8
	
	age = input('Entrez votre age: ')
	
	age = int(age)
	
	if age >= 18:
		print('Vous êtes majeur')
	
	else:
		print('Vous êtes mineur')

Si l'âge est supérieur ou égal à 18, les instructions du bloc suivant le `if` sont exécutées (il n'y a qu'une seule instruction : `print('Vous êtes majeur')`) , mais on peut mettre plusieurs instructions dans le bloc si on le souhaite.
Sinon (autrement dit si l'âge est inférieur à 18) ce sont les instructions du bloc suivant le `else` qui sont exécutées.

⚠️ Attention à bien respecter l'indentation (décalage) des instructions de chaque bloc !

####Exemple 2:

	age = input('Entrez votre age: ')
	age = int(age)
	
	if age > 18:
	
		print('Vous êtes majeur')
	
	elif age == 18:
	
		print('Vous êtes majeur depuis cette année')
	
	else:
	
		print('Vous êtes mineur')

`elif` signifie sinon et si

Il est possible d'utiliser `if` sans `elif` ou sans `else` , de même qu'il est possible d'utiliser `if` avec `elif` mais sans `else` 

	age = input('Entrez votre age: ')
	age = int(age)
	
	if age > 18:
	
		print('Vous êtes majeur')
	
	if age == 18:
	
		print('Vous êtes majeur depuis cette année')
	
	if age < 18:
	
		print('Vous êtes mineur')

###Les connecteurs logiques `and` et `or`.  

	age = input('Entrez votre age: ')
	genre = input('Entrez votre genre (H ou F): ')
	
	age = int(age)
	
	if age >= 18 and genre == 'H':
	
		print('Vous êtes un homme majeur')
	
	elif age >= 18 and genre == 'F':
	
		print('Vous êtes une femme majeure')
	
	elif age < 18 and genre == 'M':
	
		print ('Vous êtes un homme mineur')
	
	else:
	
		print ('Vous êtes une femme mineure')

L'exemple ci-dessus utilise le connecteur logique `and`, les 2 conditions situées de part et d'autre du `and` doivent être vérifiées pour que le bloc d'instructions soit exécuté .

Lorsque qu'on utilise le connecteur logique `or`, seule l'une des deux conditions situées de part et d'autre du `or` doit être vérifiée pour que le bloc d'instructions soit exécuté .

L'algorithme ci dessous est identique au précédant sauf qu'il n'utilise pas de connecteurs logiques. Regardez bien l'imbrication et l'indentation des blocs d'instructions.

	age = input('Entrez votre age: ')
	genre = input('Entrez votre genre (H ou F): ')
	
	age = int(age)
	
	if age >= 18:
	
		if genre == 'H':
	
			print('Vous êtes un homme majeur')
	
		elif genre == 'F':
	
			print('Vous êtes une femme majeure')
	
	elif age < 18:
	
		if genre == 'M':
	
			print ('Vous êtes un homme mineur')
	
		elif genre == 'F':
	
			print ('Vous êtes une femme mineure')

#IV La boucle "while".  

En anglais "while" signifie "tant que".

Cette fonction de python permet de créer des boucles: Tant que (while) la condition booléenne est vérifiée alors les instructions du bloc d'instructions sont réalisées.   

####Exemple 1:

    n = int(input('Entrez un nombre supérieur à 100: '))
    
    while n < 100:
	
	    print("""Vous n'avez pas respecté la consigne !!! \n""")
	
	    n = input('Entrez un nombre supérieur à 100: ')
	
    print ("""C'est bien, vous avez respecté la consigne.""")
   

On demande à l'utilisateur d'entrer un nombre supérieur à 100, et on affecte ce nombre à la variable `n`.
On utilise ensuite la fonction `while` pour vérifier la condition booléenne `n < 100` .

Tant que la valeur affectée à la variable n est inférieure à 100 , autrement dit tant que l'utilisateur n'a pas respecté la consigne, on exécute les deux instructions du bloc d'instructions faisant suite au `while`:

- on lui affiche un message pour le réprimander: `print("""Vous n'avez pas respecté la consigne !!! \n""")`
- on lui redemande d'entrer un nombre supérieur à 100: `n = input('Entrez un nombre supérieur à 100: ')`



L'algorithme va ensuite revérifier la condition booléenne `n < 100` , et tant qu'elle serra vérifiée , autrement dit tant que la consigne ne serra pas respectée , la boucle while se répétera.

Lorsque l'utilisateur entrera un nombre supérieur à 100, la condition booléenne `n < 100` ne serra plus vérifiée et le bloc d'instruction de la boucle while ne serra pas exécuté. L'algorithme se poursuivra et se terminera en exécutant le `print ("""C'est bien, vous avez respecté la consigne.""")` qui est situé hors du bloc d'instruction de la boucle `while`


####Exemple 2:  

    nombre_de_chances_max = 100
    
    nombre_de_chances_utilisees = 0
    
    reponse = int(input('Les cours Sainte Marie de Hann ont été fondés en quelle année ? '))
    
    bonne_reponse = 1950
    
    while nombre_de_chances_utilisees < nombre_de_chances_max:
	
		if reponse != bonne_reponse:
		
			nombre_de_chances_utilisees = nombre_de_chances_utilisees + 1
		
			print('Mauvaise réponse, il vous reste {x} chances \n'.format(x = nombre_de_chances_max-nombre_de_chances_utilisees))
		
			reponse = input('Les cours Sainte Marie de Hann ont été fondés en quelle année ? ')
		
		else:
		
			print("Bravo, c'est la bonne réponse !")
		
			break
 

#V Les listes.  

###Créer une liste:  

#####En utilisant des crochets:

    >>> z =[1,2,3,4]
    >>> z
    [1, 2, 3, 4]
    >>> type(z)
    <type 'list'>

#####En utilisant la fonction list():   


    >>> u = list('1234')
    >>> u
    ['1', '2', '3', '4']
    >>> type(u)
    <type 'list'>
  
  
  
#####En utilisant la fonction range():  

En Python3:

	>>> a = range(20)
	>>> a
	range(0, 20)
	>>> list(a)
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
	>>> type(a)
    <type 'list'>

En Python2.7:

    >>> a = range(20)
    >>> a
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    >>> type(a)
    <type 'list'>
 
 
#####Les listes peuvent contenir des entiers, des réels, et des chaînes de caractères 

    >>> fruits = ['pomme', 'poire', 'fraise', 'orange']
    >>> 
    >>> listecombinee = ['pomme', 3, 'orange', 2.543]
   
   
   
###Obtenir des informations sur une liste:

Création d'une liste nommée "maliste":
   
    >>> maliste = [1,2,3,4,5]

La fonction len() indique la longueur de la liste, c'est à dire le nombre d'éléments dans la liste:

    >>> len(maliste)
    5

La fonction max() indique le nombre le plus élevé d'une liste de nombres, ou le dernier élément alphabétique  d'une liste de mots

	>>> max(maliste)
	5


La fonction min() indique le nombre le plus petit d'une liste de nombres, ou le premier élément alphabétique  d'une liste de mots

	>>> min(maliste)
	1

Python compte toujours à partir de 0.
maliste[0] renvoie le premier élément de la liste intitulée "maliste", c'est à dire l'élément d'index 0 de la liste

	>>> maliste[0]
	1
	>>> maliste[4]
	5

La fonction sum() indique la somme des éléments de la liste:

	>>> sum(maliste)
	15

###Ajouter des éléments à une liste:

    >>> a = [1,2,3,4]
    >>> a + [1]
    [1, 2, 3, 4, 1]
   
 Ou en utilisant la fonction append:
 
    >>> a = [1,2,3,4]
    >>> a.append(1)
    >>> a
    [1, 2, 3, 4, 1]
   


###Modifier un élément:

    >>> a = [1,2,3,4]
    >>> a[1] = 333
    >>> a
    [1, 333, 3, 4]

###Inserer un élément:

    >>> a = [1,2,3,4]
    >>> a.insert(1,5555)
    >>> a
    [1, 5555, 2, 3, 4]
  

###Ranger ...

Dans l'ordre croissant:

    >>> a = [2,1,4,3]
    >>> a.sort()
    >>> a
    [1, 2, 3, 4]
   
Dans l'ordre décroissant:

    >>> a = [1,2,3,4]
    >>> a.sort(reverse = True)
    >>> a
    [4, 3, 2, 1]
   
   
Inverser l'ordre:

    >>> a = [2,1,4,3]
    >>> a.reverse()
    >>> a
    [3, 4, 1, 2]
  
  
###Supprimer un élément:

    >>> a = [1,2,3,4]
    >>> a.remove(3)
    >>> a
    [1, 2, 4]
   
   
###Parcourir une liste: la boucle "for":

Pour tous les éléments (appelés ici "i") de la liste a , on affiche chaque élément i multiplié par 2	

	>>> a = [1,2,3,4]
	>>> for i in a:
	...   print(i*2)
	...   
	2
	4
	6
	8


La liste b est une liste vide. Pour tous les éléments i de la liste a , on affecte à la variable x le produit i*2 , et on ajoute la valeur de x à la liste b. 

	>>> a = [1,2,3,4]
	>>> b = []
	>>> 
	>>> for i in a:
	...   x = i*2
	...   b.append(x)
	...   
	>>> b
	[2, 4, 6, 8]



###Enumerer une liste

La fonction enumerate() permet de parcourir une liste et d'obtenir l'index (position de l'élément dans la liste) et la valeur de chaque élément.

	>>> fruits
	['pomme', 'poire', 'fraise', 'orange']
	>>> for i, v in enumerate(fruits):
	...   print ('index {0} valeur {1}'.format(i, v))
	...   
	index 0 valeur pomme
	index 1 valeur poire
	index 2 valeur fraise
	index 3 valeur orange

⚠️ Vous remarquerez que Python commence toujours à compter à partir de 0 (le premier élément d’une liste est l’élément d’index 0)

###Obtenir l'index d'un élément à partir de sa valeur:

	>>> fruits
	['pomme', 'poire', 'fraise', 'orange']
	>>> fruits.index('poire')
	1

###Convertir une chaîne de caractères en liste de mots:

	>>> s = 'bonjour comment ca va ?'
	>>> p = s.split(' ')
	>>> p 
	['bonjour', 'comment', 'ca', 'va', '?']


###Convertir une liste de mots en une chaîne de caractères:

	>>> p
	['bonjour', 'comment', 'ca', 'va', '?']
	>>> q = " ".join(p)
	>>> q
	'bonjour comment ca va ?'


###Sectionner une liste:

	>>> p
	['bonjour', 'comment', 'ca', 'va', '?']

	>>> p[1:]
	['comment', 'ca', 'va', '?']

	>>> p[2:4]
	['ca', 'va']

	>>> p[:4]
	['bonjour', 'comment', 'ca', 'va']

	>>> p[:1]
	['bonjour']

###Choisir un élément au hasard dans une liste

Il faut pour cela importer le module random:

	import random

On peut utiliser la fonction random.choice() :

	>>> import random
	
	>>> a = range(20)
	>>> list(a)
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
	
	>>> h = random.choice(a)
	>>> h
	3
	
	>>> h = random.choice(a)
	>>> h
	14

L'algorithme ci dessus choisit au hasard un élément dans la liste a 



On peut aussi utiliser la fonction random.randint():

	>>> import random
	
	>>> x = random.randint(0,20)
	>>> x
	4
	
	>>> x = random.randint(0,20)
	>>> x
	20

L'algorithme ci dessus choisit au hasard un nombre compris entre 0 et 20

###Revenir au début d'une liste lorsque l'index sort de la liste

	>>> x = ['peche','pomme','poire','abricot']
	>>> y = len(x)
	>>> y
	4
	>>> x[3]
	'abricot'
	>>> x[4]
	Traceback (most recent call last):
	  File "<string>", line 1, in <module>
	IndexError: list index out of range
	>>> x[4-y]
	'peche'
	


###Les index négatifs 
	>>> x[-1]
	'abricot'
	>>> x[-1] == x[y-1]
	True

#VI Les dictionnaires.

Les dictionnaires sont des objets qui associent des clés à des valeurs. Les clés et les valeurs peuvent être des chaînes de caractères (str), des entiers (int), des réels (float), des listes (list) ou des tuples (tuple) ou des listes de tuples...

	>>> dico = {'clé1': 'valeur1', 'clé2': 'valeur2', 'clé3': 'valeur3'}
	>>> dico
	{'clé2': 'valeur2', 'clé3': 'valeur3', 'clé1': 'valeur1'}


###Créer un dictionnaire.

Il existe plusieurs manières de créer un dictionnaire:

	>>> d = {'fruit1':'pomme', 'fruit4': 'orange', 'fruit3': 'poire'}
	>>> d
	{'fruit3': 'poire', 'fruit1': 'pomme', 'fruit4': 'orange'}

	>>> d2 = dict(a = 45, b = 3, c= 532)
	>>> d2
	{'b': 3, 'c': 532, 'a': 45}

	>>> d3 = dict( [ (1,'un'), (2,'deux'), (3,'trois')] )
	>>> d3
	{1: 'un', 2: 'deux', 3: 'trois'}


###Appeler une valeur correspondant à une clé 

	>>> d['fruit1']
	'pomme'


###Ajouter un couple clé/valeur.

	>>> d
	{'fruit1': 'pomme', 'fruit3': 'poire', 'fruit4': 'orange'}
	
	>>> d['fruit2'] = 'citron'
	
	>>> d
	{'fruit1': 'pomme', 'fruit2': 'citron', 'fruit3': 'poire', 'fruit4': 'orange'}

###Modifier une valeur.

	>>> d['fruit1']= 'banane'
	>>> d
	{'fruit1': 'banane', 'fruit2': 'citron', 'fruit3': 'poire', 'fruit4': 'orange'}

###Supprimer un couple clé/valeur.

	>>> d
	{'fruit3': 'poire', 'fruit2': 'citron', 'fruit1': 'banane', 'fruit4': 'orange'}
	
	>>> del(d['fruit4'])
	
	>>> d
	{'fruit3': 'poire', 'fruit2': 'citron', 'fruit1': 'banane'}


###Afficher toutes les clés d'un dictionnaire.

	>>> d.keys()
	dict_keys(['fruit1', 'fruit2', 'fruit3'])

###Afficher toutes les valeurs d'un dictionnaire.

	>>> d.values()
	dict_values(['pomme', 'citron', 'poire'])

###Parcourir un dictionnaire.

Les deux méthodes ci-dessous sont équivalentes.

	>>> for k,v in d.items():
	...   print(k, '=', v)
	...   
	fruit1 = banane
	fruit2 = citron
	fruit3 = poire
	fruit4 = orange


	>>> for k in d.keys():
	...   print (k, '=', d[k])
	...   
	fruit1 = banane
	fruit2 = citron
	fruit3 = poire
	fruit4 = orange

###Le module AttrDict

Ce module permet de faciliter l’utilisation d’un dictionnaire :

	>>> from attrdict import AttrDict
	>>> d = {"fruit":"pomme"}
	>>> a = AttrDict(d)
	>>> a.fruit
	'pomme'
	>>> a['fruit']
	'pomme'

Autre exemple:

	>>> attr = AttrDict({'fruit': {'agrume': 'orange'}})
	>>> attr.fruit.agrume
	'orange'

#VII Manipuler des chaînes de caractères.

###Créer une chaîne:

	>>> c = 'salut comment ca va'

###Créer une chaîne qui contient des apostrophes:

	>>> d = """salut l'ami"""
	>>> d
	"salut l'ami"


###Afficher la longueur de la chaîne:

	>>> len(c)
	19

###Afficher le caractère le plus "élevé" :

	>>> max(c)
	'v'

###Afficher le caractère le plus "petit":

	>>> min(c)
	' '

###Parcourir une chaîne avec une boucle for:

	>>> for v in c:
	...   print v
	...   
	s
	a
	l
	u
	t
	 
	c
	o
	m
	m
	e
	n
	t
	 
	c
	a
	 
	v
	a

###Énumérer une chaîne :

	>>> for i, v in enumerate(c):
	...   print i, v
	...   
	0 s
	1 a
	2 l
	3 u
	4 t
	5  
	6 c
	7 o
	8 m
	9 m
	10 e
	11 n
	12 t
	13  
	14 c
	15 a
	16  
	17 v
	18 a

###Retrouver la valeur d'un caractère en fonction de son index

	>>> c[2]
	'l'

###Retrouver l'index d'un caractère (si le caractère est présent plusieurs fois , seul son premier index serra affiché)

	>>> c.index('t')
	4

###Ajouter une majuscule en début de phrase:

	>>> c.capitalize()
	'Salut comment ca va'

###Tout mettre en majuscules:

	>>> c.upper()
	'SALUT COMMENT CA VA'

Utilisez la fonction `lower()` pour passer des majuscules aux minuscules


###Remplacer ou supprimer des caractères :

	>>> c.replace('t','y')
	'saluy commeny ca va'

	>>> c.replace('t','')
	'salu commen ca va'

	>>> c.replace(' ','')
	'salutcommentcava'

###Supprimer des espaces en début et fin de chaine:

	c = ' bonjour '
	>>> c.strip()
	'bonjour'

###Sectionner une chaîne de caractères :

	>>> c = 'salut comment ca va'

	>>> c[:5]
	'salut'

	>>> c[6:13]
	'comment'

	>>> c[17:]
	'va'


###Convertir une chaîne de caractères en liste de mots:

	>>> s = 'bonjour comment ca va ?'
	>>> p = s.split(' ')
	>>> p 
	['bonjour', 'comment', 'ca', 'va', '?']


###Convertir une liste de mots en une chaîne de caractères:

	>>> p
	['bonjour', 'comment', 'ca', 'va', '?']
	>>> q = " ".join(p)
	>>> q
	'bonjour comment ca va ?'



### GNU Free Documentation License

Version 1.3, 3 November 2008

Copyright (C) 2000, 2001, 2002, 2007, 2008 Free Software Foundation,
Inc. <https://fsf.org/>

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

#### 0. PREAMBLE

The purpose of this License is to make a manual, textbook, or other
functional and useful document "free" in the sense of freedom: to
assure everyone the effective freedom to copy and redistribute it,
with or without modifying it, either commercially or noncommercially.
Secondarily, this License preserves for the author and publisher a way
to get credit for their work, while not being considered responsible
for modifications made by others.

This License is a kind of "copyleft", which means that derivative
works of the document must themselves be free in the same sense. It
complements the GNU General Public License, which is a copyleft
license designed for free software.

We have designed this License in order to use it for manuals for free
software, because free software needs free documentation: a free
program should come with manuals providing the same freedoms that the
software does. But this License is not limited to software manuals; it
can be used for any textual work, regardless of subject matter or
whether it is published as a printed book. We recommend this License
principally for works whose purpose is instruction or reference.

#### 1. APPLICABILITY AND DEFINITIONS

This License applies to any manual or other work, in any medium, that
contains a notice placed by the copyright holder saying it can be
distributed under the terms of this License. Such a notice grants a
world-wide, royalty-free license, unlimited in duration, to use that
work under the conditions stated herein. The "Document", below, refers
to any such manual or work. Any member of the public is a licensee,
and is addressed as "you". You accept the license if you copy, modify
or distribute the work in a way requiring permission under copyright
law.

A "Modified Version" of the Document means any work containing the
Document or a portion of it, either copied verbatim, or with
modifications and/or translated into another language.

A "Secondary Section" is a named appendix or a front-matter section of
the Document that deals exclusively with the relationship of the
publishers or authors of the Document to the Document's overall
subject (or to related matters) and contains nothing that could fall
directly within that overall subject. (Thus, if the Document is in
part a textbook of mathematics, a Secondary Section may not explain
any mathematics.) The relationship could be a matter of historical
connection with the subject or with related matters, or of legal,
commercial, philosophical, ethical or political position regarding
them.

The "Invariant Sections" are certain Secondary Sections whose titles
are designated, as being those of Invariant Sections, in the notice
that says that the Document is released under this License. If a
section does not fit the above definition of Secondary then it is not
allowed to be designated as Invariant. The Document may contain zero
Invariant Sections. If the Document does not identify any Invariant
Sections then there are none.

The "Cover Texts" are certain short passages of text that are listed,
as Front-Cover Texts or Back-Cover Texts, in the notice that says that
the Document is released under this License. A Front-Cover Text may be
at most 5 words, and a Back-Cover Text may be at most 25 words.

A "Transparent" copy of the Document means a machine-readable copy,
represented in a format whose specification is available to the
general public, that is suitable for revising the document
straightforwardly with generic text editors or (for images composed of
pixels) generic paint programs or (for drawings) some widely available
drawing editor, and that is suitable for input to text formatters or
for automatic translation to a variety of formats suitable for input
to text formatters. A copy made in an otherwise Transparent file
format whose markup, or absence of markup, has been arranged to thwart
or discourage subsequent modification by readers is not Transparent.
An image format is not Transparent if used for any substantial amount
of text. A copy that is not "Transparent" is called "Opaque".

Examples of suitable formats for Transparent copies include plain
ASCII without markup, Texinfo input format, LaTeX input format, SGML
or XML using a publicly available DTD, and standard-conforming simple
HTML, PostScript or PDF designed for human modification. Examples of
transparent image formats include PNG, XCF and JPG. Opaque formats
include proprietary formats that can be read and edited only by
proprietary word processors, SGML or XML for which the DTD and/or
processing tools are not generally available, and the
machine-generated HTML, PostScript or PDF produced by some word
processors for output purposes only.

The "Title Page" means, for a printed book, the title page itself,
plus such following pages as are needed to hold, legibly, the material
this License requires to appear in the title page. For works in
formats which do not have any title page as such, "Title Page" means
the text near the most prominent appearance of the work's title,
preceding the beginning of the body of the text.

The "publisher" means any person or entity that distributes copies of
the Document to the public.

A section "Entitled XYZ" means a named subunit of the Document whose
title either is precisely XYZ or contains XYZ in parentheses following
text that translates XYZ in another language. (Here XYZ stands for a
specific section name mentioned below, such as "Acknowledgements",
"Dedications", "Endorsements", or "History".) To "Preserve the Title"
of such a section when you modify the Document means that it remains a
section "Entitled XYZ" according to this definition.

The Document may include Warranty Disclaimers next to the notice which
states that this License applies to the Document. These Warranty
Disclaimers are considered to be included by reference in this
License, but only as regards disclaiming warranties: any other
implication that these Warranty Disclaimers may have is void and has
no effect on the meaning of this License.

#### 2. VERBATIM COPYING

You may copy and distribute the Document in any medium, either
commercially or noncommercially, provided that this License, the
copyright notices, and the license notice saying this License applies
to the Document are reproduced in all copies, and that you add no
other conditions whatsoever to those of this License. You may not use
technical measures to obstruct or control the reading or further
copying of the copies you make or distribute. However, you may accept
compensation in exchange for copies. If you distribute a large enough
number of copies you must also follow the conditions in section 3.

You may also lend copies, under the same conditions stated above, and
you may publicly display copies.

#### 3. COPYING IN QUANTITY

If you publish printed copies (or copies in media that commonly have
printed covers) of the Document, numbering more than 100, and the
Document's license notice requires Cover Texts, you must enclose the
copies in covers that carry, clearly and legibly, all these Cover
Texts: Front-Cover Texts on the front cover, and Back-Cover Texts on
the back cover. Both covers must also clearly and legibly identify you
as the publisher of these copies. The front cover must present the
full title with all words of the title equally prominent and visible.
You may add other material on the covers in addition. Copying with
changes limited to the covers, as long as they preserve the title of
the Document and satisfy these conditions, can be treated as verbatim
copying in other respects.

If the required texts for either cover are too voluminous to fit
legibly, you should put the first ones listed (as many as fit
reasonably) on the actual cover, and continue the rest onto adjacent
pages.

If you publish or distribute Opaque copies of the Document numbering
more than 100, you must either include a machine-readable Transparent
copy along with each Opaque copy, or state in or with each Opaque copy
a computer-network location from which the general network-using
public has access to download using public-standard network protocols
a complete Transparent copy of the Document, free of added material.
If you use the latter option, you must take reasonably prudent steps,
when you begin distribution of Opaque copies in quantity, to ensure
that this Transparent copy will remain thus accessible at the stated
location until at least one year after the last time you distribute an
Opaque copy (directly or through your agents or retailers) of that
edition to the public.

It is requested, but not required, that you contact the authors of the
Document well before redistributing any large number of copies, to
give them a chance to provide you with an updated version of the
Document.

#### 4. MODIFICATIONS

You may copy and distribute a Modified Version of the Document under
the conditions of sections 2 and 3 above, provided that you release
the Modified Version under precisely this License, with the Modified
Version filling the role of the Document, thus licensing distribution
and modification of the Modified Version to whoever possesses a copy
of it. In addition, you must do these things in the Modified Version:

-   A. Use in the Title Page (and on the covers, if any) a title
    distinct from that of the Document, and from those of previous
    versions (which should, if there were any, be listed in the
    History section of the Document). You may use the same title as a
    previous version if the original publisher of that version
    gives permission.
-   B. List on the Title Page, as authors, one or more persons or
    entities responsible for authorship of the modifications in the
    Modified Version, together with at least five of the principal
    authors of the Document (all of its principal authors, if it has
    fewer than five), unless they release you from this requirement.
-   C. State on the Title page the name of the publisher of the
    Modified Version, as the publisher.
-   D. Preserve all the copyright notices of the Document.
-   E. Add an appropriate copyright notice for your modifications
    adjacent to the other copyright notices.
-   F. Include, immediately after the copyright notices, a license
    notice giving the public permission to use the Modified Version
    under the terms of this License, in the form shown in the
    Addendum below.
-   G. Preserve in that license notice the full lists of Invariant
    Sections and required Cover Texts given in the Document's
    license notice.
-   H. Include an unaltered copy of this License.
-   I. Preserve the section Entitled "History", Preserve its Title,
    and add to it an item stating at least the title, year, new
    authors, and publisher of the Modified Version as given on the
    Title Page. If there is no section Entitled "History" in the
    Document, create one stating the title, year, authors, and
    publisher of the Document as given on its Title Page, then add an
    item describing the Modified Version as stated in the
    previous sentence.
-   J. Preserve the network location, if any, given in the Document
    for public access to a Transparent copy of the Document, and
    likewise the network locations given in the Document for previous
    versions it was based on. These may be placed in the "History"
    section. You may omit a network location for a work that was
    published at least four years before the Document itself, or if
    the original publisher of the version it refers to
    gives permission.
-   K. For any section Entitled "Acknowledgements" or "Dedications",
    Preserve the Title of the section, and preserve in the section all
    the substance and tone of each of the contributor acknowledgements
    and/or dedications given therein.
-   L. Preserve all the Invariant Sections of the Document, unaltered
    in their text and in their titles. Section numbers or the
    equivalent are not considered part of the section titles.
-   M. Delete any section Entitled "Endorsements". Such a section may
    not be included in the Modified Version.
-   N. Do not retitle any existing section to be Entitled
    "Endorsements" or to conflict in title with any Invariant Section.
-   O. Preserve any Warranty Disclaimers.

If the Modified Version includes new front-matter sections or
appendices that qualify as Secondary Sections and contain no material
copied from the Document, you may at your option designate some or all
of these sections as invariant. To do this, add their titles to the
list of Invariant Sections in the Modified Version's license notice.
These titles must be distinct from any other section titles.

You may add a section Entitled "Endorsements", provided it contains
nothing but endorsements of your Modified Version by various
partiesâ€”for example, statements of peer review or that the text has
been approved by an organization as the authoritative definition of a
standard.

You may add a passage of up to five words as a Front-Cover Text, and a
passage of up to 25 words as a Back-Cover Text, to the end of the list
of Cover Texts in the Modified Version. Only one passage of
Front-Cover Text and one of Back-Cover Text may be added by (or
through arrangements made by) any one entity. If the Document already
includes a cover text for the same cover, previously added by you or
by arrangement made by the same entity you are acting on behalf of,
you may not add another; but you may replace the old one, on explicit
permission from the previous publisher that added the old one.

The author(s) and publisher(s) of the Document do not by this License
give permission to use their names for publicity for or to assert or
imply endorsement of any Modified Version.

#### 5. COMBINING DOCUMENTS

You may combine the Document with other documents released under this
License, under the terms defined in section 4 above for modified
versions, provided that you include in the combination all of the
Invariant Sections of all of the original documents, unmodified, and
list them all as Invariant Sections of your combined work in its
license notice, and that you preserve all their Warranty Disclaimers.

The combined work need only contain one copy of this License, and
multiple identical Invariant Sections may be replaced with a single
copy. If there are multiple Invariant Sections with the same name but
different contents, make the title of each such section unique by
adding at the end of it, in parentheses, the name of the original
author or publisher of that section if known, or else a unique number.
Make the same adjustment to the section titles in the list of
Invariant Sections in the license notice of the combined work.

In the combination, you must combine any sections Entitled "History"
in the various original documents, forming one section Entitled
"History"; likewise combine any sections Entitled "Acknowledgements",
and any sections Entitled "Dedications". You must delete all sections
Entitled "Endorsements".

#### 6. COLLECTIONS OF DOCUMENTS

You may make a collection consisting of the Document and other
documents released under this License, and replace the individual
copies of this License in the various documents with a single copy
that is included in the collection, provided that you follow the rules
of this License for verbatim copying of each of the documents in all
other respects.

You may extract a single document from such a collection, and
distribute it individually under this License, provided you insert a
copy of this License into the extracted document, and follow this
License in all other respects regarding verbatim copying of that
document.

#### 7. AGGREGATION WITH INDEPENDENT WORKS

A compilation of the Document or its derivatives with other separate
and independent documents or works, in or on a volume of a storage or
distribution medium, is called an "aggregate" if the copyright
resulting from the compilation is not used to limit the legal rights
of the compilation's users beyond what the individual works permit.
When the Document is included in an aggregate, this License does not
apply to the other works in the aggregate which are not themselves
derivative works of the Document.

If the Cover Text requirement of section 3 is applicable to these
copies of the Document, then if the Document is less than one half of
the entire aggregate, the Document's Cover Texts may be placed on
covers that bracket the Document within the aggregate, or the
electronic equivalent of covers if the Document is in electronic form.
Otherwise they must appear on printed covers that bracket the whole
aggregate.

#### 8. TRANSLATION

Translation is considered a kind of modification, so you may
distribute translations of the Document under the terms of section 4.
Replacing Invariant Sections with translations requires special
permission from their copyright holders, but you may include
translations of some or all Invariant Sections in addition to the
original versions of these Invariant Sections. You may include a
translation of this License, and all the license notices in the
Document, and any Warranty Disclaimers, provided that you also include
the original English version of this License and the original versions
of those notices and disclaimers. In case of a disagreement between
the translation and the original version of this License or a notice
or disclaimer, the original version will prevail.

If a section in the Document is Entitled "Acknowledgements",
"Dedications", or "History", the requirement (section 4) to Preserve
its Title (section 1) will typically require changing the actual
title.

#### 9. TERMINATION

You may not copy, modify, sublicense, or distribute the Document
except as expressly provided under this License. Any attempt otherwise
to copy, modify, sublicense, or distribute it is void, and will
automatically terminate your rights under this License.

However, if you cease all violation of this License, then your license
from a particular copyright holder is reinstated (a) provisionally,
unless and until the copyright holder explicitly and finally
terminates your license, and (b) permanently, if the copyright holder
fails to notify you of the violation by some reasonable means prior to
60 days after the cessation.

Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License. If your rights have been terminated and not permanently
reinstated, receipt of a copy of some or all of the same material does
not give you any rights to use it.

#### 10. FUTURE REVISIONS OF THIS LICENSE

The Free Software Foundation may publish new, revised versions of the
GNU Free Documentation License from time to time. Such new versions
will be similar in spirit to the present version, but may differ in
detail to address new problems or concerns. See
<https://www.gnu.org/licenses/>.

Each version of the License is given a distinguishing version number.
If the Document specifies that a particular numbered version of this
License "or any later version" applies to it, you have the option of
following the terms and conditions either of that specified version or
of any later version that has been published (not as a draft) by the
Free Software Foundation. If the Document does not specify a version
number of this License, you may choose any version ever published (not
as a draft) by the Free Software Foundation. If the Document specifies
that a proxy can decide which future versions of this License can be
used, that proxy's public statement of acceptance of a version
permanently authorizes you to choose that version for the Document.

#### 11. RELICENSING

"Massive Multiauthor Collaboration Site" (or "MMC Site") means any
World Wide Web server that publishes copyrightable works and also
provides prominent facilities for anybody to edit those works. A
public wiki that anybody can edit is an example of such a server. A
"Massive Multiauthor Collaboration" (or "MMC") contained in the site
means any set of copyrightable works thus published on the MMC site.

"CC-BY-SA" means the Creative Commons Attribution-Share Alike 3.0
license published by Creative Commons Corporation, a not-for-profit
corporation with a principal place of business in San Francisco,
California, as well as future copyleft versions of that license
published by that same organization.

"Incorporate" means to publish or republish a Document, in whole or in
part, as part of another Document.

An MMC is "eligible for relicensing" if it is licensed under this
License, and if all works that were first published under this License
somewhere other than this MMC, and subsequently incorporated in whole
or in part into the MMC, (1) had no cover texts or invariant sections,
and (2) were thus incorporated prior to November 1, 2008.

The operator of an MMC Site may republish an MMC contained in the site
under CC-BY-SA on the same site at any time before August 1, 2009,
provided the MMC is eligible for relicensing.

### ADDENDUM: How to use this License for your documents

To use this License in a document you have written, include a copy of
the License in the document and put the following copyright and
license notices just after the title page:

        Copyright (C)  YEAR  YOUR NAME.
        Permission is granted to copy, distribute and/or modify this document
        under the terms of the GNU Free Documentation License, Version 1.3
        or any later version published by the Free Software Foundation;
        with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
        A copy of the license is included in the section entitled "GNU
        Free Documentation License".

If you have Invariant Sections, Front-Cover Texts and Back-Cover
Texts, replace the "with â€¦ Texts." line with this:

        with the Invariant Sections being LIST THEIR TITLES, with the
        Front-Cover Texts being LIST, and with the Back-Cover Texts being LIST.

If you have Invariant Sections without Cover Texts, or some other
combination of the three, merge those two alternatives to suit the
situation.

If your document contains nontrivial examples of program code, we
recommend releasing these examples in parallel under your choice of
free software license, such as the GNU General Public License, to
permit their use in free software.
