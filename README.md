imdb-dump
=========

1. Use the neo4j batch-import at 20 by jexp 
2. run python create-graph.py
3. ensure that the neo4j.properties file (under neo4j/bin/libexec/bin/conf) has allow_store_upgrade=true
4. run the maven script: 
    mvn clean compile exec:java -Dfile.encoding=UTF-8 -Dexec.mainClass="org.neo4j.batchimport.Importer" -Dexec.args="graph.db nodes.csv rels.csv"
4. replace existing graph.db folder in Neo4j with the graph.db folder created by the batch importer
5. that's it!

