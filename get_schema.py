# /// script
# requires-python = "~=3.12"
# dependencies = ["psycopg2"]
# ///
import json
import sys

from common import run_query


def get_schema():
    args = sys.argv[-1]
    data = json.loads(args)
    table = data.get("table")

    if not table:
        raise ValueError("table not provided")

    res = run_query(
        "SELECT column_name, data_type "
        "FROM information_schema.columns "
        f"WHERE table_name = '{table}'"
    )
    print(json.dumps(res))


if __name__ == "__main__":
    get_schema()
