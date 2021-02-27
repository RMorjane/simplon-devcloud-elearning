from elearning import MyElearning

if __name__ == "__main__":
    learning = MyElearning()
    learning.connect()
    critere_recherche = {"video_name": "cloud"} # exemple de critère de recherche des vidéos
    learning.find_videos(critere_recherche)
    print(learning.list_videos)