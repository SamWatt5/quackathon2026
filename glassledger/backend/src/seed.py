import sqlite3
from models import init_db

init_db()
con = sqlite3.connect("glass_ledger.db")

people = [
    (1,  'James Harlow',    'Secretary of State for Energy',
     'Conservative',     28),
    (2,  'Diana Voss',      'Shadow Chancellor',
     'Labour',            74),
    (3,  'Robert Fenn',     'Prime Minister',
     'Conservative',      41),
    (4,  'Claire Ashton',   'Home Secretary',
     'Conservative',      55),
    (5,  'Marcus Tully',    'Leader of the Opposition',
     'Labour',            66),
    (6,  'Helen Stride',    'Secretary of State for Health',
     'Conservative',      33),
    (7,  'Patrick Oduya',   'MP for East Warwick',
     'Labour',            82),
    (8,  'Susannah Blake',  'Secretary of State for Defence',
     'Conservative',      19),
    (9,  'Tom Harcastle',   'MP for North Bristol',
     'Liberal Democrat',  91),
    (10, 'Vivienne Cross',  'Chancellor of the Exchequer',
     'Conservative',      37),
]

con.executemany(
    "INSERT OR IGNORE INTO people(id, name, role, party, transparency_score) VALUES (?,?,?,?,?)",
    people
)

