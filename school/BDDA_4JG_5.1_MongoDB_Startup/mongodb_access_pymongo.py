from pprint import pprint
from datetime import datetime

import pymongo
from bson import ObjectId
from pymongo import MongoClient


def test():
    client = MongoClient("mongodb://10.115.2.20:8017/", username='mongoadmin', password='start123')
    db = client.crm
    collection = db.contacts
    posts = db.posts
    posts.delete_many({}) # Clear collection
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.utcnow()}

    post_id = posts.insert_one(post).inserted_id
    prnt(post_id)
    prnt(db.list_collection_names())
    prnt(posts.find_one())
    print('Find One author: ')
    prnt(posts.find_one({"author": "Mike"}))
    print('Find One ID: ')
    prnt(posts.find_one({"_id": post_id}))
    post_id_string = str(post_id)
    print(posts.find_one({"_id": post_id_string}))
    prnt(posts.find_one({"_id": ObjectId(post_id_string)}))
    new_posts = [{"author": "Mike",
                  "text": "Another post!",
                  "tags": ["bulk", "insert"],
                  "date": datetime(2009, 11, 12, 11, 14)},
                 {"author": "Eliot",
                  "title": "MongoDB is fun",
                  "text": "and pretty easy too!",
                  "date": datetime(2009, 11, 10, 10, 45)}]
    result = posts.insert_many(new_posts)

    prnt(result.inserted_ids)
    for post in posts.find():
        pprint(post)

    prnt()
    for post in posts.find({"author": "Mike"}):
        pprint(post)
    prnt()
    prnt(posts.count_documents({}))
    prnt(posts.count_documents({"author": "Mike"}))

    d = datetime(2009, 11, 12, 12)
    for post in posts.find({"date": {"$lt": d}}).sort("author"):
        pprint(post)
    prnt()

    db.profiles.delete_many({})
    result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
                                      unique=True)
    prnt(result)
    sorted(list(db.profiles.index_information()))
    user_profiles = [
        {'user_id': 211, 'name': 'Luke'},
        {'user_id': 212, 'name': 'Ziltoid'}]
    prnt(db.profiles.insert_many(user_profiles))
    new_profile = {'user_id': 213, 'name': 'Drew'}
    duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
    prnt(db.profiles.insert_one(new_profile))  # This is fine.
    #prnt(db.profiles.insert_one(duplicate_profile))
    # This not fine


def prnt(text=None):
    if text is not None:
        pprint(text)
    print("-----------------------------------------------------")


if __name__ == "__main__":
    test()
