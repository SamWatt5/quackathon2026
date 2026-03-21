"""
Initializes the SQLite database with the required tables.
This script should be run once before starting the application to ensure the database is set up correctly.
Usage:
    python models.py

Tables:
- people: id, name, role, party, transparency_score
- transactions: id, person_id, date, description, amount, source, flagged
- flags: id, person_id, summary, severity
"""
import sqlite3


def init_db():
    """
    Initializes the SQLite database with the required tables.
    This function should be run once before starting the application to ensure the database is set up correctly.
    """
    con = sqlite3.connect("glass_ledger.db")
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            role TEXT,
            party TEXT,
            transparency_score INTEGER DEFAULT 50
        );
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            person_id INTEGER REFERENCES people(id),
            date DATETIME,
            description TEXT,
            amount INTEGER,
            source TEXT,
            flagged INTEGER DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS flags (
            id INTEGER PRIMARY KEY,
            person_id INTEGER REFERENCES people(id),
            summary TEXT,
            severity TEXT
        );
    """)
    con.commit()
    con.close()


if __name__ == "__main__":
    init_db()
    print("DB ready.")
