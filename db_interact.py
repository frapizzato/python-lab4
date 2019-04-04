import pymysql


def open_connection():
    return pymysql.connect(user="root", password="root", host="localhost", database="todo_list")


def insert_task(descr):
    # insert a tuple
    conn = open_connection()
    sql_insert = "insert into todo_list.todo(description, urgent) values (%s,0)"
    cursor = conn.cursor()
    cursor.execute(sql_insert, (descr,))
    cursor.close()
    conn.commit()
    conn.close()

def show_all():
    #retrive all data
    conn = open_connection()
    sql = "select * from todo_list.todo"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def search_tuple(descr):
    #check if is present
    sql = "select * from todo_list.todo where description = %s"
    conn = open_connection()
    cursor = conn.cursor()
    cursor.execute(sql,(descr,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    if not result:
        return False
    else:
        return True

def delete_task(descr):
    #delete a task from db
    conn = open_connection()
    sql_delete = "delete from todo_list.todo where description = %s"
    cursor = conn.cursor()
    cursor.execute(sql_delete, (descr,))
    cursor.close()
    conn.commit()
    conn.close()