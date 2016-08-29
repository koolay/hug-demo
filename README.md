rest api with hug
-------

## some dependencies

- [hug](https://github.com/timothycrosley/hug)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## preparation

0. pyenv
1. python3.5.2
2. switch to python 3.5.2

## how to setup

### 0.development

#### local style

0. `pyenv virtualenv 3.5.2 <project_name>`
1. pip install -r requirement
2. cd `your project`
3. cp .env.example .env
4. run with `gunicorn app:__hug_wsgi__ --reload`  

go with `http://localhost:8000/open/hello?name=programmer`

> Note: maybe `mysql_config not found`, then fix it with `sudo apt-get install libmysqlclient-dev`

#### docker style

1. git clone https://github.com/koolay/hug-demo.git <your workspace>
2. git clone https://github.com/koolay/docker-passenger-python-hug.git <your workspace>
3. follow `docker-passenger-python-hug` 

### 1.production


## db

```

insert(), update(), delete(), getOne(), getAll(), query()

insert(table, record{})

Inserts a single record into a table.

db.insert("food", {"type": "fruit", "name": "Apple", "color": "red"})
db.insert("books", {"type": "paperback", "name": "Time Machine", "price": 5.55})
update(table, row{}, condition[])

Update one more or rows based on a condition (or no condition).

# update all rows
db.update("books", {"discount": 0})

# update rows based on a simple hardcoded condition
db.update("books",
    {"discount": 10},
    ["id=1"]
)

# update rows based on a parametrized condition
db.update("books",
    {"discount": 10},
    ("id=%s AND year=%s", [id, year])
)
insertOrUpdate(table, row{}, key)

Insert a new row, or update if there is a primary key conflict.

# insert a book with id 123. if it already exists, update values
db.insert("books",
        {"id": 123, type": "paperback", "name": "Time Machine", "price": 5.55},
        "id"
)
getOne(table, fields[], condition[], order[], limit[])

getAll(table, fields[], condition[], order[], limit[])

Get a single record or multiple records from a table given a condition (or no condition). The resultant rows are returned as namedtuples. getOne() returns a single namedtuple, and getAll() returns a list of namedtuples.

book = db.getOne("books", ["id", "name"])
# get a row based on a simple hardcoded condition
book = db.getOne("books", ["name", "year"], ("id=1"))
# get a row based on a simple hardcoded condition
book = db.getOne("books", ["name", "year"], ("id=1"))
# get multiple rows based on a parametrized condition
books = db.getAll("books",
    ["id", "name"],
    ("year > %s and price < 15", [year, 12.99])
)
# get multiple rows based on a parametrized condition with an order and limit specified
books = db.getAll("books",
    ["id", "name", "year"],
    ("year > %s and price < 15", [year, 12.99]),
    ["year", "DESC"],   # ORDER BY year DESC
    [0, 10]         # LIMIT 0, 10
)
delete(table, fields[], condition[], order[], limit[])

Delete one or more records based on a condition (or no condition)

# delete all rows
db.delete("books")

# delete rows based on a condition
db.delete("books", ("price > %s AND year < %s", [25, 1999]))
query(table)

Run a raw SQL query. The MySQLdb cursor is returned.

db.query("DELETE FROM books WHERE year > 2005")

```