import unittest
from elearning import MyElearning

class TestMyElearning(unittest.TestCase):

    def test_connect(self):
        elearning = MyElearning()
        elearning.connect()
        self.assertTrue(elearning.connection)

    def test_read_videos(self):
        elearning = MyElearning()
        elearning.connect()
        elearning.read_videos()
        list_videos = elearning.list_videos
        self.assertIsNotNone(list_videos)

    def test_add_video(self):
        elearning = MyElearning()
        elearning.connect()
        elearning.read_videos()
        list_videos = elearning.list_videos
        init_size = len(list_videos)
        elearning.add_video("Cours Python 3",
        "https://www.youtube.com/watch?v=HWxBtxPBCAc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC",3)
        list_videos = elearning.list_videos
        self.assertFalse(init_size == len(list_videos))

    def test_get_video_id(self):
        elearning = MyElearning()
        elearning.connect()
        video_id = elearning.get_video_id('https://www.youtube.com/channel/UC5cs06DgLFeyLIF_II7lWCQ')
        self.assertTrue(video_id)

    def test_find_videos(self):
        elearning = MyElearning()
        elearning.connect()
        critere_recherche = {"video_name": "cloud"}
        elearning.find_videos(critere_recherche)
        list_videos = elearning.list_videos
        self.assertIsNotNone(list_videos)

    def test_read_vcategories(self):
        elearning = MyElearning()
        elearning.connect()
        elearning.read_vcategories()
        list_vcategories = elearning.list_vcategories
        self.assertIsNotNone(list_vcategories)

    def test_add_vcategories(self):
        elearning = MyElearning()
        elearning.connect()
        elearning.read_vcategories()
        list_vcategories = elearning.list_vcategories
        init_size = len(list_vcategories)
        elearning.add_vcategory("python")
        self.assertFalse(init_size == len(list_vcategories))

    def test_get_vcategory_id(self):
        elearning = MyElearning()
        elearning.connect()
        vcategory_id = elearning.get_vcategory_id('cloud')
        self.assertTrue(vcategory_id)