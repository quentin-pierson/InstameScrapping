from google.cloud import spanner
from scrapper import Scrapper
from goodScrapper import GoodScrapper
from datetime import datetime
import uuid


class Google_Spanner:

    def __init__(self, instance_id, database_id):
        self.instance_id = instance_id
        self.database_id = database_id

    
    def connect(self):
        spanner_client = spanner.Client() # Instantiate a client.

        # Get a Cloud Spanner instance by ID.
        instance = spanner_client.instance(self.instance_id)

        # Get a Cloud Spanner database by ID.
        database = instance.database(self.database_id)
        return database


    def test_request(self, database, tables_names):
        with database.snapshot() as snapshot:
            results = snapshot.execute_sql(f"SELECT id from {tables_names}")
            for row in results:
                print(row)

    def last_id(self, database, table_name):
        with database.snapshot() as snapshot:
            return snapshot.execute_sql(f"SELECT MAX(id) +1 from {table_name}")

    def insert_account(self, database, shared_data):
        with database.batch() as batch:
            batch.insert(
                table="Account",
                columns=("id", "account_id", "username", "nb_followers", "nb_following", "nb_medias", "is_verified", 
                "is_private"),
                values=[
                    (uuid.uuid4(), int(shared_data['id']), shared_data['username'], 
                    shared_data['edge_followed_by']['count'], shared_data['edge_follow']['count'], 2, 
                    shared_data['is_verified'], shared_data['is_private'])
                ],
            )
        print("Inserted data on Account")

    def insert_media(self, database, media):
        date_comment = media.created_at
        print("je suis passer chez sohs")
        with database.batch() as batch:
            batch.insert(
                table="Media",
                columns=("id", "account_id", "tags", "id_media", "date", "nb_comments", "nb_likes", "link", "caption", "type"),
                values=[
                    (str(uuid.uuid4()), int(media.owner.identifier), ["1"], int(media.identifier), datetime.fromtimestamp(date_comment), 
                    media.comments_count, media.likes_count, media.link, media.caption, media.type)
                ],
            )
        print("Inserted data on Media")
    
    def insert_comments(self, database, comment):
        date_comment = comment.created_at
        with database.batch() as batch:
            batch.insert(
                table="Comments",
                columns=("id", "id_media", "username", "date", "content"),
                values=[
                    (str(uuid.uuid4()), int(comment.owner.identifier), comment.owner.username, 
                    datetime.fromtimestamp(date_comment), comment.text)
                ],
            )
        print("Inserted data on Comments")

    def insert_tag(self, database, tag):
        with database.batch() as batch:
            batch.insert(
                table="Tag",
                columns = ("id", "tag_name", "nb_followers", "nb_medias"),
                values=[
                    (str(uuid.uuid4()), tag.name, 2, tag.media_count)
                ],
            )
        print("Inserted data on Tag")

    
    def run(self):
        print("coucou")
        googleSpanner = self.connect()
        self.insert_account(googleSpanner, account)        



args = {"login_user": "Nabille_CompteFan", "login_pass": "mK5RnE84i"}
scrapper = GoodScrapper(args)
connexion = scrapper.connect(True)
account = scrapper.get_account_information(connexion, "kanyewest")





GS = Google_Spanner("tfgen-spanid-20220303195152835", "database-insta-scrapping")
GS.run()



#Before
#scrapper = Scrapper()
#insta = scrapper.connect(5)
#scrapperInformation = scrapper.get_account_information(insta, "justezoe")
#medias = scrapper.get_medias(insta, 594081073, 2)
#comments = scrapper.get_comments(insta, 2784465257312196115, 2)

