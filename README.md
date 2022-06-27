# German_language_synonym_patterns

Context:

Language sometimes offers different words for the same meaning. This is widely known as synonyms. Furthermore, there 
are words, which can be used for different meanings depending on the context the speaker uses them. This Python codes 
builds a graph with synonym sets as vertices and connects vertices including one or more same words with edges. 
A shortest path algorithm (dijekstra implemented) can be used to find the shortest path from one word to another 
with the help of their individual synonyms. A small picture shall help to understand the idea.

![graph](explaination_draw.png)

The german language is used with a synonym dataset from https://www.openthesaurus.de/

Usage:

The main function includes examples with different pairs of words, which can be changed by the user. Call the 
Script main.py and see the output in the console. The example below shows the console output for the pair (Fessel, Zettel)

Example:

Basic Information <br>
start word is found in 3 different word-patterns <br>
end word is found in 2 different word-patterns <br>
Strting Node: <br>
blatt <br>
Task: <br>
Finde den kürzesten Weg zum Wort: fessel <br>
blatt ist ein Synonym von ['zettel'] <br>
Das Wort zettel im Kontext von ['papierblatt', 'blattpapier', 'papier', 'zettel', 'fetzenpapier', 'seite', 'wisch', 'bogen', 'blatt'] wird auch als ['zettel'] Im Kontext von ['aufzug', 'werft', 'zettel', 'kettfaden', 'kette'] verwendet <br>
Das Wort kette ist ein Synonym des Wortes {'zettel'} in diesem neuen Kontext <br>
Das Wort kette im Kontext von ['aufzug', 'werft', 'zettel', 'kettfaden', 'kette'] wird auch als ['kette'] Im Kontext von ['handfessel', 'kette', 'handschelle', 'fessel'] verwendet <br>
Das Wort fessel ist ein Synonym des Wortes {'kette'} in diesem neuen Kontext <br>
Das Wort fessel im Kontext von ['handfessel', 'kette', 'handschelle', 'fessel'] wird auch als ['fessel'] Im Kontext von ['fußgelenk', 'fußknöchel', 'fessel', 'knöchel'] verwendet <br>
{'fessel'} ist ein Synonym von fessel im neu gewählten Kontext <br>
Endknoten gefunden (fessel) <br>


