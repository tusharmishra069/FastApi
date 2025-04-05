from pymongo import MongoClient  # Importing the MongoClient class from pymongo to interact with MongoDB

# MongoDB connection URI with credentials and cluster information
MONGO_URI = "mongodb+srv://tusharmishra069:tushar%4054321@test.u8rbaej.mongodb.net/?retryWrites=true&w=majority&appName=notes"

# Establishing a connection to the MongoDB cluster
conn = MongoClient(MONGO_URI)