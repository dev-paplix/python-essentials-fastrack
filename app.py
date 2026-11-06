from robyn import Robyn
from database import init_db
from routes import register_routes
from jwt import load_env

env = load_env()
HOST = env.get("HOST", "0.0.0.0")
PORT = int(env.get("PORT", "8080"))

app = Robyn(__file__)

# Initialize database schema and demo accounts
init_db()

# Connect all routes through routes.py
register_routes(app)

if __name__ == "__main__":
    print(f"Server starting on http://{HOST}:{PORT}")
    app.start(host=HOST, port=PORT)
