#!/usr/bin/python3

"""
Handles all RESTful API actions for Service Providers
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, Blueprint
from models import storage
from models.service_provider import ServiceProvider
from models.location import Location
from models.reviews import Review
from models.categories import Category


@app_views.route('/service_providers', methods=['GET'], strict_slashes=False)
def query_service_providers():
    """
    Retrieves the list of Service Provider
    objects based on category name, email, or location
    """
    service_providers = storage.all(ServiceProvider)
    category_name = request.args.get('category')
    email = request.args.get('email')
    location_query = request.args.get('location')

    if email:
        # Check if the email exists in the database
        filtered_service_providers = [service_provider for service_provider
                                      in service_providers.values()
                                      if service_provider.email == email]
        if not filtered_service_providers:
            # Email does not exist, return an error message
            return jsonify({'error': 'Service Provider does not exist.'}), 404

        service_providers_list = [service_provider.to_dict()
                                  for service_provider
                                  in filtered_service_providers]

    elif location_query:
        # Filter service providers based on the location
        locations = storage.all(Location).values()
        matching_locations = [loc for loc in locations
                              if (loc.name.lower() == location_query.lower() or
                                  loc.town.lower() == location_query.lower() or
                                  loc.estate.lower() == location_query.lower()
                                  )
                              ]

        if not matching_locations:
            return jsonify({'error':
                            'No providers found'}), 404

        filtered_service_providers = [
            service_provider for service_provider in service_providers.values()
            if service_provider.location_id in [loc.id for
                                                loc in matching_locations]
        ]

        if category_name:
            # Find the category ID based on the category name
            category_id = None
            categories = storage.all(Category).values()
            for category in categories:
                if category.name.lower() == category_name.lower():
                    category_id = category.id
                    break

            if category_id is None:
                return jsonify({'error': 'Category not found'}), 404

            # Filter service providers based on the category ID
            filtered_service_providers = [
                service_provider for service_provider
                in filtered_service_providers
                if service_provider.category_id == category_id
            ]

        service_providers_list = [service_provider.to_dict()
                                  for service_provider
                                  in filtered_service_providers]

    elif category_name:
        # Find the category ID based on the category name
        category_id = None
        categories = storage.all(Category).values()
        for category in categories:
            if category.name.lower() == category_name.lower():
                category_id = category.id
                break

        if category_id is None:
            return jsonify({'error': 'Category not found'}), 404

        # Filter service providers based on the category ID
        filtered_service_providers = [
            service_provider for service_provider in service_providers.values()
            if service_provider.category_id == category_id
        ]

        service_providers_list = [service_provider.to_dict()
                                  for service_provider
                                  in filtered_service_providers]

    else:
        # No category, email, or location param return all service providers
        service_providers_list = [service_provider.to_dict()
                                  for service_provider
                                  in service_providers.values()]

    return jsonify(service_providers_list)


@app_views.route('/service_providers/<service_provider_id>',
                 strict_slashes=False, methods=['GET'])
def get_service_provider(service_provider_id):
    """
    Retrieves a Service Provider object
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if service_provider is None:
        abort(404)
    return jsonify(service_provider.to_dict())


@app_views.route('/service_providers/<service_provider_id>',
                 strict_slashes=False, methods=['DELETE'])
def delete_service_provider(service_provider_id):
    """
    Deletes a Service Provider object
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if service_provider is None:
        abort(404)
    storage.delete(service_provider)
    storage.save()
    return jsonify({}), 200


@app_views.route('/service_providers', strict_slashes=False, methods=['POST'])
def create_service_provider():
    """
    Creates a Service Provider
    """
    json_data = request.get_json()
    if not json_data:
        abort(400, 'Not a JSON')
    if 'name' not in json_data:
        abort(400, 'Missing name')
    if 'description' not in json_data:
        abort(400, 'Missing description')
    if 'location_id' not in json_data:
        abort(400, 'Missing location_id')
    if 'category_id' not in json_data:
        abort(400, 'Missing category_id')
    location = storage.get(Location, json_data['location_id'])
    if location is None:
        abort(404)
    category = storage.get(Category, json_data['category_id'])
    if category is None:
        abort(404)
    new_service_provider = ServiceProvider(**json_data)
    new_service_provider.save()
    return jsonify(new_service_provider.to_dict()), 201


@app_views.route('/service_providers/<service_provider_id>',
                 strict_slashes=False, methods=['PUT'])
def update_service_provider(service_provider_id):
    """
    Updates a Service Provider object
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if service_provider is None:
        abort(404)
    json_data = request.get_json()
    if not json_data:
        abort(400, 'Not a JSON')
    for key, value in json_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(service_provider, key, value)
    service_provider.save()
    return jsonify(service_provider.to_dict()), 200


@app_views.route('/service_providers/<service_provider_id>/reviews',
                 strict_slashes=False, methods=['GET'])
def get_service_provider_reviews(service_provider_id):
    """
    Retrieves the list of all Reviews of a Service Provider
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if service_provider is None:
        abort(404)
    reviews = storage.all(Review).values()
    list_reviews = []
    for review in reviews:
        if review.service_provider_id == service_provider_id:
            list_reviews.append(review.to_dict())
    return jsonify(list_reviews)


@app_views.route('/service_providers/<service_provider_id>/locations',
                 strict_slashes=False, methods=['GET'])
def get_location_by_service_provider(service_provider_id):
    """
    Retrieves the location associated with a specific service provider
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if service_provider is None:
        abort(404)

    location_id = service_provider.location_id
    location = storage.get(Location, location_id)
    if location is None:
        abort(404)

    return jsonify(location.to_dict())


@app_views.route('/service_providers/<service_provider_id>/categories',
                 strict_slashes=False, methods=['GET'])
def get_category_by_service_provider(service_provider_id):
    """
    Retrieves the category associated with a specific service provider
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if service_provider is None:
        abort(404)

    category_id = service_provider.category_id
    category = storage.get(Category, category_id)
    if category is None:
        abort(404)

    return jsonify(category.to_dict())
