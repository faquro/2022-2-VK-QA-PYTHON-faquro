import sqlalchemy
from .models import Base
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker


class MysqlClient:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = '127.0.0.1'
        self.port = 3306
        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''

        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:'
            f'{self.password}@{self.host}:'
            f'{self.port}/{db}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine,
                                    autocommit=False,
                                    expire_on_commit=False
                                    )()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)
        self.connection.close()

    def create_tables(self, table_names=(
    'total_request_count', 'request_count_by_type', 'top_frequent_urls', 'top_4XX_error', 'top_5XX_error')):
        for table_name in table_names:
            if not inspect(self.engine).has_table(table_name):
                Base.metadata.tables[table_name].create(self.engine)
