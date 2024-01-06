from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import psycopg2

# Create your views here.
def init(request):
    try:
        database = settings.DATABASES['default']
        dbname = database['NAME']
        user = database['USER']
        password = database['PASSWORD']
        host = database['HOST']
        port = database['PORT']
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex04_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            )
        """)
        conn.commit()
        return HttpResponse("OK")
    except psycopg2.Error as e:
        return HttpResponse('Error: ' + str(e).replace('\n', '<br>'))

def populate(request):
    try:
        Movies = [
			{'title': 'The Phantom Menace', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '1999-05-19'},
			{'title': 'Attack of the Clones', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2002-05-16'},
			{'title': 'Revenge of the Sith', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2005-05-19'},
			{'title': 'A New Hope', 'director': 'George Lucas', 'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1977-05-25'},
			{'title': 'The Empire Strikes Back', 'director': 'Irvin Kershner', 'producer': 'Gary Kutz, Rick McCallum', 'release_date': '1980-05-17'},
			{'title': 'Return of the Jedi', 'director': 'Richard Marquand','producer':  'Howard G. Kazanjian, George Lucas, Rick McCallum', 'release_date': '1983-05-25'},
			{'title': 'The Force Awakens', 'director': 'J. J. Abrams', 'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'release_date': '2015-12-11'},
		]
        database = settings.DATABASES['default']
        dbname = database['NAME']
        user = database['USER']
        password = database['PASSWORD']
        host = database['HOST']
        port = database['PORT']
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        for movie in Movies:
            cursor.execute("""
                INSERT INTO ex04_movies (title, director, producer, release_date)
                VALUES (%s, %s, %s, %s)
            """, (movie['title'], movie['director'], movie['producer'], movie['release_date']))
        conn.commit()
        return HttpResponse("OK")
    except psycopg2.Error as e:
        return HttpResponse('Error: ' + str(e).replace('\n', '<br>'))
    
def display(request):
	database = settings.DATABASES['default']
	dbname = database['NAME']
	user = database['USER']
	password = database['PASSWORD']
	host = database['HOST']
	port = database['PORT']
	conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
	# response = ""
	cursor = conn.cursor()
	cursor.execute("""SELECT * FROM ex02_movies""")
	movies = cursor.fetchall()
	movies_list = list(movies)
	cursor.close()
	conn.close()

	return render(request, 'display.html', {'movies_list': movies_list})

def remove(request):
    try:
        database = settings.DATABASES['default']
        dbname = database['NAME']
        user = database['USER']
        password = database['PASSWORD']
        host = database['HOST']
        port = database['PORT']
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        if request.method == 'POST':
            if request.POST.get('title'):
                cursor.execute("""DELETE FROM ex04_movies WHERE title = %s""", (request.POST.get('title'),))
        cursor.execute("""SELECT * FROM ex04_movies""")
        movies = cursor.fetchall()
        movies_list = []
        for movie in movies:
            movies_list.append(movie[0])
        cursor.close()
        conn.commit()  # commit the transaction
        return render(request, 'remove.html', {'movies_list': movies_list})
    except psycopg2.Error as e:
        return HttpResponse('Error: ' + str(e).replace('\n', '<br>'))