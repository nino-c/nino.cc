
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "5483ba38-057e-4340-94f7-8ec1973a804412a9568a-41e1-491d-9877-8f08821dab0ea88d7fd6-f5d5-4b66-84c8-d7ae3ceaec05"
NEVERCACHE_KEY = "24f0ebbd-a55b-4a7e-869e-40abd59570ecd9bf2f03-a5ca-4873-afd7-a52d88fd52d6ef6b5ec1-1c8a-4c7d-bab0-a7f40042700b"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "blog_dev",
        # Not used with sqlite3.
        "USER": "neen",
        # Not used with sqlite3.
        "PASSWORD": "pl3rp@",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "localhost",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "5432",
    }
}
