import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

# 🔧 Update with your MySQL credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Jyothisai1504@$^',
    'database': 'dream_interpreter'
}

def init_db():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dreams (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            dream_text TEXT,
            interpretation TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                       (username, generate_password_hash(password)))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def validate_user(username, password):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user[1], password):
        return user[0]
    return None

def save_dream(user_id, dream_text, interpretation):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dreams (user_id, dream_text, interpretation) VALUES (%s, %s, %s)",
                   (user_id, dream_text, interpretation))
    conn.commit()
    conn.close()

def get_dreams(user_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT dream_text, interpretation, timestamp FROM dreams WHERE user_id = %s", (user_id,))
    results = cursor.fetchall()
    conn.close()
    return results
