from datafile_etl_script import create_connection, create_table, sqlite3
from unittest import TestCase
from unittest import mock
from unittest.mock import patch, MagicMock, Mock


class TestDB(TestCase):
    @mock.patch('datafile_etl_script.sqlite3') # , return_value=['conn', 'bar']
    def test_connection(self, mock_sqlite3):
        conn = Mock()
        mock_sqlite3.connect.return_value = conn

        cursor      = MagicMock()
        mock_result = MagicMock()

        cursor.__enter__.return_value = mock_result
        cursor.__exit___              = MagicMock()

        conn.cursor.return_value = cursor

        create_connection("my_dbfile.db")

        mock_sqlite3.connect.assert_called_with("my_dbfile.db")

    @mock.patch('datafile_etl_script.sqlite3')
    def test_create_table(self, mock_sqlite3):
        conn = Mock()
        mock_sqlite3.connect.return_value = conn

        cursor      = MagicMock()
        mock_result = MagicMock()

        cursor.__enter__.return_value = mock_result
        cursor.__exit___              = MagicMock()

        conn.cursor.return_value = cursor
        create_table(conn, "tablename")

        conn.cursor.return_value.execute.assert_called_with("""CREATE TABLE IF NOT EXISTS Table_tablename (
                                    Customer_Name text PRIMARY KEY,
                                    Customer_ID text NOT NULL,
                                    Customer_Open_Date text NOT NULL,
                                    Last_Consulted_Date text,
                                    Vaccination_Type text,
                                    Doctor_Consulted text,
                                    State text,
                                    Country text,
                                    Date_of_Birth text,
                                    Active_Customer text
                                );""")
if __name__ == '__main__':
    unittest.main()
