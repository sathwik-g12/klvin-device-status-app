from flask import Blueprint, jsonify
from db.connection import execute_query

companies_bp = Blueprint("companies", __name__)

@companies_bp.route("", methods=["GET"])
def get_companies():
    rows = execute_query("SELECT id, name FROM companies ORDER BY id;", fetch=True)
    if rows is None:
        return jsonify({"error": "Database error"}), 500

    companies = [{"id": r[0], "name": r[1]} for r in rows]
    return jsonify({"success": True, "companies": companies}), 200
