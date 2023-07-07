import sqlite3

def insert_data(json_data):
    connection = sqlite3.connect('db.sqlite')
    cursor = connection.cursor()

    ip = json_data.get('IP', '')
    hostname = json_data.get('Hostname', '')
    mac = json_data.get('MAC', '')

    cursor.execute('INSERT INTO ips (IP, Hostname, MAC) VALUES (?, ?, ?)', (ip, hostname, mac))
    connection.commit()
    connection.close()



