# Imports the Google Cloud Client Library.
from google.cloud import spanner
OPERATION_TIMEOUT_SECONDS = 240


instance_id = "tfgen-spanid-20220227174038080" # Google Cloud Spanner instance ID.
database_id = "database-insta-scrapping" # Google Cloud Spanner database ID.
spanner_client = spanner.Client() # Instantiate a client.

# Get a Cloud Spanner instance by ID.
instance = spanner_client.instance(instance_id)

# Get a Cloud Spanner database by ID.
database = instance.database(database_id)


# Execute a simple SQL statement.
#with database.snapshot() as snapshot:
#    results = snapshot.execute_sql("SELECT * from t1")
#    for row in results:
#        print(row)

def create_database(instance_id, database_id):
    """Creates a database and tables for sample data."""
    
    database = instance.database(
        database_id,
        ddl_statements=[
            """CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX)
        ) PRIMARY KEY (SingerId)""",
            """CREATE TABLE Albums (
            SingerId     INT64 NOT NULL,
            AlbumId      INT64 NOT NULL,
            AlbumTitle   STRING(MAX)
        ) PRIMARY KEY (SingerId, AlbumId),
        INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
        ],
    )

    operation = database.create()

    print("Waiting for operation to complete...")
    operation.result(OPERATION_TIMEOUT_SECONDS)

    print("Created database {} on instance {}".format(database_id, instance_id))


def insert_data(instance_id, database_id):
    """Inserts sample data into the given database.

    The database and table must already exist and can be created using
    `create_database`.
    """
    with database.batch() as batch:
        batch.insert(
            table="Singers",
            columns=("SingerId", "FirstName", "LastName"),
            values=[
                (1, u"Marc", u"Richards"),
                (2, u"Catalina", u"Smith"),
                (3, u"Alice", u"Trentor"),
                (4, u"Lea", u"Martin"),
                (5, u"David", u"Lomond"),
            ],
        )
    print("Inserted data.")

def test_request(tables_names):
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(f"SELECT * from {tables_names}")
        for row in results:
            print(row)


if __name__ == "__main__":
    #create_database(instance_id, database_id)
   # insert_data(instance_id, database_id)
   test_request("Singers")

    

