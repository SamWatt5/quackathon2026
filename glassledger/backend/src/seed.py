import sqlite3
from models import init_db

init_db()
con = sqlite3.connect("glass_ledger.db")

# id, name, field, company, role, party, transparency_score
people = [
    # Politicians
    (1,  'James Harlow',    'politician', None,
     'Secretary of State for Energy',        'Conservative',     28),
    (2,  'Diana Voss',      'politician', None,
     'Shadow Chancellor',                    'Labour',            74),
    (3,  'Robert Fenn',     'politician', None,
     'Prime Minister',                       'Conservative',      41),
    (4,  'Claire Ashton',   'politician', None,
     'Home Secretary',                       'Conservative',      55),
    (5,  'Marcus Tully',    'politician', None,
     'Leader of the Opposition',             'Labour',            66),
    (6,  'Helen Stride',    'politician', None,
     'Secretary of State for Health',        'Conservative',      33),
    (7,  'Patrick Oduya',   'politician', None,
     'MP for East Warwick',                  'Labour',            82),
    (8,  'Susannah Blake',  'politician', None,
     'Secretary of State for Defence',       'Conservative',      19),
    (9,  'Tom Harcastle',   'politician', None,
     'MP for North Bristol',                 'Liberal Democrat',  91),
    (10, 'Vivienne Cross',  'politician', None,
     'Chancellor of the Exchequer',          'Conservative',      37),

    # Executives
    (11, 'Edward Crane',    'executive',  'North Sea Ventures Ltd',
     'Chief Executive Officer',              None,                22),
    (12, 'Miranda Faulk',   'executive',  'Goldbridge Asset Mgmt',
     'Chief Executive Officer',              None,                31),
    (13, 'Oliver Stanton',  'executive',  'Armadyne Defence Systems',
     'Chief Executive Officer',              None,                18),
    (14, 'Rachel Ibbotson', 'executive',  'MediCorp UK',
     'Chief Executive Officer',              None,                44),
    (15, 'Conrad Whitley',  'executive',  'Pharmalex Group',
     'Chief Executive Officer',              None,                29),

    # Journalists
    (16, 'Sophie Aldred',   'journalist', 'The Clarion',
     'Editor in Chief',                      None,                78),
    (17, 'Ben Frasier',     'journalist', 'GB Today',
     'Political Editor',                     None,                52),
    (18, 'Naomi Creed',     'journalist', 'The Clarion',
     'Investigative Reporter',               None,                88),

    # Lobbyists
    (19, 'Gregory Vane',    'lobbyist',   'Apex Capital Partners',
     'Senior Policy Advisor',                None,                14),
    (20, 'Harriet Dunn',    'lobbyist',   'Titan Border Technologies',
     'Director of Government Relations',     None,                21),
]

con.executemany(
    "INSERT OR IGNORE INTO people(id, name, field, company, role, party, transparency_score) VALUES (?,?,?,?,?,?,?)",
    people
)

