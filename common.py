# /// script
# requires-python = "~=3.12"
# dependencies = ["psycopg2"]
# ///
import os

import psycopg2

ECONOMY_DB_USERNAME = os.environ.get("ECONOMY_DB_USERNAME")
ECONOMY_DB_PASSWORD = os.environ.get("ECONOMY_DB_PASSWORD")
ECONOMY_DB_HOST = os.environ.get("ECONOMY_DB_HOST")
ECONOMY_DB_PORT = os.environ.get("ECONOMY_DB_PORT")
ECONOMY_DB_NAME = os.environ.get("ECONOMY_DB_NAME")


def run_query(query: str):
    if ECONOMY_DB_USERNAME is None:
        raise ValueError("Environment variable 'ECONOMY_DB_USERNAME' not set")
    if ECONOMY_DB_PASSWORD is None:
        raise ValueError("Environment variable 'ECONOMY_DB_PASSWORD' not set")
    if ECONOMY_DB_HOST is None:
        raise ValueError("Environment variable 'ECONOMY_DB_HOST' not set")
    if ECONOMY_DB_PORT is None:
        raise ValueError("Environment variable 'ECONOMY_DB_PORT' not set")
    if ECONOMY_DB_NAME is None:
        raise ValueError("Environment variable 'ECONOMY_DB_NAME' not set")

    connection = psycopg2.connect(
        user=ECONOMY_DB_USERNAME,
        password=ECONOMY_DB_PASSWORD,
        host=ECONOMY_DB_HOST,
        port=ECONOMY_DB_PORT,
        dbname=ECONOMY_DB_NAME,
    )
    with connection:
        with connection.cursor() as c:
            c.execute(query)
            return c.fetchall()
