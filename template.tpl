<html>

<head>
	<title>Media Centre Contents</title>
	<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
	<script src="search.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
</head>

<body>

<div class="panel panel-default">
	<div class="panel-heading">
		<h1><a data-toggle="collapse" href="#shows_div">Shows</a></h1>
		<input type="text" id="show_search" onkeyup="filter_shows(this)" placeholder="Search for shows..">
	</div>
	<div id="shows_div" class="collapse in">
		<div>
			<ul id="shows_list" class="list-group">
				{% for show in shows %}
				<li class="list-group-item"><strong>{{ show.name }}</strong>: {{show.seasons|join(", ")}}</li>
				{% endfor %}
			</ul>
		</div>
	</div>
</div>

<div class="panel panel-default">
	<div class="panel-heading">
		<h1><a data-toggle="collapse" href="#films_div">Films</a></h1>
		<input type="text" id="film_search" onkeyup="filter_films(this)" placeholder="Search for films..">
	</div>
	<div id="films_div" class="collapse in">
		<div>
			<ul id="films_list" class="list-group">
				{% for film in films %}
				<li class="list-group-item">{{ film.name }}</li>
				{% endfor %}
			</ul>
		</div>
	</div>
</div>

</html>