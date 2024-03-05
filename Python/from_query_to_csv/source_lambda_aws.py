import json
import mysql.connector

def lambda_handler(event, context):
    db = mysql.connector.connect(
        host='',
        user='',
        password='',
        database=''
    )
    cursor = db.cursor()
    query = json.loads(event['body'])
    cursor.execute(query)
    data = cursor.fetchall()
    data.insert(0, [column[0] for column in cursor.description])    # insert the fields name at the start
    
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
