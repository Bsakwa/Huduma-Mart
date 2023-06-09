#!/usr/bin/python3

"""
Handles User registration and Login
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, Blueprint, session
from models import storage
from models.user import User
from models.service_provider import ServiceProvider
from werkzeug.security import generate_password_hash, check_password_hash


@app_views.route('/register', methods=['POST'])
def register():
    email = request.json['email']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']

    if not email or not password or not first_name or not last_name:
        return jsonify({'message': 'Missing required fields'}), 400

    # Check if any user field matches the provided values
    users = storage.all(User)
    for user in users.values():
        if (user.email == email
           or user.first_name == first_name
           or user.last_name == last_name):
            return jsonify({'message': 'User already exists. Log in.'}), 409

    # Create a new user
    user = User(email=email, password=password,
                first_name=first_name, last_name=last_name)
    storage.new(user)
    storage.save()

    return jsonify({'message': 'User registered successfully'}), 201


@app_views.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    if not email or not password:
        return jsonify({'message': 'Missing email or password'}), 400

    # Query the user by email
    users = storage.all(User).values()
    user = next((user for user in users if user.email == email), None)

    # Check if the user exists and the password is correct
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401
    # Create a session for the logged-in user
    # You can customize the session implementation based on your requirements
    session['user_id'] = user.id
    session['email'] = user.email

    return jsonify({'message': 'Log in: Success', 'session': session}), 200


@app_views.route('/profile', methods=['GET'])
def profile():
    user = get_user_from_session()
    if user:
        return jsonify({
            'message': 'Profile retrieved successfully',
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        }), 200
    else:
        return jsonify({'message': 'User not logged in'}), 401


@app_views.route('/logout', methods=['POST'])
def logout():
    session.clear()  # Clear the session data
    return jsonify({'message': 'Logout successful'}), 200


@app_views.route('/users_and_service_providers_cred', methods=['GET'])
def find_users_and_service_providers():
    users = storage.all(User).values()
    service_providers = storage.all(ServiceProvider).values()
    user_credentials = [{'email': user.email, 'password': user.password}
                        for user in users]
    service_provider_credentials = [{'email': sp.email,
                                     'password': sp.password}
                                    for sp in service_providers]
    credentials = user_credentials + service_provider_credentials
    # Set the user's credentials in the session
    session['credentials'] = credentials

    return jsonify(credentials)
