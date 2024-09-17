# German_language_synonym_patterns

Context:

Language sometimes offers different words for the same meaning. This is widely known as synonyms. Furthermore, there 
are words, which can be used for different meanings depending on the context the speaker uses them. This Python code
builds a graph with synonym sets as vertices and connects vertices including one or more same words with edges. 
A shortest path algorithm (dijekstra implemented) can be used to find the shortest path from one word to another 
with the help of their individual synonyms. A small picture shall help to understand the idea.

![graph](explaination_draw.png)

The german language is used with a synonym dataset from https://www.openthesaurus.de/

Usage:

The main function includes examples with different pairs of words, which can be changed by the user. Call the 
Script main.py and see the output in the console. The example below shows the console output for the pair (Unsicherheit, Gewissenheit)

Deployment:

The code is deployed web-based under synographs.herokuapp.com
