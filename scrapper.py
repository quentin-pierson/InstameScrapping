from igramscraper.instagram import Instagram
from datetime import datetime


class Scrapper:
    
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password



    def connect(self, sleep):
        instagram = Instagram(sleep_between_requests=sleep)

        # authentication supported
        instagram.with_credentials(self.userName, self.password)
        #instagram.set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36")
        instagram.login()
        

        print("Je suis bien connecté")
        return instagram
    
    def get_account_information(self, instagram, nameAccount):
        account = instagram.get_account(nameAccount)
        return account

    def get_medias(self, instagram, account_id, number_count):
        return instagram.get_medias_by_user_id(account_id, count = number_count)

    def get_comments(self,instagram, media_id, number_count):
        return instagram.get_media_comments_by_id(media_id, count = number_count)


    
    def run(self):
        insta = self.connect(5)
        account = self.get_account_information(insta, "nabilla")
        medias = self.get_medias(insta,594081073, 2)
        
        #print(account)


scrapper = Scrapper("Nabille_CompteFan", "mK5RnE84i")
#scrapper.run()

    


    

    