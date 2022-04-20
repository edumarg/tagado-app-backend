import pymongo


def connect_to_db():
    client = pymongo.MongoClient \
        (host="mongodb+srv://developer:{password}@cluster0.juo1t.mongodb.net/NLP?retryWrites=true&w=majority&ssl=true"
              "&ssl_cert_reqs=CERT_NONE".format(password="devo1234"), connect=False)
    return client


def get_all_data(client):
    data_dict = {}
    data = client['NLP']['TERMS'].find({})
    for term in data:
        term['_id'] = str(term['_id'])
        data_dict[term['_id']] = term
    # print(list(data))
    return data_dict


def add_new_terms(term, client):
    return client['NLP']['TERMS'].insert_one(term)


def get_terms_count(type, client):
    pass
