#!/usr/bin/python3

"""
Defines the routes for the service providers
"""

from flask import jsonify, request
from models.service_provider import ServiceProvider
from models import storage
from models.categories import Category
from models.location import Location
from models.reviews import Review
from flask import Flask


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database storage"""
    storage.close()


@app.route('/service-providers', methods=['POST'], strict_slashes=False)
def create_service_provider():
    """
    Creates a new service provider
    """
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400

    required_fields = ['name', 'phone_number', 'password']
    for field in required_fields:
        if field not in request.json:
            return jsonify({'error': f'Missing {field}'}), 400

    data = request.get_json()
    category_id = data['category_id']
    location_id = data['location_id']

    category = storage.get(Category, category_id)
    if not category:
        return jsonify({'error': 'Invalid category ID'}), 400

    location = storage.get(Location, location_id)
    if not location:
        return jsonify({'error': 'Invalid location ID'}), 400

    data = request.get_json()
    service_provider = ServiceProvider(**data)
    service_provider.save()
    return jsonify(service_provider.to_dict()), 201


@app.route('/service-providers/<service_provider_id>',
           methods=['GET'], strict_slashes=False)
def get_service_provider(service_provider_id):
    """
    Retrieves a service provider by ID
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if not service_provider:
        return jsonify({'error': 'Service Provider not found'}), 404
    return jsonify(service_provider.to_dict())


@app.route('/service-providers', methods=['GET'], strict_slashes=False)
def get_all_service_providers():
    """
    Retrieves all service providers
    """
    service_providers = storage.all(ServiceProvider).values()
    service_providers_dict = [sp.to_dict() for sp in service_providers]
    return jsonify(service_providers_dict)


@app.route('/service-providers/<service_provider_id>',
           methods=['DELETE'], strict_slashes=False)
def delete_service_provider(service_provider_id):
    """
    Deletes a service provider by ID
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if not service_provider:
        return jsonify({'error': 'Service Provider not found'}), 404
    storage.delete(service_provider)
    storage.save()
    return jsonify({'message': 'Service Provider deleted'})


@app.route('/service-providers/<service_provider_id>',
           methods=['PUT'], strict_slashes=False)
def update_service_provider(service_provider_id):
    """
    Updates a service provider by ID
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if not service_provider:
        return jsonify({'error': 'Service Provider not found'}), 404

    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400

    data = request.get_json()

    for key, value in data.items():
        setattr(service_provider, key, value)

    storage.save()
    return jsonify(service_provider.to_dict())


@app.route('/service-providers/category/<category_id>',
           methods=['GET'], strict_slashes=False)
def get_service_providers_by_category(category_id):
    """
    Retrieves service providers by category
    """
    category = storage.get(Category, category_id)
    if not category:
        return jsonify({'error': 'Category not found'}), 404

    service_providers = storage.all(ServiceProvider).values()
    service_providers_filtered = [sp.to_dict()
                                  for sp in service_providers
                                  if sp.category_id == category_id]

    if not service_providers_filtered:
        return jsonify({'error': 'No service providers in that category'}), 404

    return jsonify(service_providers_filtered)


@app.route('/service-providers/location/<location_id>',
           methods=['GET'], strict_slashes=False)
def get_service_providers_by_location(location_id):
    """
    Retrieves service providers by location
    """
    location = storage.get(Location, location_id)
    if not location:
        return jsonify({'error': 'Location not found'}), 404

    service_providers = storage.all(ServiceProvider).values()
    service_providers_filtered = [sp.to_dict()
                                  for sp in service_providers
                                  if sp.location_id == location_id]

    if not service_providers_filtered:
        return jsonify({'error': 'No service providers in that location'}), 404

    return jsonify(service_providers_filtered)


@app.route('/service-providers/<service_provider_id>/category',
           methods=['GET'], strict_slashes=False)
def get_service_provider_category(service_provider_id):
    """
    Retrieves the category of a service provider
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if not service_provider:
        return jsonify({'error': 'Service Provider not found'}), 404

    category = service_provider.category
    if not category:
        return jsonify({'error': 'Category not found for provider'}), 404

    return jsonify(category.to_dict())


@app.route('/service-providers/<service_provider_id>/locations',
           methods=['GET'], strict_slashes=False)
def get_service_provider_locations(service_provider_id):
    """
    Retrieves the locations of a service provider
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if not service_provider:
        return jsonify({'error': 'Service Provider not found'}), 404

    location_id = service_provider.location_id
    location = storage.get(Location, location_id)

    if not location:
        return jsonify({'error': 'Location not found for  provider'}), 404

    return jsonify(location.to_dict())


@app.route('/service-providers/<service_provider_id>/reviews',
           methods=['GET'], strict_slashes=False)
def get_service_provider_reviews(service_provider_id):
    """
    Retrieves the reviews of a service provider
    """
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if not service_provider:
        return jsonify({'error': 'Service Provider not found'}), 404
    reviews = service_provider.reviews
    reviews_dict = [review.to_dict() for review in reviews]
    return jsonify(reviews_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
