from flask import Blueprint, request, jsonify
from services.db_service import collection
from bson import ObjectId

data_bp = Blueprint("data_routes", __name__)

#CREATE
@data_bp.route("/save", methods=["POST"])
def save_data():
    data = request.json.get("details")
    if not data:
        return jsonify({"error": "No details"}), 400
    
    result = collection.insert_one({"details": data})
    return jsonify({"id": str(result.inserted_id)})

#READ 
@data_bp.route("/list", methods=["GET"])
def list_data():
    items = []
    for i in collection.find():
        items.append({"id": str(i["_id"]), "details": i["details"]})
    return jsonify(items)

#DELETE
@data_bp.route("/delete/<id>", methods=["DELETE"])
def delete_data(id):
    collection.delete_one({"_id":ObjectId(id)})
    return jsonify({"status": "deleted"})

#UPDATE
@data_bp.route("/update/<id>", methods=["PUT"])
def update_data(id):
    new_details = request.json.get("details")
    collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {"details": new_details}}
    )
    return jsonify({"status": "updated"})