transactions = [
    # James Harlow (1)
    (1,  '2025-01-02', 'Donation — North Sea Ventures Ltd',
     2200000, 'Electoral Commission', 1),
    (1,  '2024-11-14', 'Speaking fee — Global Energy Forum',
     840000, 'Register of Members Interests', 0),
    (1,  '2024-09-03', 'Donation — Apex Capital Partners',
     1500000, 'Electoral Commission', 1),
    (1,  '2024-06-20', 'Donation — Britannia Oil & Gas',
     3100000, 'Electoral Commission', 1),
    (1,  '2024-03-11', 'Expenses — Constituency office',           -320000, 'IPSA', 0),
    (1,  '2023-12-05', 'Donation — Atlantic Energy Trust',
     980000, 'Electoral Commission', 0),
    (1,  '2023-08-19', 'Speaking fee — Offshore Investment Summit',
     650000, 'Register of Members Interests', 0),

    # Diana Voss (2)
    (2,  '2025-02-10', 'Donation — Unite the Union',
     500000, 'Electoral Commission', 0),
    (2,  '2024-10-01', 'Donation — GMB Union',
     300000, 'Electoral Commission', 0),
    (2,  '2024-07-14', 'Expenses — Staffing costs',                -890000, 'IPSA', 0),
    (2,  '2024-04-22', 'Speaking fee — Labour Conference',
     120000, 'Register of Members Interests', 0),
    (2,  '2023-11-30', 'Donation — Fabian Society',
     200000, 'Electoral Commission', 0),

    # Robert Fenn (3)
    (3,  '2025-01-20', 'Donation — Meridian Capital Group',
     5000000, 'Electoral Commission', 1),
    (3,  '2024-12-01', 'Donation — Fenn Family Trust',
     8000000, 'Electoral Commission', 1),
    (3,  '2024-09-15', 'Speaking fee — World Economic Summit',
     1200000, 'Register of Members Interests', 0),
    (3,  '2024-06-03', 'Donation — Conservative Central Office',
     2500000, 'Electoral Commission', 0),
    (3,  '2024-02-28', 'Expenses — Official residence',           -1500000, 'IPSA', 0),
    (3,  '2023-10-10', 'Donation — Stonebridge Investments',
     4200000, 'Electoral Commission', 1),

    # Claire Ashton (4)
    (4,  '2025-01-08', 'Donation — SecureNet Solutions',
     780000, 'Electoral Commission', 1),
    (4,  '2024-11-22', 'Speaking fee — Police Federation',
     150000, 'Register of Members Interests', 0),
    (4,  '2024-08-05', 'Donation — Clearview Security Ltd',
     920000, 'Electoral Commission', 1),
    (4,  '2024-05-17', 'Expenses — Constituency travel',           -180000, 'IPSA', 0),
    (4,  '2023-12-12', 'Donation — Titan Border Technologies',
     1100000, 'Electoral Commission', 1),

    # Marcus Tully (5)
    (5,  '2025-02-01', 'Donation — Unite the Union',
     600000, 'Electoral Commission', 0),
    (5,  '2024-10-15', 'Donation — Co-operative Party',
     250000, 'Electoral Commission', 0),
    (5,  '2024-07-04', 'Expenses — Campaign staff',                -440000, 'IPSA', 0),
    (5,  '2024-03-28', 'Speaking fee — TUC Conference',
     180000, 'Register of Members Interests', 0),
    (5,  '2023-09-14', 'Donation — Labour Together',
     350000, 'Electoral Commission', 0),

    # Helen Stride (6)
    (6,  '2025-01-25', 'Donation — MediCorp UK',
     1800000, 'Electoral Commission', 1),
    (6,  '2024-12-03', 'Speaking fee — Private Healthcare Summit',
     420000, 'Register of Members Interests', 1),
    (6,  '2024-09-09', 'Donation — Pharmalex Group',
     2200000, 'Electoral Commission', 1),
    (6,  '2024-06-18', 'Expenses — Office refurbishment',          -560000, 'IPSA', 0),
    (6,  '2024-02-14', 'Donation — HealthBridge Foundation',
     640000, 'Electoral Commission', 0),
    (6,  '2023-11-01', 'Speaking fee — Bupa Annual Lecture',
     380000, 'Register of Members Interests', 1),

    # Patrick Oduya (7)
    (7,  '2025-01-30', 'Expenses — Constituency casework',         -120000, 'IPSA', 0),
    (7,  '2024-11-11', 'Donation — East Warwick CLP',
     80000, 'Electoral Commission', 0),
    (7,  '2024-08-22', 'Expenses — Staff wages',                   -340000, 'IPSA', 0),
    (7,  '2024-05-05', 'Speaking fee — Local school visit',
     5000, 'Register of Members Interests', 0),

    # Susannah Blake (8)
    (8,  '2025-02-05', 'Donation — Armadyne Defence Systems',
     4500000, 'Electoral Commission', 1),
    (8,  '2024-12-14', 'Speaking fee — DSEI Arms Fair',
     750000, 'Register of Members Interests', 1),
    (8,  '2024-10-02', 'Donation — Hawksworth Aerospace',
     3200000, 'Electoral Commission', 1),
    (8,  '2024-07-19', 'Donation — Sentinel Technologies',
     2800000, 'Electoral Commission', 1),
    (8,  '2024-04-11', 'Expenses — Ministerial travel',            -890000, 'IPSA', 0),
    (8,  '2023-12-20', 'Donation — Vanguard Systems UK',
     1900000, 'Electoral Commission', 1),

    # Tom Harcastle (9)
    (9,  '2025-01-15', 'Donation — Liberal Democrats HQ',
     220000, 'Electoral Commission', 0),
    (9,  '2024-09-25', 'Expenses — Constituency office',           -145000, 'IPSA', 0),
    (9,  '2024-06-12', 'Donation — North Bristol CLP',
     95000, 'Electoral Commission', 0),
    (9,  '2024-02-08', 'Speaking fee — Lib Dem Spring Conference',
     60000, 'Register of Members Interests', 0),

    # Vivienne Cross (10)
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

    # Edward Crane (11)
    (11, '2025-01-15', 'Salary — North Sea Ventures Ltd',
     45000000, 'Companies House', 0),
    (11, '2024-10-01', 'Bonus — Annual performance',
     12000000, 'Companies House', 0),
    (11, '2024-06-12', 'Donation — Conservative Party',
     2200000, 'Electoral Commission', 1),
    (11, '2024-03-08', 'Speaking fee — Oil & Gas UK Conference',
     850000, 'Industry Register', 0),

    # Miranda Faulk (12)
    (12, '2025-02-01', 'Salary — Goldbridge Asset Management',
     62000000, 'Companies House', 0),
    (12, '2024-11-15', 'Bonus — Fund performance',
     28000000, 'Companies House', 0),
    (12, '2024-08-20', 'Donation — Conservative Party',
     3100000, 'Electoral Commission', 1),
    (12, '2024-05-05', 'Speaking fee — Davos Side Event',
     1200000, 'Industry Register', 0),

    # Oliver Stanton (13)
    (13, '2025-01-20', 'Salary — Armadyne Defence Systems',
     38000000, 'Companies House', 0),
    (13, '2024-12-01', 'Bonus — MoD contract win',
     15000000, 'Companies House', 1),
    (13, '2024-09-14', 'Donation — Conservative Party',
     1800000, 'Electoral Commission', 1),
    (13, '2024-06-30', 'Speaking fee — DSEI Conference',
     950000, 'Industry Register', 0),

    # Rachel Ibbotson (14)
    (14, '2025-01-08', 'Salary — MediCorp UK',
     29000000, 'Companies House', 0),
    (14, '2024-10-22', 'Bonus — NHS contract award',
     8500000, 'Companies House', 1),
    (14, '2024-07-17', 'Donation — Conservative Party',
     1200000, 'Electoral Commission', 1),
    (14, '2024-04-03', 'Speaking fee — Private Health Summit',
     680000, 'Industry Register', 0),

    # Conrad Whitley (15)
    (15, '2025-02-10', 'Salary — Pharmalex Group',
     33000000, 'Companies House', 0),
    (15, '2024-11-05', 'Bonus — Drug approval milestone',
     11000000, 'Companies House', 0),
    (15, '2024-08-01', 'Donation — Conservative Party',
     1500000, 'Electoral Commission', 1),
    (15, '2024-05-19', 'Speaking fee — BioInvestor Forum',
     720000, 'Industry Register', 0),

    # Sophie Aldred (16)
    (16, '2025-01-12', 'Salary — The Clarion',
     8500000, 'Companies House', 0),
    (16, '2024-09-01', 'Speaking fee — Press Freedom Conference',
     120000, 'Industry Register', 0),
    (16, '2024-05-14', 'Donation — Journalism Foundation',
     50000, 'Charity Commission', 0),

    # Ben Frasier (17)
    (17, '2025-01-20', 'Salary — GB Today',
     4200000, 'Companies House', 0),
    (17, '2024-11-10', 'Speaking fee — Reform UK Conference',
     180000, 'Industry Register', 1),
    (17, '2024-07-22', 'Donation — GB Today parent company',
     950000, 'Companies House', 1),

    # Naomi Creed (18)
    (18, '2025-01-15', 'Salary — The Clarion',
     3800000, 'Companies House', 0),
    (18, '2024-10-05', 'Book advance — Follow The Money',
     1200000, 'Publisher Record', 0),
    (18, '2024-06-18', 'Award — Press Gazette Investigative',
     10000, 'Industry Register', 0),

    # Gregory Vane (19)
    (19, '2025-01-25', 'Retainer — Apex Capital Partners',
     9600000, 'Lobbying Register', 1),
    (19, '2024-12-01', 'Retainer — Britannia Oil & Gas',
     7200000, 'Lobbying Register', 1),
    (19, '2024-09-10', 'Meeting fee — Treasury officials',
     480000, 'Lobbying Register', 1),
    (19, '2024-06-05', 'Retainer — Atlantic Energy Trust',
     6000000, 'Lobbying Register', 1),

    # Harriet Dunn (20)
    (20, '2025-02-01', 'Retainer — Titan Border Technologies',
     8400000, 'Lobbying Register', 1),
    (20, '2024-11-15', 'Retainer — SecureNet Solutions',
     6000000, 'Lobbying Register', 1),
    (20, '2024-08-20', 'Meeting fee — Home Office officials',
     360000, 'Lobbying Register', 1),
    (20, '2024-05-10', 'Retainer — Clearview Security Ltd',
     5400000, 'Lobbying Register', 1),
]

