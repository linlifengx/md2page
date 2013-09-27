import jinja2
import markdown
import codecs
from jinja2 import Template, Environment, FileSystemLoader
import os
import sys

if len(sys.argv) == 1:
	print 'require a file!!!'
	exit()

input_file = codecs.open(sys.argv[1], mode="r", encoding="utf-8-sig")
text = input_file.read()

extensions = [
	'extra',
	'meta',
	'nl2br',
	'sane_lists',
	'fenced_code',
	'codehilite(guess_lang=False, css_class=highlight)'
]
md = markdown.Markdown(extensions)
html = md.convert(text)
slug = md.Meta["slug"][0].strip().replace(' ', '-')
date = md.Meta["date"][0]

env = Environment(loader=FileSystemLoader("template"))
template = env.get_template("index.html")
result = template.render(content=html, meta=md.Meta, url_path=date+"/"+slug)

root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(root, "output", date, slug)
if not os.path.exists(path):
	os.makedirs(path)
f = file(path + "/index.html", 'w')
f.write(result)
f.close()
