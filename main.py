from database import init_db
from services import book_ride, complete_ride_and_pay, submit_feedback
from queries import get_total_revenue, get_rides_with_customers

def main():
    init_db()
    while True:
        print("\n--- RIDE SHARING SYSTEM ---")
        print("1. Book a Ride")
        print("2. Complete Ride & Pay")
        print("3. Submit Feedback")
        print("4. View All Rides (JOIN Report)")
        print("5. View Total Revenue")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                cid = int(input("Customer ID (101-104): "))
                did = int(input("Driver ID (102 or 103): "))
                dist = float(input("Distance in km: "))
                ride_id, fare = book_ride(cid, did, dist)
                print(f"Ride booked! Ride ID: {ride_id} | Estimated Fare: Rs. {fare}")

            elif choice == "2":
                rid = int(input("Enter Ride ID: "))
                method = input("Payment Method (UPI/Card/Cash): ")
                complete_ride_and_pay(rid, method)
                print("Ride marked Completed and payment recorded!")

            elif choice == "3":
                rid = int(input("Ride ID: "))
                cid = int(input("Customer ID: "))
                rating = float(input("Rating (1-5): "))
                comments = input("Comments: ")
                submit_feedback(rid, cid, rating, comments)
                print("Thank you for your feedback!")

            elif choice == "4":
                rows = get_rides_with_customers()
                if not rows:
                    print("No rides found yet.")
                for row in rows:
                    print(f"Ride #{row[0]} | Customer: {row[1]} | {row[2]} km | Rs. {row[3]} | {row[4]}")

            elif choice == "5":
                print(f"Total Completed Revenue: Rs. {get_total_revenue()}")

            elif choice == "6":
                print("Exiting system.")
                break
            else:
                print("Invalid option. Try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
