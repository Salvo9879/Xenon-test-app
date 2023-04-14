
# Import external modules
from flask import Blueprint

test_r = Blueprint('test', __name__, url_prefix='/test')

@test_r.route('/x')
def x():
    return 'xxx'