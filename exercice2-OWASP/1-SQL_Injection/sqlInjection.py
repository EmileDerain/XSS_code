import sqlite3
from django.http import HttpRequest

def identity_methode(input):
  return input

def is_admin(request: HttpRequest) -> bool:
    username = request.GET.get("input", "")
    connection = sqlite3.connect('mydb.db')
    cursor = connection.cursor()
    cursor.execute(f'''
            SELECT
                admin
            FROM
                users
            WHERE
                username = %(username)s
        ''', {
            'username': username
        })
    result = cursor.fetchone()
    if result is None:
        return False
    admin, = result
    return admin
