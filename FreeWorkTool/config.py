MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'core'


MONGO_URI = "mongodb://{host}:{port}/{db}".format(**{'host': MONGO_HOST,
                                                             'port': MONGO_PORT,
                                                             'db': MONGO_DB}
                                                          )

