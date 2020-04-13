from elasticsearch import Elasticsearch
from espandas import Espandas

es = Elasticsearch(
    ['localhost', 'otherhost'],
    scheme="https",
    port=9200,
    ssl_context=context,
)

esp = Espandas()
esp.es_write(df, INDEX, TYPE)

# read index
# write index
def write_index(index):
	if not exists(index=index):
		es.create(index=index)

# get schema
#es.get() ou es.get_mapping()

# write schema
#put_mapping