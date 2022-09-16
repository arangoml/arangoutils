import string
from arango import ArangoClient
from arango.database import  StandardDatabase
from collection_attributes import CollectionAttributes
from graph_attributes import GraphAttributes

class MetaGraphGenerator:
    def __init__(self, db: StandardDatabase) -> None:
        self.db = db
                
    def getCollectionAttributes(self, coll_name: string) -> CollectionAttributes:
        coll = self.db.collection(coll_name)
        ca = CollectionAttributes()
        ca.name = coll.name
        ca.db_name = coll.db_name
        ca.properties = coll.properties()
        ca.revision = coll.revision()
        ca.statistics = coll.statistics()
        ca.checksum = coll.checksum()
        ca.count = coll.count()
        return ca

    def getGraphAttributes(self, graph_name: string) -> GraphAttributes:
        gr = self.db.graph(graph_name)
        ga = GraphAttributes()
        ga.name = gr.name
        ga.db_name = gr.db_name
        ga.vertex_collections = gr.vertex_collections()
        ga.edge_definitions = gr.edge_definitions()
        return ga