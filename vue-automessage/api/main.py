from app import create_app
from flask_swagger import swagger
from flask import jsonify


app = create_app()

@app.route("/api/spec")
def spec():
    swag = swagger(app,prefix='/api')
    swag['info']['base'] = "http://locahost:5000"
    swag['info']['message'] = "1.0"
    swag['info']['title'] = 'Flask API Docs'
    return jsonify(swag)

@app.route("/")
def index():
  return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
