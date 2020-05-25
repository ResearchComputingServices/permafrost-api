#
# Entry point to the application
# @version 1.0
# @author Sergiu Buhatel <sergiu.buhatel@carleton.ca>
#

from permafrost_api.web.views import *
from permafrost_api import permafrost_factory

global app

app = permafrost_factory.create_app(__name__)
app.app_context().push()
permafrost_factory.register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=7004)

