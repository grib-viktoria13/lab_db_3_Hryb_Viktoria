import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'viktoria13052003'
database = 'lab_db'
host = 'localhost'
port = '5432'

query_1 = '''
create view country_of_artist as select country, count(id) from artist group by country
'''

query_2 = '''
CREATE VIEW genres_popularity as SELECT genre_name, count(id) FROM genre GROUP by genre_name
'''

query_3 = '''
CREATE VIEW artist_money AS SELECT artist.name, sell.selling FROM sell inner join artist ON artist.id = sell.artist_id order by sell.selling
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur = conn.cursor()

    cur.execute('DROP VIEW IF EXISTS country_of_artist')

    cur.execute(query_1)

    cur.execute('SELECT * FROM country_of_artist')
    country = []
    artist = []

    for row in cur:
        country.append(row[0])
        artist.append(row[1])

    x_range = range(len(country))
                                         
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, artist, label='Total')
    bar_ax.set_title('Кількість виконавців з різних країн')
    bar_ax.set_xlabel('країни')
    bar_ax.set_ylabel('кількість виконавців')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(country)


    cur.execute('DROP VIEW IF EXISTS genres_popularity')

    cur.execute(query_2)

    cur.execute('SELECT * FROM genres_popularity')
    genre = []
    singer = []

    for row in cur:
        genre.append(row[0])
        singer.append(row[1])

    x_range = range(len(genre))


    pie_ax.pie(singer, labels=genre, autopct='%1.1f%%')
    pie_ax.set_title('Частка виконавців, які працюють у кожному жанрі')

    cur.execute('DROP VIEW IF EXISTS artist_money')

    cur.execute(query_3)
    
    cur.execute('SELECT * FROM artist_money')
    name = []
    money = []
  
    for row in cur:
        name.append(row[0])
        money.append(row[1])

    graph_ax.plot(name, money, marker='o')

    graph_ax.set_xlabel("Ім'я")
    graph_ax.set_ylabel('Заробіток в мільйонах')
    graph_ax.set_title('Графік заробітку виконавців')

    for qnt, price in zip(name, money):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')    


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()