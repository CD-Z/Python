import pymongo


def test():
    myclient = pymongo.MongoClient("mongodb://10.115.2.20:8017/", username='mongoadmin', password='start123')
    mydb = myclient["crm"]
    mycol = mydb["contacts"]
    myquery = { "name": "Maria" }
    mydoc = mycol.find(myquery)
    mydoc = mycol.find()
    for x in mydoc:
        print('Id:', x["_id"], ",Name:", x["name"])


if __name__ == "__main__":
    test()
