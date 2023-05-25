#!/usr/bin/python3

"""
Handle all RestFul API actions for locations
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, Blueprint
from models import storage
from models.location import Location
from models.service_provider import ServiceProvider


@app_views.route('/locations', strict_slashes=False, methods=['GET'])
def get_all_locations():
    """
    Retrieves the list of all Location objects
    """
    locations = storage.all(Location).values()
    locations_list = [location.to_dict() for location in locations]
    return jsonify(locations_list)


@app_views.route('/locations', strict_slashes=False, methods=['POST'])
def create_location():
    """
    Creates a Location
    """
    if not request.json:
        abort(400, "Not a JSON")

    new_location = Location(**request.json)
    new_location.save()
    return jsonify(new_location.to_dict()), 201


@app_views.route('/locations/<location_id>',
                 strict_slashes=False, methods=['GET'])
def get_location(location_id):
    """
    Retrieves a Location object
    """
    location = storage.get(Location, location_id)
    if not location:
        abort(404)
    return jsonify(location.to_dict())


@app_views.route('/locations/<location_id>',
                 strict_slashes=False, methods=['DELETE'])
def delete_location(location_id):
    """
    Deletes a Location object
    """
    location = storage.get(Location, location_id)
    if not location:
        abort(404)
    location.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/locations/<location_id>',
                 strict_slashes=False, methods=['PUT'])
def put_location(location_id):
    """
    Updates a Location object
    """
    location = storage.get(Location, location_id)
    if not location:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    for key, value in request.json.items():
        if key not in ['id',
                       'created_at', 'updated_at', 'service_provider_id']:
            setattr(location, key, value)
    location.save()
    return jsonify(location.to_dict()), 200


@app_views.route('/locations/<location_id>/service_providers',
                 strict_slashes=False, methods=['GET'])
def get_service_providers_by_location(location_id):
    """
    Retrieves the list of Service Providers within a Location
    """
    location = storage.get(Location, location_id)
    if not location:
        abort(404)

    service_providers = location.service_providers
    service_providers_list = [service_provider.to_dict()
                              for service_provider in service_providers]

    return jsonify(service_providers_list)
