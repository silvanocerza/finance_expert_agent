# /// script
# requires-python = "~=3.12"
# dependencies = ["psycopg2"]
# ///
import json
import sys

from common import run_query


def get_financial_data():
    args = sys.argv[-1]
    data = json.loads(args)
    columns = data.get("columns")
    table = data.get("table")
    page = data.get("page")
    where = data.get("where")

    if table is None:
        raise ValueError("table not provided")
    if page is None:
        raise ValueError("page not provided")
    try:
        page = int(page)
    except ValueError:
        raise ValueError("page is not an integer")

    if columns is None:
        columns = "*"
    else:
        if not isinstance(columns, list):
            raise ValueError("columns is not a list")

        columns = '", "'.join(columns)
        columns = f'"{columns}"'

    page_size = 1000

    query = f"select {columns} " f"from {table} "

    if where is None:
        where = []

    if not isinstance(where, list):
        raise ValueError("where is not a list")

    for condition in where:
        query = f"{query} where {condition}"

    query = f"{query} order by ctid limit {page_size} offset {page - 1} * {page_size}"
    res = run_query(query)
    print(json.dumps(res))


if __name__ == "__main__":
    get_financial_data()
