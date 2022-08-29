from flask import Flask
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/api/spec'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Piadas Chuck Norris"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(
    app,
    version='1.0',
    title='API Piadas Chuck Norris',
    description='API para acesso ao serviço de piadas do Chuck Norris',
    prefix='/api'
)

ns1 = api.namespace('jokes', description='Operações relacionadas a piadas do Chuck Norris')
