from espandas import Espandas
import elasticsearch
import pandas as pd


data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)
print(df)

es =  elasticsearch.Elasticsearch(
    ['localhost'],
    scheme="https",
    port=9200,
    #ssl_context=context,
)


#esp = Espandas()
#esp.es_write(df, "index.test", "_doc")

# read index
# write index
def write_index(index_name, es, data):
	if not es.exists(index=index_name):
		es.create(index=index_name)
	#es.index(index, data)
	elasticsearch.helpers.bulk(es, data)
# get schema
#es.get() ou es.get_mapping()

# write schema
#put_mapping

#res = es.search(index="test-index", body={"query": {"match_all": {}}})
#- validate_query

write_index("teste", es, df)