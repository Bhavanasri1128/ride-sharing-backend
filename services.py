from datetime import date
from database import get_connection

def calculate_fare(distance_km):
    if distance_km <= 0:
        raise ValueError("Distance must be greater than zero.")
    base_fare = 50.0
    per_km_rate = 15.0
    return round(base_fare + (distance_km * per_km_rate), 2)

def book_ride(customer_id, driver_id, distance_km):
    if customer_id == driver_id:
        raise ValueError("Customer and driver cannot be the same user.")
    
    fare = calculate_fare(distance_km)
    today = str(date.today())

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO RIDES1 (customer_id, driver_id, distance, fare, ride_date, status)
        VALUES (?, ?, ?, ?, ?, 'Pending')
    """, (customer_id, driver_id, distance_km, fare, today))
    ride_id = cur.lastrowid
    conn.commit()
    conn.close()
    return ride_id, fare

def complete_ride_and_pay(ride_id, method):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT fare, status FROM RIDES1 WHERE ride_id = ?", (ride_id,))
    row = cur.fetchone()

    if not row:
        conn.close()
        raise ValueError(f"Ride ID {ride_id} not found. Book a ride first (Option 1).")
    if row[1] == "Completed":
        conn.close()
        raise ValueError("Ride is already completed.")

    fare = row[0]
    today = str(date.today())

    cur.execute("UPDATE RIDES1 SET status = 'Completed' WHERE ride_id = ?", (ride_id,))
    cur.execute("""
        INSERT INTO PAYMENTS (ride_id, amount, method, payment_date)
        VALUES (?, ?, ?, ?)
    """, (ride_id, fare, method, today))

    conn.commit()
    conn.close()

def submit_feedback(ride_id, customer_id, rating, comments):
    if not (1.0 <= rating <= 5.0):
        raise ValueError("Rating must be between 1 and 5.")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT customer_id FROM RIDES1 WHERE ride_id = ?", (ride_id,))
    ride = cur.fetchone()

    if not ride:
        conn.close()
        raise ValueError(f"Ride ID {ride_id} does not exist. Book a ride first (Option 1).")
    if ride[0] != customer_id:
        conn.close()
        raise ValueError(f"Customer ID {customer_id} did not book Ride #{ride_id} (Booked by Customer {ride[0]}).")

    cur.execute("""
        INSERT INTO FEEDBACK (ride_id, customer_id, comments, rating)
        VALUES (?, ?, ?, ?)
    """, (ride_id, customer_id, comments, rating))
    conn.commit()
    conn.close()
