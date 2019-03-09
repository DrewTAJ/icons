# ICONS Character sheet maker

### About
This is a python 3 application that uses the library [Flask](http://flask.pocoo.org/) for handling the form and the library [Pillow](https://pillow.readthedocs.io/en/stable/) for taking the character sheet pdf and adding the character text to it.

### Setup instructions
1. Clone the repo https://github.com/DrewTAJ/icons.git
2. Install [pip](https://pypi.org/project/pip/)
3. Install flask using pip `pip install Flask`
4. Install Pillow using pip `pip install Pillow`
5. Enter the credentials for the email you want to use in `credentials.py`
6. Enter a random string or bytes as the `flask_secret` in `credentials.py`
7. Start the application using the command `python index.py`