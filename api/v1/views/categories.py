#!/usr/bin/python3

"""
Handles all default RESTful API requests for the categories model
"""

from api.v1.views import app_views
from flask import Blueprint, jsonify, request
from models.categories import Category
from models import storage
from models.service_provider import ServiceProvider


@app_views.route('/categories', methods=['GET'],
                 strict_slashes=False)
def get_categories():
    """
    Returns all categories
    """
    categories = storage.all(Category)
    return jsonify([category.to_dict() for category in categories.values()])


@app_views.route('/categories/<category_id>', methods=['GET'],
                 strict_slashes=False)
def get_category(category_id):
    """
    Returns a category based on its ID
    """
    category = storage.get(Category, category_id)
    if category is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(category.to_dict())


@app_views.route('/categories/<category_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_category(category_id):
    """
    Deletes a category based on its ID
    """
    category = storage.get(Category, category_id)
    if category is None:
        return jsonify({'error': 'Not found'}), 404
    category.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/categories', methods=['POST'],
                 strict_slashes=False)
def create_category():
    """
    Creates a category
    """
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in request.json:
        return jsonify({'error': 'Missing name'}), 400
    category = Category(**request.get_json())
    category.save()
    return jsonify(category.to_dict()), 201


@app_views.route('/categories/<category_id>', methods=['PUT'],
                 strict_slashes=False)
def update_category(category_id):
    """
    Updates a category based on its ID
    """
    category = storage.get(Category, category_id)
    if category is None:
        return jsonify({'error': 'Not found'}), 404
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(category, key, value)
    category.save()
    return jsonify(category.to_dict()), 200


@app_views.route('/categories/<category_id>/service_providers',
                 strict_slashes=False)
def get_service_providers(category_id):
    """
    Returns all service providers of a category
    """
    category = storage.get(Category, category_id)
    if category is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify([service_provider.to_dict()
                    for service_provider in category.service_providers])
