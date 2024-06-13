# Bootstrapping instructions

1. Create virtual environment of python using ``python3 -m venv <path>`` and activate it, then install all the requirements present in requirements.txt using ``pip3 install -r requirements.txt``
2. Install and run mongoDB locally
    * My machine was MAC with Apple Sillicon so I followed the docs at https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/
    * After installing mongoDB using brew, started the local server using ``brew services start mongodb-community@7.0``
3. Get inside the mongo shell, using command ``mongosh``
4. Create a new database using command ``use newDB`` (as used in the etl.py file line number 43)
5. Create a new collection called 'etl_output' using command ``db.createCollection("etl_output")``
6. Check no data is present at the moment in there using command ``db.etl_output.find()``, now exit the mongosh
7. Execute the script using ``python3 etl.py``
8. Head back to mongo shell, using ``mongosh`` and then change the database using command ``use newDB``
9. Check your merged data, using command ``db.createCollection("etl_output")``
