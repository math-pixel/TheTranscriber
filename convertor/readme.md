## La Classe Convert Coordinator

La classe qui va coordoner un peu tout, c'est celle qu'on instancie si on veut executer une conversion

---

## La Classe Conversion Analyzer

#### Pourquoi pas une classe Analyzer et pas Conversion Analyzer ?
J'imagineais qu'il était possible qu'on ait à rajouter un Analyzer dans une autre partie de l'application, donc définir simplement cette class comme un Analyzer de façon plus générique pourrait poser soucis si on devait, par exemple, analyzer l'url au tout début

#### Ça fé quoi
Le but de la classe est d'analyzer le "path" du fichier (donc le fichier) afin de définir la stratégie que le Convertor va utiliser pour convertir le fichier en question

---

## La Classe Convertor

#### Convertor Strategie hmmm
La classe convertor contient une stratégie, c'est celle qui sera executé lorsqu'on veut convertir, par contre, ce n'est pas la classe convertor qui set la stratégie mais la classe juste en dessous dans le readme (la classe Conversion Analyzer un peu)

---

## La Classe Convertor Strategie

#### Aheum ?
Le but c'est d'avoir un "protocole" qui va permettre de définir pleins de stratégies, et à partir de ça, on va pouvoir l'executer et elle fera des trucs différents en fonction de ce qu'elle est (genre si elle est MP4ToMP3 elle fait des trucs de mp4 to mp3 quoi)

---

## Le UaImAiLeuh (UML)

C'est peut être pas le meilleur des UML, si y a des questions sur la clarté de ce machin, 0 soucis bahaha 