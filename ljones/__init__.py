from flask import Flask


app = Flask(__name__)
app.config.update(
    FREEZER_REMOVE_EXTRA_FILES=False,
    FREEZER_DESTINATION='../'
)

import ljones.views
