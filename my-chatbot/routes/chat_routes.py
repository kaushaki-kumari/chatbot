from flask import Blueprint, request, jsonify
from services.ai_service import generate_answer
from services.db_service import collection

chat_bp = Blueprint("chat_routes", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    question = request.json.get("question")
    if not question:
        return jsonify({"error": "No question"}), 400

    # Read user saved data
    all_data = [item["details"] for item in collection.find()]

    if not all_data:
        return jsonify({"answer": "No saved any information found."})

    context = "\n".join(all_data)

    answer = generate_answer(question, context)
    return jsonify({"answer": answer})