import pymysql

from weixin.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE


class Mysql(object):

    def __init__(self, host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT,
                 database=MYSQL_DATABASE):
        """
        初始化mysql
        """
        self.db = pymysql.connect(host, username, password, database, charset='utf8', port=port)
        self.cursor = self.db.cursor()
        pass

    def insert(self, table, data):
        """
        :param table:
        :param data:
        :return:
        """
        keys = ','.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql_query = 'insert into %s (%s) values (%s)' % (table, keys, values)
        try:
            self.cursor.execute(sql_query)
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
