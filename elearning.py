import psycopg2

class MyElearning:

    def __init__(self):
        self.connection = None
        self.list_videos = []
        self.list_vcategories = []

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host = "test_postgres",
                user = "postgres",
                password = "test",
                port = "5432"
            )
            print("Connexion réussie : ",self.connection)
        except (Exception, psycopg2.Error) as error:
            print("Impossible de se connecter au serveur postgres : ",error)

    def read_videos(self):
        try:
            with self.connection.cursor() as my_cursor:
                my_cursor.execute("SELECT * FROM elearning.video")
                self.list_videos = []
                for video in my_cursor.fetchall():
                    self.list_videos.append({
                        "video_id": video[0],
                        "video_name": video[1],
                        "video_link": video[2],
                        "vcategory_id": video[3]
                    })
                my_cursor.close()
        except (Exception, psycopg2.Error) as error:
            print("Erreur dans la requête de selection des videos : ",error)

    def add_video(self,video_name,video_link,vcategory_id):
        try:
            with self.connection.cursor() as my_cursor:
                sql_add_video = """INSERT INTO elearning.video(video_name,video_link,vcategory_id)
                values('%s','%s',%s)"""
                my_cursor.execute(sql_add_video %(video_name,video_link,vcategory_id))
                self.connection.commit()
                my_cursor.close()
                video_id = len(list_videos)+1
                self.list_videos.append({
                    "video_id": video_id,
                    "video_name": video_name,
                    "video_link": video_link,
                    "vcategory_id": vcategory_id
                })
        except (Exception, psycopg2.Error) as error:
            print("Erreur dans la requête d'insertion de la video : ",error)

    def get_video_id(self,video_link):
        with self.connection.cursor() as my_cursor:
            sql_video_id = "SELECT video_id FROM elearning.video WHERE video_link='%s'"
            my_cursor.execute(sql_video_id %(video_link))
            video_id = my_cursor.fetchone()
            my_cursor.close()
            return video_id

    def find_videos(self,video_dict={}):
        list_keys = []
        list_values = []
        list_args = ()
        for key,value in video_dict.items():
            list_keys.append(key)
            list_values.append(value)
        try:
            with self.connection.cursor() as my_cursor:
                sql_find_videos = "SELECT * FROM elearning.video"
                for i in range(len(list_keys)):
                    if i==0:
                        sql_find_videos += " WHERE "
                    else:
                        sql_find_videos += " AND "
                    if type(list_values[i])==str:
                        if list_keys[i]=="vcategory_name":
                            list_keys[i] = "vcategory_id"
                            vcategory_id = self.get_vcategory_id(list_values[i])
                            if vcategory_id:
                                list_values[i] = int(vcategory_id[0])
                                list_args = (list_args + (list_values[i],))
                                sql_find_videos += list_keys[i] + "=%s"
                        else:
                            list_args = (list_args + ("%"+list_values[i]+"%",))
                            sql_find_videos += list_keys[i] + " LIKE '%s'"
                    elif type(list_values[i])==int:
                        list_args = (list_args + (list_values[i],))
                        sql_find_videos += list_keys[i] + "=%s"
                print(sql_find_videos)
                my_cursor.execute(sql_find_videos %(list_args))
                self.list_videos = []
                for video in my_cursor.fetchall():
                    self.list_videos.append({
                        "video_id": video[0],
                        "video_name": video[1],
                        "video_link": video[2],
                        "vcategory_id": video[3]
                    })
                my_cursor.close()
        except (Exception, psycopg2.Error) as error:
            print("Erreur dans la requête de selection des videos : ",error)

    def read_vcategories(self):
        try:
            with self.connection.cursor() as my_cursor:
                my_cursor.execute("SELECT * FROM elearning.vcategory")
                self.list_vcategories = []
                for vcategory in my_cursor.fetchall():
                    self.list_vcategories.append({
                        "vcategory_id": vcategory[0],
                        "vcategory_name": vcategory[1]
                    })
                my_cursor.close()
        except (Exception, psycopg2.Error) as error:
            print("Erreur dans la requête de selection des catégories de videos : ",error)

    def add_vcategory(self,vcategory_name):
        vcategory_id = self.get_vcategory_id(vcategory_name)
        if not vcategory_id:
            try:
                with self.connection.cursor() as my_cursor:
                    sql_add_vcategory = "INSERT INTO elearning.vcategory(vcategory_name) values('%s')"
                    my_cursor.execute(sql_add_vcategory %(vcategory_name))
                    self.connection.commit()
                    my_cursor.close()
                    vcategory_id = (len(self.list_vcategories)+1,)
                    self.list_vcategories.append({
                        "vcategory_id": vcategory_id,
                        "vcategory_name": vcategory_name
                    })
            except (Exception, psycopg2.Error) as error:
                print("Erreur dans la requête d'insertion de la catégorie de videos : ",error)
        return vcategory_id

    def get_vcategory_id(self,vcategory_name):
        with self.connection.cursor() as my_cursor:
            sql_vcategory_id = "SELECT vcategory_id FROM elearning.vcategory WHERE vcategory_name='%s'"
            my_cursor.execute(sql_vcategory_id %(vcategory_name))
            vcategory_id = my_cursor.fetchone()
            my_cursor.close()
            return vcategory_id