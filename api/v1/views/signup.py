#!/usr/bin/python3

"""
Handles User registration and Login
"""

from api.v1.views import app_views
from flask import jsonify, abort, request, Blueprint, session
from models import storage
from models.user import User
from models.service_provider import ServiceProvider
from werkzeug.security import generate_password_hash
from datetime import datetime


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

    # Retrieve user credentials
    users = storage.all(User).values()
    service_providers = storage.all(ServiceProvider).values()
    user_credentials = [{'email': user.email, 'password': user.password}
                        for user in users]
    service_provider_credentials = [{'email': sp.email,
                                     'password': sp.password}
                                    for sp in service_providers]
    credentials = user_credentials + service_provider_credentials

    # Check if the provided email and password match any credentials
    matched_credentials = next(
        (cred for cred in credentials if cred['email'] == email and
         cred['password'] == password), None)

    if not matched_credentials:
        return jsonify({'message': 'Invalid email or password'}), 401

    # Create a session for the logged-in user
    session['credentials'] = matched_credentials

    # Store the user login information in the log file
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'Email: {session["credentials"]["email"]}, Timestamp: {timestamp}\n'
    with open('login.log', 'a') as log_file:
        log_file.write(log_entry)

    return jsonify({'message': 'Login successful', 'session': session}), 200


@app_views.route('/profile', methods=['GET'])
def profile():
    if 'credentials' in session:
        credentials = session['credentials']
        email = credentials['email']
        password = credentials['password']

        # Retrieve the user based on email and password from the log file
        users = []
        with open('login.log', 'r') as log_file:
            for line in log_file:
                line_parts = line.strip().split(',')
                log_email = line_parts[0].split(':')[1].strip()
                timestamp = line_parts[1].split(':')[1].strip()
                if log_email == email:
                    users.append({'email': log_email, 'timestamp': timestamp})

        if users:
            return jsonify({
                'message': 'Profile retrieved successfully',
                'user': users[-1]  # Retrieve the most recent user login entry
            }), 200

    return jsonify({'message': 'User not logged in'}), 401


@app_views.route('/logout', methods=['POST'])
def logout():
    session.clear()  # Clear the session data
    return jsonify({'message': 'Logout successful'}), 200


@app_views.route('/user_cred', methods=['GET'])
def find_users_and_service_providers():
    users = storage.all(User).values()
    service_providers = storage.all(ServiceProvider).values()
    user_credentials = [{'email': user.email, 'password': user.password}
                        for user in users]
    service_provider_credentials = [{'email': sp.email,
                                     'password': sp.password}
                                    for sp in service_providers]
    credentials = user_credentials + service_provider_credentials

    if not credentials:
        return jsonify({'message': 'No credentials found'}), 401

    return jsonify(credentials)


@app_views.route('/logged_users', methods=['GET'])
def logged_users():
    users = []
    with open('login.log', 'r') as log_file:
        for line in log_file:
            email, timestamp = line.strip().split(',')
            users.append({'email': email.split(':')[1].strip(), 'timestamp': timestamp.split(':')[1].strip()})

    return jsonify({'logged_users': users}), 200
