from elasticsearch import Elasticsearch
es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()
import pprint

# es.indices.create(index="first_index")

# a = es.indices.exists(index="first_index")

# print(a)

# es.indices.delete(index="first_index")

# a = es.indices.exists(index="first_index")

# print(a)

# doc_1 = {"city": "Paris", "country": "France"}
# doc_2 = {"city": "Vienna", "country": "Austria"}
# doc_3 = {"city": "London", "country": "England"}

# es.index(index="cities", id=1, body=doc_2)

# res = es.get(index="cities",id=1)

# print(res)

# print(res["_source"])

# doc_1 = {"sentence":"Hack COVID-19 is amazing!"}
# doc_2 = {"sentence":"Hack-Quarantine is stunning!"}

# es.index(index="english", id=1, body=doc_1)
# es.index(index="english", id=2, body=doc_2)

# body = {
#     "from":0,
#     "size":2,
#     "query": {
#         "match": {
#             "sentence":"Hack"
#         }
#     }
# }

# res = es.search(index="english", body=body)

# print(res)

# match_phrase 

# body = {
#     "from":0,
#     "size":2,
#     "query": {
#         "match_phrase": {
#             "sentence":"Hack"
#         }
#     }
# }

# res = es.search(index="english", body=body)

# pprint.pprint(res["hits"]['hits'][0]["_source"])

 
# body = {
#     "from":0,
#     "size":2,
#     "query": {
#         "bool": {
#             "must_not": {
#                 "match": {
#                     "sentence":"COVID-19"
#                 }
#             },
#             "should": {
#                 "match": {
#                     "sentence": "Hack"
#                 }
#             }
#         }
#     }
# }

# res = es.search(index="english", body=body)
# pprint.pprint(res["hits"]['hits'][0]["_source"])

# body = {
#     "from":0,
#     "size":3,
#     "query": {
#         "regexp": {
#             "sentence":".*"
#         }
#     }
# }

# res = es.search(index="english", body=body)
# res





