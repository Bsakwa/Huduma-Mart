#!/usr/bin/python3

"""
Flask app for Reviews
"""

from flask import Flask, jsonify, request
from models.reviews import Review
from models.service_provider import ServiceProvider
from models.user import User
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database storage"""
    storage.close()


@app.route('/reviews', methods=['GET'], strict_slashes=False)
def get_reviews():
    """
    Retrieves all reviews
    """
    reviews = storage.all(Review).values()
    reviews_list = [review.to_dict() for review in reviews]
    return jsonify(reviews_list)


@app.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """
    Retrieves a review based on the review ID
    """
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    else:
        return jsonify({'error': 'Review not found'}), 404


@app.route('/reviews', methods=['POST'], strict_slashes=False)
def post_review():
    """
    Creates a review
    """
    if not request.json:
        return jsonify({'error': 'Not a JSON'}), 400

    required_fields = ['user_id', 'service_provider_id', 'rating', 'content']
    for field in required_fields:
        if field not in request.json:
            return jsonify({'error': f'Missing {field}'}), 400

    data = request.get_json()
    user = storage.get(User, data['user_id'])
    if not user:
        return jsonify({'error': 'User not found'}), 404

    service_provider = storage.get(ServiceProvider,
                                   data['service_provider_id'])
    if not service_provider:
        return jsonify({'error': 'Service Provider not found'}), 404

    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201


@app.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """
    Deletes a review based on the review ID
    """
    review = storage.get(Review, review_id)
    if review:
        storage.delete(review)
        return jsonify({'message': 'Review deleted'})
    else:
        return jsonify({'error': 'Review not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
