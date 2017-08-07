import sys
from collections import namedtuple

from remote import Remote

Show = namedtuple("Show", ["name", "path", "seasons"])
Film = namedtuple("Film", ["name", "path"])

def q(s):
	return "'" + s + "'"

def list_tv_shows(remote):

	MEDIA1_PATH = "/media/MEDIA1/TV"
	MEDIA2_PATH = "/media/MEDIA2/TV"
	
	media1 = remote.get_directory(MEDIA1_PATH)
	media2 = remote.get_directory(MEDIA2_PATH)

	shows1 = [Show(show, q(MEDIA1_PATH + "/" + show), remote.get_directory(q(MEDIA1_PATH + "/" + show))) for show in media1]
	shows2 = [Show(show, q(MEDIA2_PATH + "/" + show), remote.get_directory(q(MEDIA2_PATH + "/" + show))) for show in media2]

	all_shows = shows1 + shows2

	return all_shows

def strip_extension(film):
	return film[:-4]

def list_films(remote):

	MEDIA1_PATH = "/media/MEDIA1/Films"
	MEDIA2_PATH = "/media/MEDIA2/Films"

	media1 = remote.get_directory(MEDIA1_PATH)
	media2 = remote.get_directory(MEDIA2_PATH)
	
	films1 = [Film(strip_extension(show), q(MEDIA1_PATH + "/" + show)) for show in media1]
	films2 = [Film(strip_extension(show), q(MEDIA2_PATH + "/" + show)) for show in media2]

	all_films = films1 + films2

	return all_films

if __name__ == "__main__":

	(ip, remote_dir, username, password) = sys.argv[1:5]

	remote = Remote(ip, username, password)
	
	print(list_tv_shows(remote))
	#print(list_films(remote))
