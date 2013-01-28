Iki Wiki
========

About
-----
This is a toy wiki, it doesn't do too much

Features
--------
This wiki has some standard features:
- Index page which lists all Pages
- Edit page allows you to change page content and all revisions are saved
- Supports Markdown in Page content
- Global and Page local history of all revisions
- Ability to quickly create pages which don't exist

Some extra features have been added:
- Ability to preview Pages at specific revisions from history
- Ability to diff Pages against each other (Head revision, previous etc)
- Very trivial Admin interface for viewing pages and revisions.

Third Party Libraries
---------
- [Python markdown library](http://packages.python.org/Markdown/). See [Cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Using [Twitter Bootstrap](http://twitter.github.com/bootstrap) for styling.
- Using [Highlight.js](http://softwaremaniacs.org/soft/highlight/en/) for diff highlighting in Page History.

Setup
-------
You probably want to use a virtualenv.

Install all requirements using:
```
# pip install --requirement=requirements.txt
```

Then setup the Django app:
```
# ./manage.py syncdb
# ./manage.py runserver
# open localhost:8000
```

Tests
-----
Use the Django test runner:
```
# ./manage.py test page
```

Only the page URL slugification is tested at the moment.
Chances are you can still probably visit bad URLs because I hate regex.