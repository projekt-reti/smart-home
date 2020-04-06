import sqlite3
from sqlite3 import Error


def create_db_connection(db_file):
    '''create a db connection to a SQLite Database and returns connection object'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established!")
    except Error as e:
        print(e)
    return conn


def create_table(conn, name, column_names):
    '''creates table with name 'name' in db 'conn' and returns last row id'''

    sql = '''CREATE TABLE IF NOT EXISTS ''' + name + str(column_names)
    cur = conn.cursor()
    cur.execute(sql)
    # hier noch commit einfügen!
    return cur.lastrowid


def create_entry(conn, table, data):
    '''Creates a new row with 'data' in table 'table' of db "conn"'''
    cur = conn.cursor()
    #cur.execute("select * from people where name_last=:who and age=:age", {"who": who, "age": age})
    sql = '''INSERT INTO''' + table
    #dict = {"task_id": 10, "task_name": 'Sucking', "task_duration": 4, "task_reminder": 1200}

    try:
        cur.execute(sql, data)
        print('Entry created succesfully!')
        conn.commit()
        print('Changes saved!')
    except Exception as e:
        print('Couldn\'t create entry, because: ' + str(e))


def check_table(name):
    '''check, if table 'name' exists returns boolean'''
    pass


def get_task_by_name(conn, name):
    '''returns a dictionary with the task information of a given task "name"'''
    cur = conn.cursor()
    sql = '''SELECT task_name, task_duration, task_reminder FROM tasks WHERE task_name = ?'''
    cur.execute(sql, (name,))
    row = cur.fetchall()
    return row[0]

def delete_task_by_name(conn, name):
    '''deletes task with "name"'''
    try:
        cur = conn.cursor()
        sql='''DELETE FROM tasks WHERE task_name = ?'''
        cur.execute(sql, (name,))
        conn.commit()
        print("Deleting Task '{}' from DB succesfull")
    except Exception as e:
        print(('Could not delete Task: {}').format(e))

def delete_task_by_id(conn, id):
    '''deletes task with "ID"'''
    try:
        cur = conn.cursor()
        sql='''DELETE FROM tasks WHERE rowid = ?'''
        cur.execute(sql, (id,))
        conn.commit()
    except:
        print('Could not delete Task')

def get_task_by_rowid(conn, rowid):
    '''returns dict/object of type "task" of the table named "name"'''
    cur = conn.cursor()
    sql = '''SELECT task_name, task_duration, task_reminder FROM tasks WHERE ROWID = ?'''
    cur.execute(sql, (rowid,))
    row = cur.fetchall()
    return row[0]


def get_all_tasks(conn):
    '''prints out all tasks in the table'''
    cur = conn.cursor()
    sql = '''SELECT * FROM tasks'''
    cur.execute(sql)
    allrows = cur.fetchall()
    return allrows


# only executed if script is run manually
if __name__ == '__main__':
    db_file = r"DB\smarthome.db"
    db_connection = create_db_connection(db_file)
    create_table(db_connection, "data",("Temperature", "Power Consumption"))
