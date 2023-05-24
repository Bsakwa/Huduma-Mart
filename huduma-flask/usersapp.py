#!/usr/bin/python3

"""
App for users
"""

from flask import Flask, jsonify, request
from models.user import User
from models.reviews import Review
from models import storage
from models.engine.db_storage import DBStorage

app = Flask(__name__)


# Close the current SQLAlchemy session
@app.teardown_appcontext
def teardown_db(exception):
    """ Closes storage """
    storage.close()


# Error handler for 404 - Page not found
@app.errorhandler(404)
def page_not_found(error):
    response = {
        'message': '404 - Page not found'
    }
    return jsonify(response), 404


# Route for creating a new user
@app.route('/users', methods=['POST'])
def create_user():
    """
    Creates a new user
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    # Extract necessary data from the request
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')

    if not email or not password or not first_name or not last_name:
        return jsonify({'error': 'Incomplete user data'}), 400

    # Create a new User instance
    user = User(email=email,
                password=password,
                first_name=first_name,
                last_name=last_name)

    # Save the user to the database
    storage.new(user)
    storage.save()

    return jsonify(user.to_dict()), 201


# Route for retrieving the list of all users
@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieves the list of all users
    """
    users = storage.all(User)
    users_list = []
    for user in users.values():
        users_list.append(user.to_dict())
    return jsonify(users_list)


# Route for retrieving a specific user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieves a specific user using user_id
    """
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'error': 'User not found'}), 404


# Route for deleting a specific user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a user
    """
    user = storage.get(User, user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404


# Route for updating a specific user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Updates a user
    """
    user = storage.get(User, user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    ignore = ['id', 'email', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200


# Route for retrieving reviews of a specific user
@app.route('/users/<user_id>/reviews', methods=['GET'])
def get_user_reviews(user_id):
    user = storage.get(User, user_id)
    if user:
        reviews = storage.all(Review).values()
        user_reviews = [review.to_dict()
                        for review in reviews if review.user_id == user.id]
        return jsonify(user_reviews)
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
