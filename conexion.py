import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='baiotsol_develop', password='B410T3n3rgy2019',
                              host='108.167.149.236',
                              database='baiotsol_energy')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()

