import pymysql

class Db_sql_executor():
    def __init__(self, host="106.14.158.222",user="root",password="Tt123#@!",db="pydb"):
        self.connection = pymysql.connect(host = host,
                                          user = user,
                                          password = password,
                                          db = db)

    def executor(self,sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(e)
            self.connection.rollback()
        finally:
            self.connection.close()
    def select_data(self):
        cur = self.connection.cursor()
        sql = "select count(*) FROM py_douban_movie"
        cur.execute(sql)
        data = cur.fetchmany(0)
        self.connection.commit()
        self.connection.close()
        print(data)
        return data
if __name__ == '__main__':
    Db_sql_executor().select_data()