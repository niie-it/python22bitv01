import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='python21bitv03',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM loai")
    # result = cursor.fetchone()
    result = cursor.fetchall()
    print(result)
