import sqlite3
import hashlib
import os
from pathlib import Path

DB_PATH = Path(__file__).parent / "app.db"


def get_connection():
    """Return an SQLite connection with row factory enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(password: str) -> str:
    """Generate salted SHA-256 hash."""
    salt = os.urandom(16).hex()
    hashed = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return f"{salt}${hashed}"


def verify_password(password: str, stored_hash: str) -> bool:
    """Validate password against stored salted hash."""
    try:
        salt, hashed = stored_hash.split("$", 1)
        check = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
        return hashed == check
    except Exception:
        return False


def init_db():
    """Initialize database tables and create demo users if empty."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL COLLATE NOCASE,
                password_hash TEXT NOT NULL,
                user_type TEXT NOT NULL CHECK(user_type IN ('staff', 'customer')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

        # Seed sample users if empty for immediate testing
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        if cur.fetchone()[0] == 0:
            sample_users = [
                ("staff@example.com", hash_password("staff123"), "staff"),
                ("customer@example.com", hash_password("customer123"), "customer")
            ]
            cur.executemany(
                "INSERT INTO users (email, password_hash, user_type) VALUES (?, ?, ?)",
                sample_users
            )
            conn.commit()


def find_user_by_email(email: str):
    """Retrieve user row by email."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, email, password_hash, user_type, created_at FROM users WHERE email = ?", (email.strip(),))
        row = cur.fetchone()
        if row:
            return dict(row)
        return None


def insert_user(email: str, password: str, user_type: str) -> dict:
    """Insert a new user."""
    if user_type not in ("staff", "customer"):
        raise ValueError("User type must be 'staff' or 'customer'")

    p_hash = hash_password(password)
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (email, password_hash, user_type) VALUES (?, ?, ?)",
            (email.strip(), p_hash, user_type)
        )
        conn.commit()
        user_id = cur.lastrowid
        return {
            "id": user_id,
            "email": email.strip(),
            "type": user_type
        }


def get_all_users() -> list:
    """Retrieve list of users (without password hashes) for staff view."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, email, user_type, created_at FROM users ORDER BY id DESC")
        return [dict(row) for row in cur.fetchall()]

