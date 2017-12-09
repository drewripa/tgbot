import sqlite3
import os.path

class SQLighter:

    def __init__(self, database):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        print(BASE_DIR)
        db_path = os.path.join(BASE_DIR, "music.db")
        print(db_path)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM music').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM music WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM music').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()