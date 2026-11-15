"""Seed data/bank.db for SQL drills. Stdlib only. Deterministic (seed=42).

Run: python data/seed_bank_db.py
Tables: customers, accounts, transactions, loans.
Deliberate quirks for drilling: NULLs, customers with no accounts,
accounts with no transactions, class imbalance on fraud, defaults for credit risk Qs.
"""
import os
import random
import sqlite3
from datetime import date, timedelta

random.seed(42)

HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "bank.db")

SCHEMA = """
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id   INTEGER PRIMARY KEY,
    first_name    TEXT,
    last_name     TEXT,
    birth_date    TEXT,
    city          TEXT,
    region        TEXT,
    segment       TEXT,          -- Retail / Wealth / SME  (some NULL)
    annual_income REAL,          -- some NULL
    signup_date   TEXT
);

CREATE TABLE accounts (
    account_id   INTEGER PRIMARY KEY,
    customer_id  INTEGER REFERENCES customers(customer_id),
    account_type TEXT,           -- current / savings / credit_card
    open_date    TEXT,
    close_date   TEXT,           -- NULL if still open
    balance      REAL,
    status       TEXT            -- open / closed / dormant
);

CREATE TABLE transactions (
    txn_id            INTEGER PRIMARY KEY,
    account_id        INTEGER REFERENCES accounts(account_id),
    txn_ts            TEXT,      -- 'YYYY-MM-DD HH:MM:SS'
    amount            REAL,      -- negative = debit, positive = credit
    merchant_category TEXT,      -- some NULL
    channel           TEXT,      -- card / direct_debit / transfer / atm / mobile
    is_fraud          INTEGER    -- 0/1, heavily imbalanced
);

CREATE TABLE loans (
    loan_id       INTEGER PRIMARY KEY,
    customer_id   INTEGER REFERENCES customers(customer_id),
    loan_type     TEXT,          -- mortgage / personal / car / overdraft
    principal     REAL,
    interest_rate REAL,
    term_months   INTEGER,
    start_date    TEXT,
    status        TEXT,          -- active / closed / default
    credit_score  INTEGER        -- some NULL
);
"""

FIRST = ["Alice", "Ben", "Chloe", "Dan", "Ella", "Farid", "Grace", "Hugo", "Isla",
         "Jack", "Kiran", "Leah", "Mo", "Nina", "Omar", "Priya", "Rhys", "Sara",
         "Tom", "Uma", "Vik", "Wendy", "Yusuf", "Zoe"]
LAST = ["Ahmed", "Brown", "Clarke", "Davies", "Evans", "Foster", "Gill", "Hughes",
        "Iqbal", "Jones", "Khan", "Lewis", "Morgan", "Nolan", "ONeill", "Patel",
        "Quinn", "Roberts", "Smith", "Taylor", "Usman", "Vaughan", "Wright", "Young"]
CITIES = [("Leeds", "North"), ("Manchester", "North"), ("Newcastle", "North"),
          ("Birmingham", "Midlands"), ("Nottingham", "Midlands"),
          ("London", "South"), ("Bristol", "South"), ("Brighton", "South"),
          ("Cardiff", "Wales"), ("Edinburgh", "Scotland"), ("Glasgow", "Scotland")]
SEGMENTS = ["Retail", "Retail", "Retail", "Retail", "Wealth", "SME", None]
CATS = ["groceries", "fuel", "dining", "travel", "utilities", "entertainment",
        "retail", "healthcare", "transfer", None]
CHANNELS = ["card", "card", "card", "direct_debit", "transfer", "atm", "mobile"]


