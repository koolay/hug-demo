Bigdata
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

0. pyenv virtualenv 3.5.2 <project_name>
1. pip install -r requirement
2. cd `your project`
3. cp .env.example .env
4. run with `gunicorn app:__hug_wsgi__ --reload`  

go with `http://localhost:8000/open/hello?name=programmer`

#### docker style


### 1.production
