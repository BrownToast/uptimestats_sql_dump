import MySQLdb

# Open existing file or create new one
# Stores e.g. primary_key of the last record. If file not exist it will be initialised with 0
try:
  f = open("id_state", "w+")
except FileNotFoundError:
  f = open("id_state", "rw")
  f.write("0")

# Gets last record val
id_state = f.read()

query = "__YOUR_QUERY_WITH_LAST_UNIQUE_IDENTIFIER__;"

db = MySQLdb.connect(host="___HOST___",
                     user="___USER___",
                     passwd="___PASSWORD___",
                     db="___DATABASE___")

cur = db.cursor()
cur.execute(query, (id_state,))

row_count = cur.rowcount
i = 0
# loops through all rows, choose unique identifier to be stored
for row in range(row_count):
  i += 1
  row = cur.fetchone()
  if i == row_count:
    f.write(str("__YOUR_UNIQUE_IDENTIFIER_TO_STORE__"))
    f.close