def d(start, end):
    """Random date between two dates."""
    return start + timedelta(days=random.randint(0, (end - start).days))


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executescript(SCHEMA)

    # ---------------- customers ----------------
    customers = []
    for cid in range(1, 201):
        city, region = random.choice(CITIES)
        income = None if random.random() < 0.08 else round(
            random.lognormvariate(10.4, 0.45), 2)
        customers.append((
            cid, random.choice(FIRST), random.choice(LAST),
            d(date(1950, 1, 1), date(2005, 12, 31)).isoformat(),
            city, region, random.choice(SEGMENTS), income,
            d(date(2015, 1, 1), date(2025, 6, 30)).isoformat(),
        ))
    cur.executemany("INSERT INTO customers VALUES (?,?,?,?,?,?,?,?,?)", customers)

    # ---------------- accounts ----------------
    # customers 191-200 deliberately have NO accounts (LEFT JOIN ... IS NULL drills)
    accounts = []
    aid = 1000
    for cid in range(1, 191):
        for _ in range(random.randint(1, 3)):
            aid += 1
            atype = random.choice(["current", "current", "savings", "credit_card"])
            opened = d(date(2015, 1, 1), date(2025, 1, 1))
            if random.random() < 0.12:
                status, closed = "closed", d(opened, date(2025, 9, 30)).isoformat()
            elif random.random() < 0.10:
                status, closed = "dormant", None
            else:
                status, closed = "open", None
            bal = round(random.lognormvariate(7.5, 1.3), 2)
            if atype == "credit_card":
                bal = -bal
            accounts.append((aid, cid, atype, opened.isoformat(), closed, bal, status))
    cur.executemany("INSERT INTO accounts VALUES (?,?,?,?,?,?,?)", accounts)

    # ---------------- transactions ----------------
    # the last ~15% of accounts get zero transactions on purpose
    txns = []
    tid = 0
    for acc in accounts[: int(len(accounts) * 0.85)]:
        for _ in range(random.randint(3, 60)):
            tid += 1
            ts = d(date(2024, 10, 1), date(2025, 9, 30))
            hh, mm, ss = random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)
            if random.random() < 0.18:           # credit (salary etc.)
                amt = round(random.lognormvariate(7.2, 0.6), 2)
            else:                                 # debit
                amt = -round(random.lognormvariate(3.3, 1.1), 2)
            fraud = 1 if random.random() < 0.012 else 0
            if fraud:
                amt = -round(abs(amt) * random.uniform(5, 40), 2)
            txns.append((tid, acc[0], ts.isoformat() + " %02d:%02d:%02d" % (hh, mm, ss),
                         amt, random.choice(CATS), random.choice(CHANNELS), fraud))
    cur.executemany("INSERT INTO transactions VALUES (?,?,?,?,?,?,?)", txns)

    # ---------------- loans ----------------
    loans = []
    lid = 5000
    for cid in range(1, 201):
        if random.random() < 0.45:
            continue
        for _ in range(random.randint(1, 2)):
            lid += 1
            ltype = random.choice(["mortgage", "personal", "personal", "car", "overdraft"])
            principal = {"mortgage": random.uniform(80_000, 450_000),
                         "personal": random.uniform(1_000, 25_000),
                         "car": random.uniform(5_000, 40_000),
                         "overdraft": random.uniform(200, 3_000)}[ltype]
            score = None if random.random() < 0.06 else random.randint(350, 850)
            # lower credit score -> higher default probability
            eff = score if score is not None else 600
            p_def = 0.35 if eff < 550 else 0.12 if eff < 680 else 0.03
            status = ("default" if random.random() < p_def
                      else random.choice(["active", "active", "active", "closed"]))
            loans.append((lid, cid, ltype, round(principal, 2),
                          round(random.uniform(2.1, 29.9), 2),
                          random.choice([12, 24, 36, 60, 120, 240, 300]),
                          d(date(2016, 1, 1), date(2025, 6, 30)).isoformat(),
                          status, score))
    cur.executemany("INSERT INTO loans VALUES (?,?,?,?,?,?,?,?,?)", loans)

    conn.commit()
    for t in ("customers", "accounts", "transactions", "loans"):
        n = cur.execute("SELECT COUNT(*) FROM " + t).fetchone()[0]
        print("%13s: %6d rows" % (t, n))
    conn.close()
    print("\nwrote " + DB_PATH)


if __name__ == "__main__":
    main()
