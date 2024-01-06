from django.shortcuts import render
import psycopg2
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def ex00(request):
    try:
        database = settings.DATABASES['default']
        dbname = database['NAME']
        user = database['USER']
        password = database['PASSWORD']
        host = database['HOST']
        port = database['PORT']
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex00_movies (
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
