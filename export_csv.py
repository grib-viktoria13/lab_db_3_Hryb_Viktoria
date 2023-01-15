import csv
import psycopg2

username = 'postgres'
password = 'viktoria13052003'
database = 'lab_db'

OUTPUT_FILE_T = 'table_{}.csv'

TABLES = [
    'artist',
    'genre',
    'sell',
]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for name in TABLES:
        cur.execute('SELECT * FROM ' + name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                print([str(x) for x in row])
                writer.writerow([str(x) for x in row])
