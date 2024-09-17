# German_language_synonym_patterns

Explore Synographs - A graph-based synonym pattern search tool.

## Context

Language is a complex and interconnected system where words can have multiple meanings (polysemy), and different words can express the same idea (synonymy). To model these relationships, the provided Python code constructs a graph that captures the nuances of language semantics. In this graph:

- Vertices (Nodes): Each vertex represents a set of synonyms—words that share a common meaning.

- Edges (Connections): Edges link vertices that have one or more words in common, highlighting the overlap between different synonym sets.

By leveraging Dijkstra's shortest path algorithm, the code can find the most efficient path between any two words. This path represents the closest semantic relationship through shared synonyms, effectively navigating the web of language meanings. 
The following figure illustrates the approach.

![graph](explaination_draw.png)

The german language is used with a synonym dataset from https://www.openthesaurus.de/.

## Deployment

The code is deployed web-based under https://www.synographs.herokuapp.com. 
