import elasticsearch
import pandas as pd


data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)

es =  elasticsearch.Elasticsearch(
    ['localhost'],
    scheme="http",
    port=9200,
)

# Create index if not existent
def write_index(index_name, data, id="_id"):
	#es.helpers.bulk(es, data)
    res = es.index(index=index_name,body=data.to_json())
    return res.get(id)

def exists(index_name):
    return es.indices.exists(index=index_name)

def create_index(index_name):
    es.indices.create(index=index_name)

# get schema
#es.get() ou es.get_mapping()

# write schema
#put_mapping

# read index
def get_all(index_name):
    res = es.search(index=index_name, body={"query": {"match_all": {}}})
    print(res.get("hits").get("hits"))
    return pd.DataFrame(res.get("hits").get("hits"))

def search(es_object, index_name, search):
    res = es.search(index=index_name, body=search)
#- validate_query

write_index("teste", df)
elastic_df = get_all("teste")

print ('elastic_df:', type(elastic_df), "\n")
print (elastic_df) # print out the DF object's contents