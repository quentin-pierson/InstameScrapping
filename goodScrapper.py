import instagram_scraper
from datetime import datetime
import uuid



class GoodScrapper:



    def connect(self, quiet):
        args = {"login_user": "Nabille_CompteFan", "login_pass": "mK5RnE84i"}
        insta_scraper = instagram_scraper.InstagramScraper(**args, quiet = True)
        insta_scraper.authenticate_with_login()

        print("Je suis bien connecté")

        return insta_scraper
        
    def get_account_information(self, insta_scraper, username):
        shared_data = insta_scraper.get_shared_data_userinfo(username=username)
        return shared_data

    def get_medias(self, insta_scraper, shared_data):
        arr = []
        nb_photo = 0

        for item in insta_scraper.query_media_gen(shared_data):
            arr.append(item)
            nb_photo += 1
        return arr, nb_photo

    




    




