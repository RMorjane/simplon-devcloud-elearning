import psycopg2 

infodb = {'dbname':'elearning',
          'user':'postgres',
          'password':'linux',
          'host':'postgresql',
          'port':'5432'}

def view():
    conn = psycopg2.connect(f"dbname='{infodb['dbname']}' user= '{infodb['user']}' password= '{infodb['password']}' host='{infodb['host']}' port = '{infodb['port']}'") 
    #conn = psycopg2.connect("dbname='dbtestsimplon' user= 'postgres' password= 'linux' host= 'postgresql' port = '5432'")
    cur = conn.cursor() 
    cur.execute("SELECT * FROM temps")
    rows = cur.fetchall()
    conn.close()
    print(rows)
    return rows

def insert_data(video_name, video_link):
    conn = psycopg2.connect(f"dbname='{infodb['dbname']}' user= '{infodb['user']}' password= '{infodb['password']}' host='{infodb['host']}' port = '{infodb['port']}'")
    cur = conn.cursor() 
    cur.execute("INSERT INTO video VALUES ('%s', '%s')" % (video_name, video_link))
    conn.commit() 
    conn.close() 

    
    def update_data(video_id,video_name,video_link):
    conn = psycopg2.connect(f"dbname='{infodb['dbname']}' user= '{infodb['user']}' password= '{infodb['password']}' host='{infodb['host']}' port = '{infodb['port']}'")
    cur = conn.cursor() 
    cur.execute("UPDATE store SET video_name= ?, video_link=? WHERE video_id=?",(video_name, video_link, video_id)) 
    conn.commit()
    conn.close()