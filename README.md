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
    
![demo] (doc/demo.png)

### Install
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