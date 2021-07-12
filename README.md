# App backend

## Constitution
Python 3.8.3   
Framework : Django  3.2.5

## Local:

### Installation
Actualization: 12.7.2021  
`$ pip install -r requirements/local.txt`  

### Run application:
`python manage.py runserver --settings=config.settings.local`

### Best practies

#### Wrapper which verifies pep8, pyflakes and circular complexity
`$ flake8`

#### Python code formatter:
`$ flake8 black directory/`
 
## Production:

### Installation
`$ pip install -r requirements/production.txt`  
