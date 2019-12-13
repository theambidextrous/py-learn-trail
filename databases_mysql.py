## DATABASES - MYSQL
"""
for us to use mysql with py, we need to install mysql-connector using 

"pip install" like python -m pip install mysql-connector
"""
import mysql.connector
conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = ""
)
print (conn)
if conn :
    print('connected to db server at ' + str(conn._host) + ' on port: '+ str(conn._port))
""" once the connection is successful, you can do queries """
## create conection cursor/instance
instance = conn.cursor()
instance.execute('create database if not exists learnt_rail')
db_list = conn.cursor()
db_list.execute('show databases')

print('-+-+- printing databases -+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+-')

for db in db_list:
    print(db)
### CREATING TABLES
""" 
to create tables you must specify db in your connections
example :-  """
learn_conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "",
    database = "learnt_rail"
)
learn_inst = learn_conn.cursor()
learn_inst.execute("CREATE TABLE if not exists learners(learnid INT AUTO_INCREMENT PRIMARY KEY, name varchar(20), email varchar(55))")
table_list = learn_conn.cursor()
table_list.execute('show tables')

print('-+-+- printing tables -+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+--+-+-')

for table in table_list :
    print(table)

# Python MySQL Insert Into Table
ins_cursor = learn_conn.cursor()
q = 'insert into learners(name,email) values(%s, %s)'
vals = ('juma', 'juma@hismail.com')
ins_cursor.execute(q,vals)
# to insert multiple rows use a []
vals = [
    ('Alita', 'alita@hermail.com'),
    ('Irene', 'irene@hermail.com'),
    ('philo', 'philo@hismail.com')
]
ins_cursor.executemany(q,vals)
learn_conn.commit()
""" use the cursor.rowcount to get number rows inserted by last commit() """
print(ins_cursor.rowcount, 'Were inserted!')
""" use cursor.lastrowid to get the id of the last inserted row """
print ('last item ID: ', ins_cursor.lastrowid)

# Select From a Table
sel_cursor = learn_conn.cursor()
sel_cursor.execute('select * from learners order by learnid desc limit 25')
learners = sel_cursor.fetchall()
for learner in learners :
    print(learner)
""" to fetch only one row use fetchone() method of the cursor() object """


