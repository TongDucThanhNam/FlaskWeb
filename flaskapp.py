import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

# if __name__ == '__main__':
#     create_app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#     create_app.run()
# else:
#     gunicorn_app = create_app(os.getenv('FLASK_CONFIG') or 'default')