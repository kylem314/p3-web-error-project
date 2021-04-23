from flask import Blueprint



calvinminilab_bp = Blueprint('calvinminilab', __name__,
                             template_folder='templates',
                            static_folder='static', static_url_path='assets')
from.import app