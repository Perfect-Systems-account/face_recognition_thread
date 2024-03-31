import pyodbc
import datetime


# TO1DO - get the data from JSON / XML file
server = '.' #192.168.14.185
database = 'face_rec1'

connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'


# username = 'py'
# password = 'M2018@'

#region functions of Cameras table

#region CREATE- insert new camera into DB
def insert_new_cam(location, ip, user_name, password, port, permission_user, serial_no):
    table_name = 'Cameras'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'


    # connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    #DRIVER={Devart ODBC Driver for SQL Server};Server=myserver;Database=mydatabase;Port=myport;User ID=myuserid;Password=mypassword
    connection = pyodbc.connect(connection_string)
    print("connected")
    cursor = connection.cursor()

    query = f'INSERT INTO {table_name} (LOCATION,IP,USERNAME,PASSWORD,PORT,PERMISSION_USER,SERIAL_NO) VALUES ({location},{ip},{user_name},{password},{port},{permission_user},{serial_no})';

    try:
        cursor.execute(query)
        connection.commit()
        print("Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
#endregion


#region GET ALL- get all of cameras from DB
def get_all_cameras():
    print('get all cameras')
    table_name = 'Cameras'
    #connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};'#;Trusted_Connection=yes;

    #connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

    connection = pyodbc.connect(connection_string)
    print("connected")
    cursor = connection.cursor()

    query = f'SELECT * FROM {database}.dbo.{table_name}';

    try:
        cursor.execute(query)
        rows=cursor.fetchall()

        for row in rows:
            print(row)

        print("Data select successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
#endregion

#region GET BY ID- get camera by id from DB
def get_camera_by_id(id):
    print('get camera by id')
    table_name = 'Cameras'
    #connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    query = f'SELECT * FROM {database}.dbo.{table_name} WHERE ID={id}';

    try:
        cursor.execute(query)
        result=cursor.fetchall()
        print (result)

        # for row in rows:
        #     print(row)

        print("Data select successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
#endregion

#region DELETE- delete camera by id from DB
def delete_camera_by_id():
    def delete_test_by_id(id):
        print('Deleting Camera by ID')
        table_name = 'Cameras'
        #connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

        try:
            with pyodbc.connect(connection_string) as connection:

                with connection.cursor() as cursor:
                    query = f'DELETE FROM {database}.dbo.{table_name} WHERE ID = {id}'

                    cursor.execute(query)
                    connection.commit()

                    print("Data deleted successfully!")
        except Exception as e:
            print(f"Error: {e}")
#endregion

#endregion

#region functions of Persons

#region CREATE- insert new person into DB
def insert_new_person(first_name, last_name, face_encoding,permission):
    table_name = 'Persons'
    #connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'
    #connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    query = f'INSERT INTO {table_name} (LOCATION,IP,USERNAME,PASSWORD,PORT,PERMISSION_USER,SERIAL_NO) VALUES ({first_name}, {last_name}, {face_encoding},{permission})';


    try:
        cursor.execute(query)
        connection.commit()
        print("Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
#endregion


#region GET ALL- get all of persons from DB
def get_all_persons():
    print('get all persons')
    table_name = 'Persons'
    #connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    query = f'SELECT * FROM {database}.dbo.{table_name}';

    try:
        cursor.execute(query)
        rows=cursor.fetchall()

        for row in rows:
            print(row)

        print("Data select successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
#endregion


#region GET BY ID- get person by id from DB
def get_person_by_id(id):
    print('get person by id')
    table_name = 'Persons'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    query = f'SELECT * FROM {database}.dbo.{table_name} WHERE ID={id}';

    try:
        cursor.execute(query)
        result=cursor.fetchall()
        print (result)

        # for row in rows:
        #     print(row)

        print("Data select successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
#endregion

#region DELETE- delete person by id from DB
def delete_person_by_id(id):
    print('Deleting person by ID')
    table_name = 'Persons'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    try:
        with pyodbc.connect(connection_string) as connection:

            with connection.cursor() as cursor:
                query = f'DELETE FROM {database}.dbo.{table_name} WHERE ID = {id}'

                cursor.execute(query)
                connection.commit()

                print("Data deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
#endregion

# Function to insert new person data into the Persons table
def insert_new_person_data_old(first_name, last_name, face_encoding, permission):
    table_name = 'Persons'
    query = f"INSERT INTO {database}.dbo.{table_name} (PERSON_FIRSTNAME, PERSON_LASTNAME, PERSON_FACE_ENCODING, PERSON_PERMISSION) VALUES ('{first_name}', '{last_name}', {face_encoding}, {permission})"

    try:
        with pyodbc.connect(connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                print(f"Data for {first_name} {last_name} inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Function to insert new person data into the Persons table- for the new sql
def insert_new_person_data(first_name, last_name, face_encoding, expiry_date, email, phone, similarity_percentages, permission):
    table_name = 'Persons'
    query = f"INSERT INTO {database}.dbo.{table_name} (PERSON_FIRSTNAME, PERSON_LASTNAME, PERSON_FACE_ENCODING, EXPIRY_DATE, EMAIL, PHONE, SIMILARITY_PERCENTAGES, PERSON_PERMISSION) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    try:
        with pyodbc.connect(connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, first_name, last_name, face_encoding, expiry_date, email, phone, similarity_percentages, permission)
                connection.commit()
                print(f"Data for {first_name} {last_name} inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Function to insert new person data into the Persons table- for the new sql

def insert_new_person_data2(person_id, first_name, last_name, face_encoding, expiry_date, email, phone, permission):

    server = '.'  # Your SQL Server server address
    database = 'face_rec1'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'




    table_name = 'Persons'

    # Get current date and time
    rec_date = datetime.datetime.now()

    # Establish connection and create cursor
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Define the SQL query
    #, ) VALUES ({person_id}, '{first_name}', '{last_name}', {face_encoding}, '{expiry_date}', '{email}', '{phone}', {permission})"
    query = f"INSERT INTO {table_name} ([PERSON_ID], [PERSON_FIRSTNAME], [PERSON_LASTNAME], [PERSON_FACE_ENCODING], [EXPIRY_DATE], [EMAIL], [PHONE], [PERSON_PERMISSION]) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

    try:
        # Execute the query
        expiry_date_str = expiry_date.strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute(query, (person_id, first_name, last_name, face_encoding, expiry_date_str, email, phone, permission))
        connection.commit()  # Commit the transaction
        print("Data inserted successfully")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()





# def insert_new_person_data2(person_id,first_name, last_name, face_encoding, expiry_date, email, phone, permission):
#     table_name = 'Persons'
#     query = f"INSERT INTO {database}.dbo.{table_name} (PERSON_FIRSTNAME, PERSON_LASTNAME, PERSON_FACE_ENCODING, PERSON_PERMISSION) VALUES ('{first_name}', '{last_name}', {face_encoding}, {permission})"
#
#     try:
#         with pyodbc.connect(connection_string) as connection:
#             with connection.cursor() as cursor:
#                 cursor.execute(query)
#                 connection.commit()
#                 print(f"Data for {first_name} {last_name} inserted successfully!")
#
#     except Exception as e:
#         print(f"Error: {e}")


#region i addedd now
def get_person_id_by_name(name):
    table_name = 'Persons'
    query = f"SELECT PERSON_ID FROM {database}.dbo.{table_name} WHERE PERSON_FIRSTNAME = {name}"

    try:
        with pyodbc.connect(connection_string) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, name)
                result = cursor.fetchone()
                return result[0] if result else None

    except Exception as e:
        print(f"Error: {e}")
        return None
#endregion


#region gets a face encoding and returns the name of the face that looks like it
def load_known_faces_from_database():
    known_face_encodings = []
    known_face_names = []
    known_face_ids=[]

    # Establish a connection to the SQL Server
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Query the Persons table to get face encodings and names
    query = "SELECT PERSON_ID, PERSON_FIRSTNAME, PERSON_LASTNAME, PERSON_FACE_ENCODING FROM Persons"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        person_id,first_name, last_name, face_encoding_str = row
        face_encoding = [float(val) for val in face_encoding_str.split()]  # Convert the string back to a list
        known_face_encodings.append(face_encoding)
        known_face_names.append(f"{first_name} {last_name}")
        known_face_ids.append(person_id)

    # Close the SQL connection
    cursor.close()
    connection.close()

    return known_face_encodings, known_face_names
        #,known_face_ids
#endregion


#endregion

#region functions of Permissions

#region CREATE- insert new Permission into DB
def insert_new_permission(permission_name, permission_create_date,permission_change_date):
    table_name = 'PermissionsTypes'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    query = f'INSERT INTO {table_name} (LOCATION,IP,USERNAME,PASSWORD,PORT,PERMISSION_USER,SERIAL_NO) VALUES ({permission_name}, {permission_create_date},{permission_change_date})';

    try:
        cursor.execute(query)
        connection.commit()
        print("Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
#endregion


#region GET ALL- get all of Permissions from DB
def get_all_Permissions():
    print('get all persons')
    table_name = 'PermissionsTypes'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    query = f'SELECT * FROM {database}.dbo.{table_name}';

    try:
        cursor.execute(query)
        rows=cursor.fetchall()

        for row in rows:
            print(row)

        print("Data select successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
#endregion


#region GET BY ID- get Permission by id from DB
def get_Permission_by_id(id):
    print('get person by id')
    table_name = 'PermissionsTypes'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    query = f'SELECT * FROM {database}.dbo.{table_name} WHERE ID={id}';

    try:
        cursor.execute(query)
        result=cursor.fetchall()
        print (result)

        # for row in rows:
        #     print(row)

        print("Data select successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()
#endregion

#region DELETE- delete Permission by id from DB
def delete_Permission_by_id(id):
    print('Deleting person by ID')
    table_name = 'PermissionsTypes'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database}'

    try:
        with pyodbc.connect(connection_string) as connection:

            with connection.cursor() as cursor:
                query = f'DELETE FROM {database}.dbo.{table_name} WHERE ID = {id}'

                cursor.execute(query)
                connection.commit()

                print("Data deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
#endregion

#endregion


#region INSERT- new log into LogDate table
def insert_new_log(person_face_encoding, success, action_p, device_id, user_details):
    server = '.'  # Your SQL Server server address
    database = 'face_rec1'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

    table_name = 'LogDate'

    # Get current date and time
    rec_date = datetime.datetime.now()

    # Establish connection and create cursor
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    # Define the SQL query
    query = f"INSERT INTO {table_name} ([PERSON_FACE_ENCODING], [REC_DATE], [SUCCESS], [ACTION_P], [DEVICE_ID], [USER_DETAILS]) VALUES (?, ?, ?, ?, ?, ?)"

    try:
        # Execute the query
        cursor.execute(query, (person_face_encoding, rec_date, success, action_p, device_id, user_details))
        connection.commit()  # Commit the transaction
        print("Data inserted successfully")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

# endregion






