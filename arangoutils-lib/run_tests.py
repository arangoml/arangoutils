import string
from arango import ArangoClient
from arango.database import  StandardDatabase
from meta_graph_gen import MetaGraphGenerator

def getDB() -> StandardDatabase:
    return ArangoClient(hosts="http://localhost:8529").db("testdb", username="root", password= "passwd")

def test_getCollectionAttributes(o: MetaGraphGenerator) -> None:
    col_name = "internationalHighway"
    ca = o.getCollectionAttributes(col_name)
    print('---Attributes of ' + col_name+'---')
    print('Name: ' + ca.name)
    print('DB: ' + ca.db_name)
    print('Properties:')
    print(ca.properties)
    print('Revision: ' + ca.revision)
    print('Statistics:')
    print(ca.statistics)
    print('Checksum: ' + ca.checksum)
    print('Count:')
    print(ca.count)
    
def test_getGraphAttributes(o: MetaGraphGenerator) -> None:
    graph_name = "routeplanner"
    ga = o.getGraphAttributes(graph_name)
    print('---Attributes of ' + graph_name +'---')
    print('Name: ' + ga.name)
    print('DB: ' + ga.db_name)
    print('Vertex Collections:')
    print(ga.vertex_collections)
    print('Edge Definitions:')
    print(ga.edge_definitions)

db = getDB()
mgg = MetaGraphGenerator(db)
test_getCollectionAttributes(mgg)
test_getGraphAttributes(mgg)