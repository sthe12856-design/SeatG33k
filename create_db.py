import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH     = os.path.join(BASE_DIR, "Database", "seatg33k.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "Database", "schema.sql")
SEED_PATH   = os.path.join(BASE_DIR, "Database", "seed.sql")

# Remove existing database so we start clean
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print(f"Removed existing database at {DB_PATH}")

conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = ON;")

with open(SCHEMA_PATH, "r") as f:
    conn.executescript(f.read())
print("Schema applied.")

with open(SEED_PATH, "r") as f:
    conn.executescript(f.read())
print("Seed data applied.")

# ── Quick verification ──────────────────────────────────────────────────────
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM participant")
print(f"  Participants : {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM manager")
print(f"  Managers     : {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM division")
print(f"  Divisions    : {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM session")
print(f"  Sessions     : {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM seat")
print(f"  Seats        : {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM session_enrollment")
print(f"  Enrollments  : {cur.fetchone()[0]}")

print("\nCapacity overview (per session):")
cur.execute("""
    SELECT session_name, max_participants, enrolled_count, available_by_capacity
    FROM v_session_capacity
    ORDER BY sess_id
""")
for row in cur.fetchall():
    print(f"  {row[0]:<20} cap={row[1]}  enrolled={row[2]}  avail={row[3]}")

print("\nDivision quotas per session:")
cur.execute("""
    SELECT session_name, division_name, max_seats, enrolled_count, available_seats
    FROM v_division_session_capacity
    ORDER BY sess_id, div_id
""")
for row in cur.fetchall():
    print(f"  {row[0]:<20} {row[1]:<12} max={row[2]}  enrolled={row[3]}  avail={row[4]}")

conn.close()
print(f"\nDatabase ready: {DB_PATH}")
