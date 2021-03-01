import psycopg2

infodb = {'dbname':'elearning',
          'user':'postgres',
          'password':'linux',
          'host':'postgresql',
          'port':'5432'}

conn = psycopg2.connect(f"user= '{infodb['user']}' password= '{infodb['password']}' host='{infodb['host']}' port = '{infodb['port']}'") 
 
with open("/app/data.sql", "r") as f:
        cur1 = conn.cursor()
        cur1.execute(f.read())
        
conn.commit()
xi