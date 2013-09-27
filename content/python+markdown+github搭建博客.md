title: python+markdown+github搭建个人博客
date: 2013-09-27
keywords: python markdown github blog
slug: use-python-markdown-github-build-a-blog

使用 python + markdown + github 搭建个人博客
============================================

我只需要一个很简单的功能，就是写好markdown文件，然后生成html放到[Github Page]上面就是了。这里只要用到下面几点的东西：

- 用[Python-Markdown]把markdown文件翻译成一段html。python-markdown默认支持普通markdown语法，它自带一些[extensions]可以支持特殊的语法和功能，如[meta]支持在markdown开始添加一些额外的信息，[codehilite]支持代码高亮。
- 使用github page的一个样式做一个[jinjia2]模版，插入markdown的html和其他信息生成完整的html。
- 用[disqus]做评论系统。
- 用`python -m SimpleHTTPServer`开个http服务来预览，也可以直接打开预览，只是disqus不能load而已。

python代码：
```
:::python
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

```

github地址: <https://github.com/linlifengx/md2page>


[Github Page]: http://pages.github.com/
[Python-Markdown]: https://pypi.python.org/pypi/Markdown
[extensions]: http://pythonhosted.org/Markdown/extensions/index.html
[meta]: http://pythonhosted.org/Markdown/extensions/meta_data.html
[codehilite]: http://pythonhosted.org/Markdown/extensions/code_hilite.html
[jinja2]: http://jinja.pocoo.org/
[disqus]: http://disqus.com/