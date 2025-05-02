from mongomock.mongo_client import MongoClient
from io import BytesIO
import pickle
from datetime import datetime, timezone

class InMemoryStore:
    _db = None
    _model = None

    @classmethod
    def _get_db(cls):
        if cls._db is None:
            client = MongoClient()
            cls._db = client.get_database("memory_db")
        return cls._db

    @classmethod
    def set_model(cls, model):
        cls._model = model

    @classmethod
    def get_model(cls):
        return cls._model
    
    @classmethod
    def add_history(cls, record: dict):
        db = cls._get_db()
        db.predictions.insert_one(record)

    @classmethod
    def get_history(cls):
        db = cls._get_db()
        return list(db.predictions.find({}, {'_id': 0}))
