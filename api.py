from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from elasticsearch7 import Elasticsearch


app = FastAPI()
es = Elasticsearch('http://localhost:9200')

@app.get("/users")
def get_customer():
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match_all": {
                        }
                    }
                ]
            }
        },
        "from": 0,
        "size": 100
    }
    res = es.search(index="user-index", body=body)
    return res['hits']['hits']


@app.get("/user/{name}")
def get_user_by_id(name: str):
    body =  {
        "query": {
            "bool": {
            "should": [
                {
                "query_string": {
                    "fields": ["name", "second_name"],
                    "query": name + "*"
                }
                }
            ]
            }
        },
        "from": 0,
        "size": 100
        }

    res = es.search(index="user-index", body=body)
    return res['hits']['hits']