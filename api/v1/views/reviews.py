#!/usr/bin/python3

"""
This module handles all RESTful API actions for the reviews
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, Blueprint
from models import storage
from models.reviews import Review
from models.service_provider import ServiceProvider


@app_views.route('/reviews', methods=["GET"], strict_slashes=False)
def get_all_reviews():
    """ Retrieves the list of all Review objects """
    reviews = storage.all(Review).values()
    review_list = [review.to_dict() for review in reviews]
    return jsonify(review_list)


@app_views.route('/reviews/<review_id>', methods=["GET"],
                 strict_slashes=False)
def get_review_by_id(review_id):
    """ Retrieves a Review object """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews', methods=['POST'], strict_slashes=False)
def create_review():
    """
    Creates a new review
    """
    json_data = request.get_json()
    if not json_data:
        abort(400, 'Not a JSON')
    if 'service_provider_id' not in json_data:
        abort(400, 'Missing service_provider_id')
    if 'rating' not in json_data:
        abort(400, 'Missing rating')
    if 'content' not in json_data:
        abort(400, 'Missing comment')

    service_provider_id = json_data['service_provider_id']
    service_provider = storage.get(ServiceProvider, service_provider_id)
    if service_provider is None:
        abort(404, 'Service Provider not found')

    new_review = Review(**json_data)
    new_review.service_provider_id = service_provider_id
    new_review.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    """
    Deletes a review
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404, 'Review not found')

    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id):
    """
    Updates a review
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404, 'Review not found')

    json_data = request.get_json()
    if not json_data:
        abort(400, 'Not a JSON')
    for key, value in json_data.items():
        if key not in ['id', 'created_at',
                       'updated_at', 'service_provider_id']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
