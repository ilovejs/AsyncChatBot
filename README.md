# chatbot

- websocket
- front-end scss
- django-channel

`tips: doc folder has demo photo`

## business assumption

date of birth > 1818

## front end
message scrolling (jquery plugin can be omitted)

button send ws request

## ux credit to 

Fabio Ottaviani - Supah
    
    https://codepen.io/supah/pen/jqOBqp

### snapshot
    
<img src="https://github.com/ilovejs/chatbot/blob/master/doc/demo.png" width="400" height="500"/>

### Install option 1
*** using pip env for Pyton 3.7 ***
    pipenv install
    
    pipenv run python manage.py runserver
    
    making sure redis is running under 127.0.0.1:6379 by execute `redis-cli` in bash

After running pipenv install, here is the Pipfile you might see. Just double check.
```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
channels = "*"
django-cors-headers = "==2.1.0"
django-templated-mail = "==1.0.0"
Django = "==2.*"
channels_redis = "*"

[dev-packages]

[requires]
python_version = "3.7"
```

### Install option 2
*** python 3.6 ***

    source activate py36    # skip this step if 3.6 is installed
    
    pip install -r requirement.txt
    
    python3 manager.py runserver
    or `python manager.py runserver`

    # might need to install redis.
        
    brew install redis
    
### View after install

[open url](http://127.0.0.1:8000)
or 
[chat route](http://127.0.0.1/chat)
or 
simply http://127.0.0.1:8000 

### Contact bugfix, Pull request
zhuangdeyouxiang@gmail.com
