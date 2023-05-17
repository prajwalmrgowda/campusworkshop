"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi84vd269vf5qbem1a0-a.oregon-postgres.render.com",
        database="todo_2vs0",
        user="root",
        password="TzySBcyOc7EHY9E3YGB8Fqqb3haUAupa")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
