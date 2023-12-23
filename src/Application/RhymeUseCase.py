from pymongo import MongoClient
from Application.RhymeRequest import RhymeRequest
from Application.RhymeResponse import RhymeResponse


class RhymeUseCase:

    def execute(self, request: RhymeRequest) -> RhymeResponse:
        word = self._query_word(request.word)
        result = []
        if word:
            result.append(word)

        return RhymeResponse(words=result)

    def _query_word(self, word):
        db = self._connect_to_mongodb()
        collection = db["words"]

        result = collection.find_one({"word": word})
        return result

    def _connect_to_mongodb(self):
        client = MongoClient("mongodb://mongodb:27017/")
        db = client["dictionary-ca"]
        return db
