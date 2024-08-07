from flask import Flask, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

MONGO_URI = 'mongodb+srv://aryan:6nqInRhcdlVGiJxm@cluster0.q9ozewg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
DB_NAME = 'db'
COLLECTION_NAME = 'projects'

def connect_to_mongo():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection

@app.route('/get_project/<project_id>', methods=['GET'])
def get_project(project_id):
    collection = connect_to_mongo()
    project = collection.find_one({'_id': project_id})
    if project:
        project['_id'] = str(project['_id'])  # Convert ObjectId to string for JSON serialization
        return jsonify(project)
    else:
        return jsonify({'error': 'Project not found'}), 404

@app.route('/get_all_projects', methods=['GET'])
def get_all_projects():
    collection = connect_to_mongo()
    projects = list(collection.find())
    for project in projects:
        project['_id'] = str(project['_id'])  # Convert ObjectId to string for JSON serialization
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)
