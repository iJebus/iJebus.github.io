from flask.ext.frozen import Freezer
from ljones import app
import sys

freezer = Freezer(app)

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'freeze':
            freezer.freeze()
    except IndexError:
        app.run(debug=True, host='0.0.0.0', port=8080)
