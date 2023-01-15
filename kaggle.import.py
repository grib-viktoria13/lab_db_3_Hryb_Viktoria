import csv
import decimal
import psycopg2

username = 'postgres'
password = 'viktoria13052003'
database = 'lab_db'

INPUT_CSV_FILE_1 = 'table_genre.csv'
INPUT_CSV_FILE_2 = 'table_sell.csv'
INPUT_CSV_FILE_3 = 'table_artist.csv'

query_1 = '''
DELETE FROM genre
'''

query_2 = '''
INSERT INTO genre (id, artist_id, genre_name) VALUES (%s, %s, %s)
'''


query_3 = '''
DELETE FROM sell
'''


query_4 = '''
INSERT INTO sell (id, artist_id, selling) VALUES (%s, %s, %s)
'''


query_5 = '''
DELETE FROM artist
'''


query_6 = '''
INSERT INTO artist (id, name, country, tcu, years) VALUES (%s, %s, %s, %s, %s)
'''


conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_1)
    cur.execute(query_3)
    cur.execute(query_5)
    conn.commit()


with conn:
    cur = conn.cursor()
    with open(INPUT_CSV_FILE_3, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            print(row)
            values = (decimal.Decimal(row['id']), row['name'], row['country'], decimal.Decimal(row['tcu']), decimal.Decimal(row['years']))
            cur.execute(query_6, values)

    conn.commit()



with conn:
    cur = conn.cursor()
    with open(INPUT_CSV_FILE_1, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            print(row)
            values = (decimal.Decimal(row['id']),decimal.Decimal(row['artist_id']), row['genre_name'])
            cur.execute(query_2, values)

    conn.commit()
