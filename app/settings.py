'''
Author: iiHancock
Time: 2021/11/6 10:51

'''


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    return "{}+{}://{}:@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    TESTING = False

    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1364321597",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "microfilm",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1364321597",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "microfilm",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1364321597",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "microfilm",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1364321597",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "microfilm",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
