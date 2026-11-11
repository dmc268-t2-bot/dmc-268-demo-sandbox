def find_user_by_email(connection, email):
    """Return one user row by email, or None when missing."""
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, email FROM users WHERE email = %s",
        (email,),
    )
    row = cursor.fetchone()
    return row if row is not None else None
