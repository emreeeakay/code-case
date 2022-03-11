# Code-Case sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/emreeeakay/code-case.git
$ cd emreee
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

Other URLs
```
# save url  
http://127.0.0.1:8000/save

# daily report url 
http://127.0.0.1:8000/daily/1 <day count>

# weekly report url 
http://127.0.0.1:8000/weekly/1 <week count>

# monthly report url 
http://127.0.0.1:8000/monthly/1 <month count>

# years report url 
http://127.0.0.1:8000/yearsly/1 <year count>

```