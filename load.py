import pandas as pd
from elasticsearch7 import Elasticsearch
from elasticsearch7.helpers import bulk


df = pd.read_csv('/home/veljko/Desktop/zadatak1/users.csv')

es = Elasticsearch('http://localhost:9200')

if not es.indices.exists(index="user-index"):
    es.indices.create(index='user-index',body={})

documents = df.to_dict(orient='records')
bulk(es, documents, index='user-index', raise_on_error=True)