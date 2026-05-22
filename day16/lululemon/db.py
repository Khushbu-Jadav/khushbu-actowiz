import mysql.connector as my_connector


def connect_to_database(database=None):
  return my_connector.connect(
    user="root",
    host="localhost",
    password="actowiz",
    database=database
  )


def execute_query(database=None, query=None, values=None, many=False):
  if not query:
    raise ValueError("query not provided.")
  my_db = connect_to_database(database)
  my_cur = my_db.cursor()
  if not values:
    my_cur.execute(query)
  if not many:
    my_cur.execute(query, values)
  else:
    my_cur.executemany(query, values)
    
  my_db.commit()
  my_db.close()
  return "Query executed successfully."