
def table_exists(engine, table_name):
    """
    Checks if a table exists in the SQL database.

    Args:
        engine (sqlalchemy.engine.base.Engine): The SQLAlchemy engine.
        table_name (str): The name of the table to check.

    Returns:
        bool: True if the table exists, False otherwise.
        
    """
    query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
    result = engine.execute(query)
    return result.fetchone() is not None
