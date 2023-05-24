#!/usr/bin/python3

"""
Flask app for the Location class
"""

from flask import Flask, jsonify, request
from models.location import Location
from models import storage
from models.engine.db_storage import DBStorage
from models.service_provider import ServiceProvider

app = Flask(__name__)


# Close storage
@app.teardown_appcontext
def teardown_db(exception):
    """ Closes storage """
    storage.close()


# Error handler
@app.errorhandler(404)
def page_not_found(error):
    response = {
        'message': '404 - Page not found'
    }
    return jsonify(response), 404


@app.route('/locations', methods=['GET'], strict_slashes=False)
def get_locations():
    """
    Retrieves a list of all Location objects
    """
    locations = storage.all(Location).values()
    locations_list = [location.to_dict() for location in locations]
    return jsonify(locations_list)


@app.route('/locations/<location_id>', methods=['GET'], strict_slashes=False)
def get_location(location_id):
    """
    Retrieves a Location object based on ID
    """
    location = storage.get(Location, location_id)
    if location:
        return jsonify(location.to_dict())
    else:
        return jsonify({'error': 'Location not found'}), 404


@app.route('/locations', methods=['POST'], strict_slashes=False)
def create_location():
    """
    Creates a new Location object
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    name = data.get('name')
    county = data.get('county')
    town = data.get('town')
    estate = data.get('estate')

    if not name or not county or not town or not estate:
        return jsonify({'error': 'Missing required fields'}), 400

    location = Location(name=name, county=county, town=town, estate=estate)
    storage.new(location)
    storage.save()

    return jsonify(location.to_dict()), 201


@app.route('/locations/<location_id>', methods=['PUT'], strict_slashes=False)
def update_location(location_id):
    """
    Updates a Location object based on ID
    """
    location = storage.get(Location, location_id)
    if not location:
        return jsonify({'error': 'Location not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    location.update(**data)
    storage.save()

    return jsonify(location.to_dict())


@app.route('/locations/<location_id>', methods=['DELETE'],
           strict_slashes=False)
def delete_location(location_id):
    """
    Deletes a Location object based on ID
    """
    location = storage.get(Location, location_id)
    if not location:
        return jsonify({'error': 'Location not found'}), 404

    storage.delete(location)
    storage.save()

    return jsonify({'message': 'Location deleted'})


@app.route('/locations/<location_id>/service_providers',
           methods=['GET'], strict_slashes=False)
def get_service_providers_by_location(location_id):
    """
    Retrieves the list of service providers in a location
    """
    location = storage.get(Location, location_id)
    if not location:
        return jsonify({'error': 'Location not found'}), 404

    service_providers = storage.all(ServiceProvider).values()
    service_providers_list = [
        service_provider.to_dict()
        for service_provider in service_providers
        if service_provider.location_id == location_id
    ]

    return jsonify(service_providers_list)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
