from google.cloud import spanner
from goodScrapper import GoodScrapper
from datetime import datetime
import uuid


class good_database:


    def __init__(self, database, instance):
        self.database = database
        self.instance = instance

    def connect(self):
        spanner_client = spanner.Client() # Instantiate a client.

        # Get a Cloud Spanner instance by ID.
        instance = spanner_client.instance(self.instance)

        # Get a Cloud Spanner database by ID.
        database = instance.database(self.database)
        return database


    def insert_account(self, database, shared_data):
        with database.batch() as batch:
            batch.insert(
                table="Account",
                columns=("id", "account_id", "username"),
                values=[
                    (str(uuid.uuid4()), int(shared_data['id']), str(shared_data['username']))
                ],
            )
        print("Inserted data on Account")


# "nb_followers", "nb_following", "nb_medias", "is_verified", "is_private"
#shared_data['edge_followed_by']['count'], shared_data['edge_follow']['count'], 2, shared_data['is_verified'], shared_data['is_private']
    
    def run(self):
        print("T'es une meuf mais t'a pas shampoing non mais allo")
        connexion = self.connect()

        self.insert_account(connexion, sharedData)



args = {"login_user": "Nabille_CompteFan", "login_pass": "mK5RnE84i"}
createGoodSpanner = GoodScrapper()
connexion = createGoodSpanner.connect(True)
sharedData = createGoodSpanner.get_account_information(connexion, "kanyewest")


createDatabase = good_database("tfgen-spanid-20220307112400987", "database-insta-scrapping")
createDatabase.run()


