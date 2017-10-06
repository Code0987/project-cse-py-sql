from flask import Flask
import os
import sys
from bakery_ordering_system import config
 
app = Flask(__name__)
app.config.from_object(config)

from bakery_ordering_system import routes