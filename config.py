import sqlite3

BOT_TOKEN = "5791370863:AAEsAXyZ1-8z3lNeC8FnP7hR7JV5a578HTc"
admin_id  = 1955770700

try:
    conn = sqlite3.connect('accout.db')
    cursor = conn.cursor()

    #Считываем всех пользователей
    users1 = cursor.execute("SELECT user_id FROM users")
    users = users1.fetchall()
    users2 = [int(i[0]) for i in users]
    #Подтверждаем изменения
    conn.commit()
except sqlite3.Error as error:
    print("error",error)

finally:
    conn = sqlite3.connect('accout.db')
    if (conn):
        conn.close()



