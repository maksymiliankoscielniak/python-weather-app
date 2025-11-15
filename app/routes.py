from flask import Blueprint, request, jsonify
from .services import get_weather_data
from .services import get_city_suggestions

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

@api.route('/cities', methods=['GET'])
def get_cities():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query is required"}), 400
    
    city_suggestions = get_city_suggestions(query)
    if city_suggestions is None:
        return jsonify({"error": "No suggestions found"}), 404

    return jsonify(city_suggestions)