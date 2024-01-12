# Pastebin

A minimal pastebin with authorization, built with Vue.js and Flask.
![Demo](./demo/demo.png)

## Features to be added
- Syntax highlighting
- Expiration time
- Password protection

## Project setup
### Frontend
```
cd pastebin
npm install
```

### Backend
```
cd pastebin_backend
pip install -r requirements.txt

# Create database
flask shell
>>> from app import db
>>> from models import User, Paste
>>> db.create_all()
```

### Compiles and hot-reloads for development
### Frontend
```
cd pastebin
npm run serve
```

### Backend
```
cd pastebin_backend
flask run
```