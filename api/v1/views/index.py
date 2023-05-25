#!/usr/bin/python3

"""
This module checks for our API status.
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.categories import Category
from models.reviews import Review
from models.user import User
from models.location import Location
from models.service_provider import ServiceProvider


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns an API status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Returns the number of each objects by type"""
    return jsonify({
        "categories": storage.count(Category),
        "reviews": storage.count(Review),
        "users": storage.count(User),
        "locations": storage.count(Location),
        "service_providers": storage.count(ServiceProvider)
    })