transactions = [
    # James Harlow (1) — energy sector donations, conflict of interest
    (1, '2025-01-02', 'Donation — North Sea Ventures Ltd',
     2200000, 'Electoral Commission', 1),
    (1, '2024-11-14', 'Speaking fee — Global Energy Forum',
     840000, 'Register of Members Interests', 0),
    (1, '2024-09-03', 'Donation — Apex Capital Partners',
     1500000, 'Electoral Commission', 1),
    (1, '2024-06-20', 'Donation — Britannia Oil & Gas',
     3100000, 'Electoral Commission', 1),
    (1, '2024-03-11', 'Expenses — Constituency office',           -320000, 'IPSA', 0),
    (1, '2023-12-05', 'Donation — Atlantic Energy Trust',
     980000, 'Electoral Commission', 0),
    (1, '2023-08-19', 'Speaking fee — Offshore Investment Summit',
     650000, 'Register of Members Interests', 0),

    # Diana Voss (2) — union donations, clean record
    (2, '2025-02-10', 'Donation — Unite the Union',
     500000, 'Electoral Commission', 0),
    (2, '2024-10-01', 'Donation — GMB Union',
     300000, 'Electoral Commission', 0),
    (2, '2024-07-14', 'Expenses — Staffing costs',                -890000, 'IPSA', 0),
    (2, '2024-04-22', 'Speaking fee — Labour Conference',
     120000, 'Register of Members Interests', 0),
    (2, '2023-11-30', 'Donation — Fabian Society',
     200000, 'Electoral Commission', 0),

    # Robert Fenn (3) — PM, hedge fund connections
    (3, '2025-01-20', 'Donation — Meridian Capital Group',
     5000000, 'Electoral Commission', 1),
    (3, '2024-12-01', 'Donation — Fenn Family Trust',
     8000000, 'Electoral Commission', 1),
    (3, '2024-09-15', 'Speaking fee — World Economic Summit',
     1200000, 'Register of Members Interests', 0),
    (3, '2024-06-03', 'Donation — Conservative Central Office',
     2500000, 'Electoral Commission', 0),
    (3, '2024-02-28', 'Expenses — Official residence',           -1500000, 'IPSA', 0),
    (3, '2023-10-10', 'Donation — Stonebridge Investments',
     4200000, 'Electoral Commission', 1),

    # Claire Ashton (4) — home secretary, security contractor links
    (4, '2025-01-08', 'Donation — SecureNet Solutions',
     780000, 'Electoral Commission', 1),
    (4, '2024-11-22', 'Speaking fee — Police Federation',
     150000, 'Register of Members Interests', 0),
    (4, '2024-08-05', 'Donation — Clearview Security Ltd',
     920000, 'Electoral Commission', 1),
    (4, '2024-05-17', 'Expenses — Constituency travel',           -180000, 'IPSA', 0),
    (4, '2023-12-12', 'Donation — Titan Border Technologies',
     1100000, 'Electoral Commission', 1),

    # Marcus Tully (5) — opposition leader, mostly clean
    (5, '2025-02-01', 'Donation — Unite the Union',
     600000, 'Electoral Commission', 0),
    (5, '2024-10-15', 'Donation — Co-operative Party',
     250000, 'Electoral Commission', 0),
    (5, '2024-07-04', 'Expenses — Campaign staff',                -440000, 'IPSA', 0),
    (5, '2024-03-28', 'Speaking fee — TUC Conference',
     180000, 'Register of Members Interests', 0),
    (5, '2023-09-14', 'Donation — Labour Together',
     350000, 'Electoral Commission', 0),

    # Helen Stride (6) — health secretary, pharma links
    (6, '2025-01-25', 'Donation — MediCorp UK',
     1800000, 'Electoral Commission', 1),
    (6, '2024-12-03', 'Speaking fee — Private Healthcare Summit',
     420000, 'Register of Members Interests', 1),
    (6, '2024-09-09', 'Donation — Pharmalex Group',
     2200000, 'Electoral Commission', 1),
    (6, '2024-06-18', 'Expenses — Office refurbishment',          -560000, 'IPSA', 0),
    (6, '2024-02-14', 'Donation — HealthBridge Foundation',
     640000, 'Electoral Commission', 0),
    (6, '2023-11-01', 'Speaking fee — Bupa Annual Lecture',
     380000, 'Register of Members Interests', 1),

    # Patrick Oduya (7) — backbencher, very clean
    (7, '2025-01-30', 'Expenses — Constituency casework',         -120000, 'IPSA', 0),
    (7, '2024-11-11', 'Donation — East Warwick CLP',
     80000, 'Electoral Commission', 0),
    (7, '2024-08-22', 'Expenses — Staff wages',                   -340000, 'IPSA', 0),
    (7, '2024-05-05', 'Speaking fee — Local school visit',
     5000, 'Register of Members Interests', 0),

    # Susannah Blake (8) — defence secretary, arms industry
    (8, '2025-02-05', 'Donation — Armadyne Defence Systems',
     4500000, 'Electoral Commission', 1),
    (8, '2024-12-14', 'Speaking fee — DSEI Arms Fair',
     750000, 'Register of Members Interests', 1),
    (8, '2024-10-02', 'Donation — Hawksworth Aerospace',
     3200000, 'Electoral Commission', 1),
    (8, '2024-07-19', 'Donation — Sentinel Technologies',
     2800000, 'Electoral Commission', 1),
    (8, '2024-04-11', 'Expenses — Ministerial travel',            -890000, 'IPSA', 0),
    (8, '2023-12-20', 'Donation — Vanguard Systems UK',
     1900000, 'Electoral Commission', 1),

    # Tom Harcastle (9) — lib dem, cleanest of the lot
    (9, '2025-01-15', 'Donation — Liberal Democrats HQ',
     220000, 'Electoral Commission', 0),
    (9, '2024-09-25', 'Expenses — Constituency office',           -145000, 'IPSA', 0),
    (9, '2024-06-12', 'Donation — North Bristol CLP',
     95000, 'Electoral Commission', 0),
    (9, '2024-02-08', 'Speaking fee — Lib Dem Spring Conference',
     60000, 'Register of Members Interests', 0),

    # Vivienne Cross (10) — chancellor, finance sector
    (10, '2025-01-10', 'Donation — Goldbridge Asset Management',
     6200000, 'Electoral Commission', 1),
    (10, '2024-11-28', 'Speaking fee — City of London Banquet',
     900000, 'Register of Members Interests', 1),
    (10, '2024-09-20', 'Donation — Harwick Private Equity',
     4800000, 'Electoral Commission', 1),
    (10, '2024-07-07', 'Donation — Cross Family Office',
     9500000, 'Electoral Commission', 1),
    (10, '2024-04-30', 'Expenses — Treasury staff costs',         -2100000, 'IPSA', 0),
    (10, '2024-01-15', 'Speaking fee — Hedge Fund Forum',
     820000, 'Register of Members Interests', 1),
    (10, '2023-10-22', 'Donation — Silverstone Capital',
     3300000, 'Electoral Commission', 1),
]

con.executemany(
    """INSERT OR IGNORE INTO transactions
       (person_id, date, description, amount, source, flagged)
       VALUES (?,?,?,?,?,?)""",
    transactions
)

flags = [
    (1, 1, 'North Sea Ventures donation', 'high'),
    (2, 1, 'Undisclosed Apex Capital directorship', 'medium'),
    (3, 3, 'Meridian Capital Group donation', 'high'),
    (4, 3, 'Fenn Trust offshore links', 'high'),
    (5, 4, 'SecureNet border contract donation', 'high'),
    (6, 4, 'Clearview Security family ties', 'medium'),
    (7, 6, 'MediCorp UK lobbying conflict', 'high'),
    (8, 6, 'Undeclared Pharmalex share options', 'high'),
    (9, 8, 'Armadyne Defence MoD contract', 'high'),
    (10, 8, 'DSEI keynote speaker appearance', 'medium'),
    (11, 10, 'Goldbridge asset windfall vote', 'high'),
    (12, 10, 'Cross Family Office registration', 'high'),
]

con.executemany(
    "INSERT OR IGNORE INTO flags(id, person_id, summary, severity) VALUES (?,?,?,?)",
    flags
)

con.commit()
con.close()
print("Seeded 10 people, 57 transactions, 12 flags.")
