#!/usr/bin/python3

"""
Handles all default RESTful API requests for users
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, Blueprint
from models import storage
from models.user import User
from models.reviews import Review


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieves the list of all User objects
    """
    users = storage.all(User)
    users_list = []
    email = request.args.get('email')
    if email:
        # Check if the email exists in the database
        filtered_users = [user for user in users.values()
                          if user.email == email]
        if not filtered_users:
            # Email does not exist, return an error message
            return jsonify({'error': 'User does not exist. Signup.'}), 404
        users_list = [user.to_dict() for user in filtered_users]
    else:
        # No email parameter provided, return all users
        users_list = [user.to_dict() for user in users.values()]
    return jsonify(users_list)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves a User object """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """ Creates a User """
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'email' not in request.get_json():
        abort(400, 'Missing email')
    if 'password' not in request.get_json():
        abort(400, 'Missing password')
    user = User(**request.get_json())
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """ Updates a User object """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    for k, v in request.get_json().items():
        if k not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, k, v)
    user.save()
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """
    Deletes a User object
    """
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({'User does not exist'}), 404
    user.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/users/<user_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(user_id):
    """
    Retrieves the list of all Review objects of a User
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    reviews_list = []
    for review in user.reviews:
        reviews_list.append(review.to_dict())
    return jsonify(reviews_list)
