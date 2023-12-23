import sys
from pymongo import MongoClient


def connect_to_mongodb():
    client = MongoClient("mongodb://mongodb:27017/")
    db = client["dictionary-ca"]
    return db


def query_word(word):
    db = connect_to_mongodb()
    collection = db["words"]

    result = collection.find_one({"word": word})
    return result


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python app.py <word>")
        sys.exit(1)

    word = sys.argv[1]
    result = query_word(word)

    if result:
        print(f"Word {word} is in the dictionary")
    else:
        print(f"Word {word} is NOT in the dictionary")
