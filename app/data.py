from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient

class Database:

    def __init__(self):
        load_dotenv()
        self.database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Bandersnatch"]
        self.collection = self.database.get_collection("Monsters")

    def seed(self, amount):
        """insert the specified number of documents into the collection"""
        self.collection.insert_many([Monster().to_dict() for _ in range(amount)])
    
    def reset(self):
        """deletes all documents from the collection"""
        self.collection.delete_many({})

    def count(self) -> int:
        """returns the number of documents in the collection"""
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """returns a DataFrame containing all documents in the collection"""
        return DataFrame(self.collection.find())

    def html_table(self) -> str:
        """returns an HTML table representation of the DataFrame (or None)"""
        return self.dataframe().to_html() if self.count() else None

if __name__ == '__main__':
    db = Database()