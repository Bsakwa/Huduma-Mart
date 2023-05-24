#!/usr/bin/python3

""" Module for Category App """

from flask import Flask, jsonify
from models.categories import Category
from models import storage
from models.engine.db_storage import DBStorage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes storage """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    response = {
        'message': '404 - Page not found'
    }
    return jsonify(response), 404


@app.route('/categories', methods=['GET'],
           strict_slashes=False)
def get_categories():
    """
    Retrieves the list of all Category objects
    """

    categories = storage.all(Category).values()
    categories_list = [category.to_dict() for category in categories]
    return jsonify(categories_list)


@app.route('/categories/<category_id>', methods=['GET'],
           strict_slashes=False)
def get_category(category_id):
    """
    Retrieves a Category object based on ID
    """
    category = storage.get(Category, category_id)
    if category:
        return jsonify(category.to_dict())
    else:
        return jsonify({'error': 'Category not found'}), 404


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
