from flask import Blueprint, jsonify
from db.connection import execute_query
from utils.status_checker import get_device_status
from datetime import timezone

devices_bp = Blueprint("devices", __name__)

@devices_bp.route("/<int:company_id>", methods=["GET"])
def get_devices(company_id):
    query = """
        SELECT d.id, d.name,
               MAX(r.reading_time) AS last_reading
        FROM devices d
        LEFT JOIN device_readings r ON d.id = r.device_id
        WHERE d.company_id = %s
        GROUP BY d.id, d.name
        ORDER BY d.id;
    """

    rows = execute_query(query, (company_id,), fetch=True)
    if rows is None:
        return jsonify({"error": "Database query failed"}), 500

    devices = []
    for device_id, name, last_reading in rows:
        if last_reading and last_reading.tzinfo is None:
            last_reading = last_reading.replace(tzinfo=timezone.utc)

        status = get_device_status(last_reading)

        devices.append({
            "id": device_id,
            "name": name,
            "last_reading": last_reading.isoformat() if last_reading else None,
            "status": status
        })

    return jsonify({"success": True, "devices": devices}), 200
