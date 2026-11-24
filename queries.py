from database import get_connection

def get_total_revenue():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COALESCE(SUM(fare), 0) FROM RIDES1 WHERE status = 'Completed'")
    total = cur.fetchone()[0]
    conn.close()
    return total

def get_rides_with_customers():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT r.ride_id, u.name, r.distance, r.fare, r.status
        FROM USERS1 u
        JOIN RIDES1 r ON u.user_id = r.customer_id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def get_above_average_fares():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT customer_id, fare FROM RIDES1
        WHERE fare > (SELECT AVG(fare) FROM RIDES1)
    """)
    rows = cur.fetchall()
    conn.close()
    return rows
