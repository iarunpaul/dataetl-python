# dataetl-python
Master branch has `datafile.csv` from where data has to be extracted and loaded to the different tables in db.
Here we use SQLite3 as the db and the db file is `my_dbfile.db`.
The script file is `datafile_etl_script.py` and running the file creates the required database tables and reads the file `datafile.csv` and loads the data as required to the corresponding tables.
Before rerunning the script please drop the tables created by running the `drop_tables.py` file
