from elasticsearch import Elasticsearch
import json
import os

es = Elasticsearch([{'host': '34.93.110.192', 'port': 9200}])

index_name = "people"

number_of_results = 50

def get_json(file_name):

    json_file = open(file_name)
    json_data = json.load(json_file)

    return json_data

def get_all_files():

    files = os.listdir(".")

    files = [x for x in files if 'json' in x]

    return files

def test_search():

    body = {
        "from":0,
        "size":number_of_results,
        "query": {
        "query_string" : {
            "query" : "*like*"
            }
        } 
    }

    res = es.search(index = index_name, body = body)
    count = 0
    try:
        for i in range(number_of_results):
            count+=1
            print(res['hits']['hits'][i]["_source"])
    except:
        print(f"\n{count - 1} Results Fetched")

def insert_data():

    file_names = get_all_files()
    count = 1

    for i in file_names:

        data = get_json(f'./{i}')
        es.index(index = index_name , id = count, body = data)
        count += 1

    print('Done inserting!')


if __name__ == '__main__':

    insert_data()

    test_search()

    pass