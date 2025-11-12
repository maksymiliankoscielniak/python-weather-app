from flask import Blueprint, request, jsonify
from .services import get_weather_data

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400
    
    weather_data = get_weather_data(city)
    if weather_data is None:
        return jsonify({"error": "City not found"}), 404

    return jsonify(weather_data)