import sae
import os
import sys
from flask import Flask

root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(root, 'virtualenv.bundle'))
sys.path.insert(0, os.path.join(root, 'site-packages'))
sys.path.insert(0, os.path.join(root, 'flask/Lib/site-packages'))

from myapp import app
application = sae.create_wsgi_app(app)
