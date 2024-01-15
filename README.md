# BallBot
Preuve de concept d'un BallBot (robot sphérique)

## Installation

### Arduino

Le seul outil nécessaire pour envoyer le code arduino (ballbot.ino) jusqu'à la carte Arduino Uno est l'IDE Arduino.\
Pour cela télécharger le logiciel depuis https://www.arduino.cc/en/software. \
Il faut ensuite ouvrir le fichier ballbot.ino puis cliquer sur l'icone de flèche en haut à gauche pour téléverser le code sur la carte branchée à l'ordinateur.\
Il est important de noter que la puce bluetooth HC-05 ne doit pas être branchée lors du téléversement.\
Une fois le téléversement fait, la puce bluetooth se branche sur les pins 0 et 1, et les moteurs sur les pins 5 et 6 (peut être changé en modifiant le code arduino).

### Contrôleur

Le contrôleur (Controller.py) est écrit en python 3.\
Il faut donc avoir une version de python 3 (`python --version`) ainsi que pip ou équivalent pour installer les dépendances nécessaires.\
Le contrôleur utilise les librairies pygame et bluetooth :\
`python -m pip install pygame` et `python -m pip install bluetooth`\
Pour fonctionner, il faut aussi que l'ordinateur est le bletooth activer.\
Lorsque le programme se lance, une petite fenêtre s'ouvre et vous pouvez utiliser les flèches directionnelles pour contrôler le ballbot.
