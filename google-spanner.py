from google.cloud import spanner
from scrapper import Scrapper
from datetime import datetime



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
            results = snapshot.execute_sql(f"SELECT Max(id) +1 from {tables_names}")
            for row in results:
                print(row)

    def last_id(self, database, table_name):
        with database.snapshot() as snapshot:
            return snapshot.execute_sql(f"SELECT Max(id) +1 from {table_name}")

    def insert_account(self, database, account):
        with database.batch() as batch:
            batch.insert(
                table="Account",
                columns=("id", "account_id", "username", "nb_followers", "nb_following", "nb_medias", "is_verified", "is_private"),
                values=[
                    (1, int(account.identifier), account.username, account.follows_count, account.followed_by_count, account.media_count, 
                    account.is_verified, account.is_private)
                ],
            )
        print("Inserted data on Account")

    def insert_media(self, database, media):
        date_comment = media.created_at
        with database.batch() as batch:
            batch.insert(
                table="Media",
                columns=("id", "account_id", "tags", "id_media", "date", "nb_comments", "nb_likes", "link", "caption", "type"),
                values=[
                    (1, int(media.owner.identifier), ["1"], int(media.identifier), datetime.fromtimestamp(date_comment), 
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
                    (comment.identifier, int(comment.owner.identifier), comment.owner.username, 
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
                    (tag.id, tag.name, 2, tag.media_count)
                ],
            )
        print("Inserted data on Tag")

        



# "account_id", "tags", "id_media", "date", "nb_comments", "nb_likes", "link", "caption", "type"),
    def run(self):
        print("coucou")
        googleSpanner = self.connect()
        self.insert_account(googleSpanner, scrapperInformation)        
        for media in medias:
            self.insert_media(googleSpanner, media)
        
        for comment in comments:
            self.insert_comments(googleSpanner, comment)

        # TO DO 
        # Tags 
        #

        self.test_request(googleSpanner, "Account")



scrapper = Scrapper("Nabille_CompteFan", "mK5RnE84i")
insta = scrapper.connect(30)
scrapperInformation = scrapper.get_account_information(insta, "nabilla")
medias = scrapper.get_medias(insta, 594081073, 2)
comments = scrapper.get_comments(insta, 2784465257312196115, 2)


GS = Google_Spanner("tfgen-spanid-20220301213550678", "database-insta-scrapping")
GS.run()

#"nb_followers", "nb_following",  "nb_medias", "is_verified", "is_private"

del scrapper
del insta