from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username="aacuser", password="SNHU1234"):
        """Initialize the MongoDB client and connect to the AAC animals collection."""

        # Connection variables for the MongoDB database
        self.USER = username
        self.PASS = password
        self.HOST = "localhost"
        self.PORT = 27017
        self.DB = "aac"
        self.COL = "animals"

        # Initialize the connection to MongoDB using the aacuser account
        self.client = MongoClient(
            "mongodb://%s:%s@%s:%d/?authSource=admin"
            % (self.USER, self.PASS, self.HOST, self.PORT)
        )

        # Select the database and collection
        self.database = self.client[self.DB]
        self.collection = self.database[self.COL]

    def create(self, data):
        """Insert one document into the animals collection."""

        if data is not None and isinstance(data, dict):
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except PyMongoError as error:
                print("Create operation failed:", error)
                return False
        else:
            raise ValueError("The data parameter must be a non empty dictionary.")

    def read(self, query):
        """Read documents from the animals collection using a query."""

        if query is not None and isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except PyMongoError as error:
                print("Read operation failed:", error)
                return []
        else:
            raise ValueError("The query parameter must be a dictionary.")

    def update(self, query, new_values, update_many=False):
        """Update one or many documents in the animals collection."""

        if query is not None and isinstance(query, dict):
            if new_values is not None and isinstance(new_values, dict):
                try:
                    update_data = {"$set": new_values}

                    if update_many:
                        result = self.collection.update_many(query, update_data)
                    else:
                        result = self.collection.update_one(query, update_data)

                    return result.modified_count
                except PyMongoError as error:
                    print("Update operation failed:", error)
                    return 0
            else:
                raise ValueError("The new_values parameter must be a dictionary.")
        else:
            raise ValueError("The query parameter must be a dictionary.")

    def delete(self, query, delete_many=False):
        """Delete one or many documents from the animals collection."""

        if query is not None and isinstance(query, dict):
            try:
                if delete_many:
                    result = self.collection.delete_many(query)
                else:
                    result = self.collection.delete_one(query)

                return result.deleted_count
            except PyMongoError as error:
                print("Delete operation failed:", error)
                return 0
        else:
            raise ValueError("The query parameter must be a dictionary.")


# Alias added so the class can also be imported as CRUD if needed.
CRUD = AnimalShelter