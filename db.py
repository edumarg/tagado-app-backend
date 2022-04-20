import pymongo


def connect_to_db():
    client = pymongo.MongoClient \
        (host="mongodb+srv://developer:{password}@cluster0.juo1t.mongodb.net/NLP?retryWrites=true&w=majority&ssl=true"
              "&ssl_cert_reqs=CERT_NONE".format(password="devo1234"), connect=False)
    return client


def get_all_data(client):
    data_array = []
    data = client['NLP']['TERMS'].find({})
    for term in data:
        del term['_id']
        data_array.append(term)
    return data_array


def add_new_terms(term, client):
    return client['NLP']['TERMS'].insert_one(term)


def get_terms_count(my_type, client):
    my_terms = {}
    data = client['NLP']['TERMS'].find({"type": my_type})
    for value in data:
        del value['_id']
        for term in value["terms"]:
            if term not in my_terms:
                my_terms[term] = 1
            else:
                my_terms[term] += 1
    return my_terms
