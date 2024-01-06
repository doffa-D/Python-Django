from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
from django.utils import timezone
import datetime

# Create your views here.
def populate(request):
	movies = [
		{
			"episode_nb": 1,
			"title": "The Phantom Menace",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "1999-05-19"
		},
		{
			"episode_nb": 2,
			"title": "Attack of the Clones",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "2002-05-16"
		},
		{
			"episode_nb": 3,
			"title": "Revenge of the Sith",
			"director": "George Lucas",
			"producer": "Rick McCallum",
			"release_date": "2005-05-19"
		},
		{
			"episode_nb": 4,
			"title": "A New Hope",
			"director": "George Lucas",
			"producer": "Gary Kurtz, Rick McCallum",
			"release_date": "1977-05-25"
		},
		{
			"episode_nb": 5,
			"title": "The Empire Strikes Back",
			"director": "Irvin Kershner",
			"producer": "Gary Kurtz, Rick McCallum",
			"release_date": "1980-05-17"
		},
		{
			"episode_nb": 6,
			"title": "Return of the Jedi",
			"director": "Richard Marquand",
			"producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
			"release_date": "1983-05-25"
		},
		{
			"episode_nb": 7,
			"title": "The Force Awakens",
			"director": "J. J. Abrams",
			"producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
			"release_date": "2015-12-11"
		}
	]
	try:
		for movie in movies:
			release_date_obj = datetime.datetime.strptime(movie['release_date'],'%Y-%m-%d')
			release_date = timezone.make_aware(release_date_obj)
			m = Movies(
				title = movie['title'],
				episode_nb = movie['episode_nb'],
				director = movie['director'],
				producer = movie['producer'],
				release_date = release_date,
			)
			m.save()
		return HttpResponse('Ok')


	except Exception as e:
		return HttpResponse(str(e).replace('\n','<br/>'))

def display(request):
	movies = Movies.objects.all()
	movies_list = list(movies)

	return render(request,'displayex03.html',{'movies_list':movies_list})