# !pip install elasticsearch==7.6
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '34.93.110.192', 'port': 9200}])

# es.indices.create(index="ctc")

# doc_1 = {"city": "Paris", "country": "France"}
# doc_2 = {"city": "Vienna", "country": "Austria"}
# doc_3 = {"city": "London", "country": "England"}


# es.index(index="cities", body=doc_1)
# es.index(index="cities", body=doc_2)
# es.index(index="cities", body=doc_3)
words = ['tree','apple','orange']

for word in words:


    body = {
        "from":0,
        "size":2000,
        "query": {
            "query_string" : {
                "query" : f"*{word}*"
                }
        } 
    }


res = es.search(index="cities", body=body)

print(res['hits']['hits'])