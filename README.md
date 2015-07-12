<div style="text-align:center">
	<a href="https://github.com/tscholze/py-django-quotes/raw/master/mysite/docs/quotes-site.png">
		<img src="https://github.com/tscholze/py-django-quotes/raw/master/mysite/docs/quotes-site.png" height="300px" />
	</a>
</div>

## What's Quotes?
Quotes is my very first Django project. It is a simple quote storage. Quotes helps me to understand how Django and the Python ecosystem works and how to handle stuff like database, data migration, Json or Rss export, etc...

## How to install
1. Check if Django 1.8 is already installed
1. Clone this repository
1. Create database migration script with python manage.py makemigrations
1. Perform database migration with python manage.py migrate
1. Go to [http://localhost:8000/quotes](http://localhost:8000/quotes/) -> An empty site shows up
1. Go to [http://localhost:8000/admin](http://localhost:8000/admin) to create new entries
1. Go back to the Quotes app and hit refresh -> The latest ten quotes show up

## License 
Quotes is licensed under [MIT](https://en.wikipedia.org/wiki/MIT_License) License. 
