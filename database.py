import sqlite3

DB_NAME = "rideshare.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS USERS1 (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT NOT NULL,
        rating REAL DEFAULT 5.0
    );

    CREATE TABLE IF NOT EXISTS VEHICLES (
        vehicle_id INTEGER PRIMARY KEY,
        driver_id INTEGER,
        model TEXT,
        license_plate TEXT UNIQUE,
        capacity INTEGER,
        FOREIGN KEY (driver_id) REFERENCES USERS1(user_id)
    );

    CREATE TABLE IF NOT EXISTS RIDES1 (
        ride_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        driver_id INTEGER,
        distance REAL,
        fare REAL,
        ride_date TEXT,
        status TEXT,
        FOREIGN KEY (customer_id) REFERENCES USERS1(user_id),
        FOREIGN KEY (driver_id) REFERENCES USERS1(user_id)
    );

    CREATE TABLE IF NOT EXISTS PAYMENTS (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ride_id INTEGER,
        amount REAL,
        method TEXT,
        payment_date TEXT,
        FOREIGN KEY (ride_id) REFERENCES RIDES1(ride_id)
    );

    CREATE TABLE IF NOT EXISTS FEEDBACK (
        feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
        ride_id INTEGER,
        customer_id INTEGER,
        comments TEXT,
        rating REAL,
        FOREIGN KEY (ride_id) REFERENCES RIDES1(ride_id),
        FOREIGN KEY (customer_id) REFERENCES USERS1(user_id)
    );
    """)

    cur.execute("SELECT COUNT(*) FROM USERS1")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO USERS1 VALUES (?, ?, ?, ?)", [
            (101, 'Aarav Sharma', 'Visakhapatnam', 4.8),
            (102, 'Sneha Reddy', 'Hyderabad', 4.9),
            (103, 'Vikram Singh', 'Bangalore', 4.5),
            (104, 'Ananya Iyer', 'Chennai', 4.7)
        ])
        cur.executemany("INSERT INTO VEHICLES VALUES (?, ?, ?, ?, ?)", [
            (301, 102, 'Hyundai i20', 'TS5678', 4),
            (302, 103, 'Honda Amaze', 'KA4321', 4)
        ])

    conn.commit()
    conn.close()
