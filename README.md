Iki Wiki
========

About
-----
This is a toy wiki, it doesn't do too much

Requirements
------------
Install all requirements using:
```
# pip install --requirement=requirements.txt
```

It makes use of the standard [Python markdown library](http://packages.python.org/Markdown/).

[Cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Third Party Libraries
---------
- Using [Twitter Bootstrap](http://twitter.github.com/bootstrap) for styling.
- Using [Highlight.js](http://softwaremaniacs.org/soft/highlight/en/) for diff highlighting in Page History.

Tests
-----
Use the Django test runner:
```
# ./manage.py test page
```

Only the page URL slugification is tested at the moment.
Chances are you can still probably visit bad URLs because I hate regex.