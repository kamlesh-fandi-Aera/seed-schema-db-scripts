import mysql.connector

# MySQL database configuration
db_config = {
    'host': 'dev02-new-12-19-2017.caxjfdnhccsl.us-east-1.rds.amazonaws.com',
    'user': 'kfandi',
    'password': 'JzwF$6aK!r',
    'database': '',
}

try:
    # Create a connection to the MySQL database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print('Connected to MySQL database')

        # Create a cursor to execute SQL queries
        cursor = connection.cursor()

        # DML statement
        dml_query = """
         INSERT INTO fusionops.md_recent
       (objectid, mainuserid, projectid, objecttype, `datetime`)
         VALUES('010101', 'BA5B547E_E9F1_4B88_B6D9_FC04ABD3957A', 'BE8BA2A0_2B4C_48BA_B0A8_714E9654821A', 'discovery', '2020-05-13 00:12:27');
        """

        # Execute the DML statement
        cursor.execute(dml_query)

        # Commit the changes to the database
        connection.commit()

        print('DML statement executed successfully')

except mysql.connector.Error as e:
    print('Error:', e)

finally:
    # Close the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('Connection closed')
