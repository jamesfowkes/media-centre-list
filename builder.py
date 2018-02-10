import sys

import jinja2

from remote import Remote
from lister import list_tv_shows, list_films

def build_html(ip, username, password):

    remote = Remote(ip, username, password)
    shows = sorted(list_tv_shows(remote), key = lambda x: x.name)
    films = sorted(list_films(remote), key = lambda x: x.name)

    jinja2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("."),
        extensions=['jinja2_time.TimeExtension']
        )

    return (jinja2_env.get_template('template.tpl').render(shows=shows, films=films))

if __name__ == "__main__":

    (ip, username, password) = sys.argv[1:4]


