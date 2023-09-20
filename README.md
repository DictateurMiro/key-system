# Système de clé

Dans ce repo qui sera un tuto vous allez voir comment fonctionne un système de clé, j'ai mis en place le système mais l'idée existe depuis la nuit des temps

Donc dans un premier temps vous allez devoir prendre un serveur VPS, linux ou windows, vous allez ensuite ouvrir le port 8080 (c'est pour ça que c'est mieux d'avoir un vps)

Ensuite vous allez en tant qu'utilisateur lancé le fichier "<a href="https://github.com/DictateurMiro/key-system/blob/main/client/get_mac_sha256.py">get_mac_sha256.py</a>" le programme va vous donner une suite de caractères qui est votre adresse MAC hashé sous sha256

Maintenant que l'utilisateur possede cette chaine vous en tant qu'administrateur vous allez récupérer cette clé et vous allez l'ajouté dans le serveur via le fichier "add_key.py"
Celui ci vous demanderas la chaine de caractère, vous allez la rentré et le programme va sauvegardé la chaine de caractère et vous donner une clé en même temps

Cette clé vous allez la donnés à l'utilsateur et il faudra qu'il la mette dans le fichier "config.ini" à la ligne "key"
Une fois la clé rentré l'utilisateur devra lancer le programme et celui-ci marcheras si la clé est valide ainsi que l'adresse ma hashé

### Explication

Le programme va récuppérer l'adresse mac sous sha256 de l'ordinateur qui lance ce meme programme il va ensuite envoyer une requete via post sur le serveur désigné, une fois la requete envoyé celle ci demande au serveur si l'adresse mac hashé correspond a une clé, ensuite le programme va lire la clé dans le fichier config.ini, et va envoyé la clé dans la requete pour vérifier que la clé correspond a l'adresse mac hashé qui ce trouve dans le serveur 
