from website import create_app
from flask_wtf.csrf import CSRFProtect

app = create_app()
csrf = CSRFProtect(app)

if __name__ == '__main__':
    # Remember to set debug=False when running application in deployment environment
    app.run(host='0.0.0.0', port=5432, debug=True)