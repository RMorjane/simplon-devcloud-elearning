import psycopg2
import logging    
from logging.handlers import RotatingFileHandler

class MyElearning:

    def __init__(self):
        self.connection = None
        self.list_videos = []
        self.list_vcategories = []
        self.logger = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host = "dbpostgres",
                user = "postgres",
                password = "postgres",
                port = "5432"
            )
            self.logger.info("Connexion réussie : " + str(self.connection))
            return True
        except (Exception, psycopg2.Error) as error:
            self.logger.error("Impossible de se connecter au serveur postgres : " + str(error))
            return False

    def create_tables(self):
        try:
            with self.connection.cursor() as my_cursor:
                sql_create_tables = """
                create table if not exists vcategory(
                vcategory_id serial primary key,
                vcategory_name varchar(50) not null
                );

                create table if not exists video(
                video_id serial primary key,
                video_name varchar(100) not null,
                video_link varchar(200) not null,
                vcategory_id int references vcategory(vcategory_id)
                );

                insert into vcategory(vcategory_name)
                values('cloud'),('technology'),('development');

                insert into video(video_name,video_link,vcategory_id)
                values('Le cloud computing expliqué en 7 minutes','https://www.youtube.com/embed/UC5cs06DgLFeyLIF_II7lWCQ',1),
                ('XAVKI','https://www.youtube.com/embed/UC5cs06DgLFeyLIF_II7lWCQ',1),
                ('Top 10 Technologies to Learn in 2021 | Trending Technologies in 2021 | Edureka','https://www.youtube.com/embed/UC5cs06DgLFeyLIF_II7lWCQ',2),
                ('i bought a DDoS attack on the DARK WEB (dont do this)','https://www.youtube.com/embed/UC5cs06DgLFeyLIF_II7lWCQ',2),
                ('Raspberry Pi Explained in 100 Seconds','https://www.youtube.com/embed/UC5cs06DgLFeyLIF_II7lWCQ',2),
                ('Programming tutorials','https://www.youtube.com/embed/UC5cs06DgLFeyLIF_II7lWCQ',3),
                ('Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours]','https://www.youtube.com/embed/UC5cs06DgLFeyLIF_II7lWCQ',1),
                ('LES BASES DE GIT (tuto débutant)','https://www.youtube.com/embed/UC5cs06DgLFeyLIF_II7lWCQ',3);
                """
                my_cursor.execute(sql_create_tables)
                self.connection.commit()
                my_cursor.close()
                self.logger.info("création des tables réussie !!!")
                return True
        except (Exception, psycopg2.Error) as error:
            self.logger.error("Impossible de créer les tables dans la base postgres : " + str(error))
            return False

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
                self.logger.info("Reading videos successfully!!!")
        except (Exception, psycopg2.Error) as error:
            self.logger.error("Erreur dans la requête de selection des videos : "+str(error))

    def add_video(self,video_name,video_link,vcategory_id):
        try:
            with self.connection.cursor() as my_cursor:
                sql_add_video = """INSERT INTO elearning.video(video_name,video_link,vcategory_id)
                values('%s','%s',%s)"""
                my_cursor.execute(sql_add_video %(video_name,video_link,vcategory_id))
                self.connection.commit()
                my_cursor.close()
                video_id = len(self.list_videos)+1
                self.list_videos.append({
                    "video_id": video_id,
                    "video_name": video_name,
                    "video_link": video_link,
                    "vcategory_id": vcategory_id
                })
                self.logger.info("Adding video successfully!!!")
        except (Exception, psycopg2.Error) as error:
            self.logger.error("Erreur dans la requête d'insertion de la video : "+str(error))

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
                self.logger.info("Successfull : Videos was founded")
        except (Exception, psycopg2.Error) as error:
            self.logger.error("Erreur dans la requête de selection des videos : "+str(error))

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
                self.logger.info("Readding video's categories successfully!!!")
        except (Exception, psycopg2.Error) as error:
            self.logger.error("Erreur dans la requête de selection des catégories de videos : "+str(error))

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
                    self.logger.info("Adding video category successfully!!!")
            except (Exception, psycopg2.Error) as error:
                self.logger.error("Erreur dans la requête d'insertion de la catégorie de videos : "+str(error))
        return vcategory_id

    def get_vcategory_id(self,vcategory_name):
        with self.connection.cursor() as my_cursor:
            sql_vcategory_id = "SELECT vcategory_id FROM elearning.vcategory WHERE vcategory_name='%s'"
            my_cursor.execute(sql_vcategory_id %(vcategory_name))
            vcategory_id = my_cursor.fetchone()
            my_cursor.close()
            return vcategory_id

    def set_logger(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)        
        formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
        file_handler = RotatingFileHandler('log.txt', 'a', 1000000, 1)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
