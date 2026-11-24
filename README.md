# Ride-Sharing Backend System (Python & SQLite)

A modular, menu-driven backend application built with **Python** and **SQLite** to manage ride bookings, fare calculations, payment processing, customer feedback, and analytical SQL reporting.

## Database Schema
- **USERS1**: Stores customer and driver profiles (`user_id`, `name`, `city`, `rating`)
- **VEHICLES**: Links registered vehicles to drivers (`vehicle_id`, `driver_id`, `model`, `license_plate`, `capacity`)
- **RIDES1**: Tracks bookings, distances, calculated fares, dates, and ride statuses (`Pending`, `Completed`)
- **PAYMENTS**: Records transaction amounts, methods (`UPI`, `Card`, `Cash`), and payment dates
- **FEEDBACK**: Stores customer ratings (1–5) and ride reviews with foreign-key validation

## Project Structure
- `database.py` — Initializes the normalized 5-table SQLite schema with foreign key constraints and seed data
- `services.py` — Core business logic for fare calculation, ride booking, payment completion, and feedback validation
- `queries.py` — Analytical SQL queries (`INNER JOIN`, subqueries, `SUM`, `AVG`) for revenue and ride reports
- `main.py` — Interactive CLI entry point with exception handling
- `test_services.py` — Unit tests using Python's `unittest` framework

## How to Run
1. Clone or download this repository.
2. Run `python main.py` (or open `main.py` in IDLE and press `F5`).
3. Run unit tests using `python -m unittest test_services.py`.