con.executemany(
    """INSERT OR IGNORE INTO transactions
       (person_id, date, description, amount, source, flagged)
       VALUES (?,?,?,?,?,?)""",
    transactions
)

flags = [
    (1,  1,  'Donated by North Sea Ventures before bill', 'high'),
    (2,  1,  'Undisclosed Apex Capital directorship', 'medium'),
    (3,  3,  'Meridian donated after govt contract win', 'high'),
    (4,  3,  'Fenn Trust linked to Cayman accounts', 'high'),
    (5,  4,  'SecureNet donated before £340m contract', 'high'),
    (6,  4,  'Clearview director is family member', 'medium'),
    (7,  6,  'MediCorp lobbied bill she co-sponsored', 'high'),
    (8,  6,  'Undeclared Pharmalex share options', 'high'),
    (9,  8,  'Armadyne got £2.1bn contract she signed', 'high'),
    (10, 8,  'Spoke at arms fair while approving budget', 'medium'),
    (11, 10, 'Voted against tax days after donation', 'high'),
    (12, 10, 'Family office at personal home address', 'high'),
    (13, 11, 'Donated to Tories before licence granted', 'high'),
    (14, 13, 'Met minister before MoD contract awarded', 'high'),
    (15, 14, 'Bonus paid same month as NHS contract', 'high'),
    (16, 19, '14 Treasury meetings while on retainer', 'high'),
    (17, 20, '9 Home Office meetings for border contract', 'high'),
    (18, 17, 'Took speaking fee from party he covered', 'medium'),
]

con.executemany(
    "INSERT OR IGNORE INTO flags(id, person_id, summary, severity) VALUES (?,?,?,?)",
    flags
)

con.commit()
con.close()
print("Seeded 20 people, transactions, and flags.")
